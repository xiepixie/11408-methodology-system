#!/usr/bin/env python3
"""Kaoyan Portal Local Server Launcher.

Updates manifest and starts a lightweight local HTTP server for the Kaoyan Reading Portal.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import os
import socketserver
import sys
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
KAOYAN_DIR = REPO_ROOT / "kaoyan"
PORTAL_DIR = KAOYAN_DIR / "portal"

# Import manifest builder directly
sys.path.insert(0, str(REPO_ROOT / "infra" / "scripts"))
import generate_portal_manifest


def find_free_port(start_port: int = 8080) -> int:
    import socket
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port


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

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(KAOYAN_DIR))
    
    print("\n" + "=" * 60)
    print("🚀 Kaoyan Knowledge & Reading Portal")
    print("=" * 60)
    print(f"📡 Serving at: {url}")
    print(f"📁 Root directory: {KAOYAN_DIR}")
    print("⌨️  快捷键:")
    print("   • Cmd/Ctrl + K  : 全局秒级模糊检索")
    print("   • J / K         : 上下切换手册")
    print("   • [             : 展开/折叠侧边栏")
    print("   • F             : 全屏专注模式 (Zen Mode)")
    print("   • T             : 明暗主题切换")
    print("=" * 60)
    print("按 Ctrl + C 退出服务\n")

    if not args.no_browser:
        webbrowser.open(url)

    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 服务已停止。")


if __name__ == "__main__":
    main()
