#!/usr/bin/env python3
"""Kaoyan Portal Local Server Launcher.

Updates manifest and starts a lightweight local HTTP server for the Kaoyan Reading Portal.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import re
import socketserver
import sys
import time
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
KAOYAN_DIR = REPO_ROOT / "kaoyan"
PORTAL_DIR = KAOYAN_DIR / "portal"

# Import manifest builder directly
sys.path.insert(0, str(REPO_ROOT / "infra" / "scripts"))
import generate_portal_manifest

_last_manifest_build_time: float = 0.0
_manifest_cache_ttl: float = 1.0  # Debounce TTL in seconds


def maybe_refresh_manifests(force: bool = False):
    global _last_manifest_build_time
    now = time.time()
    if force or (now - _last_manifest_build_time > _manifest_cache_ttl):
        try:
            generate_portal_manifest.build_manifests()
            _last_manifest_build_time = now
        except Exception as e:
            print(f"[Portal] Warning: manifest auto-refresh error: {e}")


def find_free_port(start_port: int = 8080) -> int:
    import socket
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port


class PortalRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler with REST API support for real-time annotation sync."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(KAOYAN_DIR), **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split("?")[0]
        if clean_path in ("/portal/data/manifest.json", "/data/manifest.json"):
            maybe_refresh_manifests()
            manifest_file = PORTAL_DIR / "data" / "manifest.json"
            if manifest_file.exists():
                data = manifest_file.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.end_headers()
                self.wfile.write(data)
                return

        elif clean_path in ("/portal/data/manifest.js", "/data/manifest.js"):
            maybe_refresh_manifests()
            manifest_js = PORTAL_DIR / "data" / "manifest.js"
            if manifest_js.exists():
                data = manifest_js.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "application/javascript; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.end_headers()
                self.wfile.write(data)
                return

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/annotate":
            self.handle_annotate()
        else:
            self.send_error(404, "API endpoint not found")

    def _send_json(self, data: dict, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def handle_annotate(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            payload = json.loads(post_data.decode("utf-8"))
        except Exception as e:
            return self._send_json({"success": False, "error": f"Invalid JSON payload: {e}"}, 400)

        local_path_str = payload.get("local_path", "")
        action = payload.get("action", "add")
        selected_text = payload.get("selected_text", "").strip()
        mark_type = payload.get("mark_type", "[?]").strip()
        paragraph_id = payload.get("paragraph_id", "").strip()
        context_before = payload.get("context_before", "")
        context_after = payload.get("context_after", "")

        if not local_path_str or not selected_text:
            return self._send_json({"success": False, "error": "Missing local_path or selected_text"}, 400)

        # Resolve and validate target path security
        target_path = (REPO_ROOT / local_path_str).resolve()
        if not target_path.exists() or not str(target_path).startswith(str(KAOYAN_DIR)):
            return self._send_json({"success": False, "error": "Invalid or forbidden file path"}, 403)

        try:
            content = target_path.read_text(encoding="utf-8")
        except Exception as e:
            return self._send_json({"success": False, "error": f"Failed to read file: {e}"}, 500)

        # Execute atomic annotation mutation
        updated_content, success, msg = self._apply_annotation(
            content=content,
            action=action,
            selected_text=selected_text,
            mark_type=mark_type,
            paragraph_id=paragraph_id,
            context_before=context_before,
            context_after=context_after
        )

        if not success:
            return self._send_json({"success": False, "error": msg}, 422)

        try:
            target_path.write_text(updated_content, encoding="utf-8")
        except Exception as e:
            return self._send_json({"success": False, "error": f"Failed to write file: {e}"}, 500)

        return self._send_json({
            "success": True,
            "message": msg,
            "content": updated_content,
            "local_path": local_path_str
        })

    def _apply_annotation(self, content: str, action: str, selected_text: str, mark_type: str, paragraph_id: str, context_before: str, context_after: str) -> tuple[str, bool, str]:
        raw_words = [re.escape(w) for w in re.split(r"\s+", selected_text) if w]
        if not raw_words:
            return content, False, "选中文本为空"
        
        words_pattern = r"\s+".join(raw_words)

        if action == "add":
            already_hl_pattern = rf"==\s*({words_pattern})\s*==(?:\s*(\[\?\]|\[!\]|\[★\]|\[\~\]|\?|!|★|~))?"

            def replace_in_text(target_str: str) -> tuple[str, bool]:
                m_hl = re.search(already_hl_pattern, target_str)
                if m_hl:
                    matched_inner = m_hl.group(1)
                    rep = f"=={matched_inner}==" if mark_type == "==" else f"=={matched_inner}== {mark_type}"
                    new_str = target_str[:m_hl.start()] + rep + target_str[m_hl.end():]
                    return new_str, True
                
                m_plain = re.search(words_pattern, target_str)
                if m_plain:
                    matched_exact = m_plain.group(0)
                    rep = f"=={matched_exact}==" if mark_type == "==" else f"=={matched_exact}== {mark_type}"
                    new_str = target_str[:m_plain.start()] + rep + target_str[m_plain.end():]
                    return new_str, True

                return target_str, False

            if paragraph_id:
                paragraphs = content.split("\n\n")
                found = False
                new_paragraphs = []
                for p in paragraphs:
                    if paragraph_id in p and not found:
                        new_p, ok = replace_in_text(p)
                        if ok:
                            p = new_p
                            found = True
                    new_paragraphs.append(p)
                if found:
                    return "\n\n".join(new_paragraphs), True, f"已同步标注 {mark_type} 至本地文件"

            new_content, ok = replace_in_text(content)
            if ok:
                return new_content, True, f"已同步标注 {mark_type} 至本地文件"
            else:
                return content, False, f"未能在文件中找到目标文本: {selected_text}"

        elif action == "remove":
            hl_pattern = rf"==\s*({words_pattern})\s*==(?:\s*(\[\?\]|\[!\]|\[★\]|\[\~\]|\?|!|★|~))?"

            def remove_in_text(target_str: str) -> tuple[str, bool]:
                m = re.search(hl_pattern, target_str)
                if m:
                    matched_inner = m.group(1)
                    new_str = target_str[:m.start()] + matched_inner + target_str[m.end():]
                    return new_str, True
                return target_str, False

            if paragraph_id:
                paragraphs = content.split("\n\n")
                found = False
                new_paragraphs = []
                for p in paragraphs:
                    if paragraph_id in p and not found:
                        new_p, ok = remove_in_text(p)
                        if ok:
                            p = new_p
                            found = True
                    new_paragraphs.append(p)
                if found:
                    return "\n\n".join(new_paragraphs), True, "已清除本地文件中的高亮标注"

            new_content, ok = remove_in_text(content)
            if ok:
                return new_content, True, "已清除本地文件中的高亮标注"
            else:
                return content, False, f"未找到该高亮标记: {selected_text}"

        return content, False, f"未知操作: {action}"


def main():
    parser = argparse.ArgumentParser(description="Start the Kaoyan Knowledge & Reading Portal")
    parser.add_argument("--port", type=int, default=None, help="Port to serve on")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    parser.add_argument("--no-build", action="store_true", help="Skip manifest rebuild")
    args = parser.parse_args()

    # Step 1: Rebuild manifest
    if not args.no_build:
        print("[1/2] Updating portal manifest...")
        generate_portal_manifest.main()

    # Step 2: Choose Port & Serve
    port = args.port or find_free_port(8080)
    url = f"http://127.0.0.1:{port}/portal/"
    
    print("\n" + "=" * 60)
    print("🚀 Kaoyan Knowledge & Reading Portal (with Real-time Sync)")
    print("=" * 60)
    print(f"📡 Serving at: {url}")
    print(f"📁 Root directory: {KAOYAN_DIR}")
    print("✨ 功能特性:")
    print("   • 📝 网页划词标注实时同步写回本地 Markdown (Obsidian 同步)")
    print("   • ⌘ Cmd/Ctrl + K  : 全局秒级模糊检索")
    print("   • 🌗 T            : 明暗主题切换 (默认护眼暗色)")
    print("   • 🔲 F            : 全屏专注阅读 (Zen Mode)")
    print("=" * 60)
    print("按 Ctrl + C 退出服务\n")

    if not args.no_browser:
        webbrowser.open(url)

    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), PortalRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 服务已停止。")


if __name__ == "__main__":
    main()
