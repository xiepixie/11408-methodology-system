/**
 * Kaoyan Knowledge & Reading Portal - Interactive Core Logic (v2.5 Pro)
 * Zero-dependency Vanilla ES6+ architecture
 * Supports both direct file:// opening and local HTTP server
 */

(function () {
  'use strict';

  // External Recommended Courses Registry
  const EXTERNAL_COURSES = [
    {
      id: 'ext_lucy_c2',
      title: 'English with Lucy · Beautiful British English C2 (Proficiency)',
      type: 'Course',
      code: 'EWL-C2',
      subject: 'english1',
      subject_name: '外部课程 · 英语母语级',
      sub_subject: '12周进阶研修体系',
      url: 'file:///Users/xpx/Downloads/%E6%95%99%E8%82%B2/%E5%9C%A8%E7%BA%BF%E8%AF%BE%E7%A8%8B/English%20with%20Lucy%20-%20Beautiful%20British%20English%20C2%20Programme%20(Proficiency)%202026-5/index.html',
      isExternal: true,
      tags: ['lucy', 'c2', 'english with lucy', '母语', '口语', 'british english', 'speaking', 'functional language', 'listening']
    }
  ];

  // State
  const state = {
    manifest: null,
    documents: [],
    currentSubject: 'all',
    currentSubSubject: 'all',
    currentType: 'all',
    starOnly: false,
    selectedDocId: null,
    starredIds: new Set(JSON.parse(localStorage.getItem('kaoyan_stars') || '[]')),
    drillMastery: JSON.parse(localStorage.getItem('kaoyan_drill_mastery') || '{}'),
    recentIds: JSON.parse(localStorage.getItem('kaoyan_recents') || '[]'),
    theme: localStorage.getItem('kaoyan_theme') || 'dark',
    pdfInvert: localStorage.getItem('kaoyan_pdf_invert') === 'true',
    fontScale: parseFloat(localStorage.getItem('kaoyan_font_scale')) || 1.0,
    zenMode: false,
    sidebarCollapsed: window.innerWidth <= 768,
    
    // Command Palette State
    cmdScope: 'all',
    cmdSelectedIndex: 0,
    cmdMatches: [],
  };

  // DOM Elements
  const el = {
    app: document.getElementById('app'),
    sidebar: document.getElementById('sidebar'),
    sidebarOverlay: document.getElementById('sidebar-overlay'),
    themeToggle: document.getElementById('theme-toggle'),
    sidebarToggle: document.getElementById('sidebar-toggle'),
    expandSidebarBtn: document.getElementById('expand-sidebar-btn'),
    mobileMenuBtn: document.getElementById('mobile-menu-btn'),
    cmdTrigger: document.getElementById('cmd-k-trigger'),
    subjectTabs: document.getElementById('subject-tabs'),
    subFilterSection: document.getElementById('sub-filter-section'),
    subFilterChips: document.getElementById('sub-filter-chips'),
    typePills: document.getElementById('type-pills'),
    filterStarBtn: document.getElementById('filter-star-btn'),
    listStats: document.getElementById('list-stats'),
    documentList: document.getElementById('document-list'),
    manifestDate: document.getElementById('manifest-date'),

    // Top Navigation & Breadcrumbs
    crumbRoot: document.getElementById('crumb-root'),
    crumbSubject: document.getElementById('crumb-subject'),
    crumbModule: document.getElementById('crumb-module'),
    crumbTitle: document.getElementById('crumb-title'),
    
    // Center Stepper
    navStepper: document.getElementById('nav-stepper'),
    prevDocBtn: document.getElementById('prev-doc-btn'),
    nextDocBtn: document.getElementById('next-doc-btn'),
    docStepperPos: document.getElementById('doc-stepper-pos'),

    // Action Buttons & Reader Controls
    twinModelBtn: document.getElementById('twin-model-btn'),
    masteryStatusBtn: document.getElementById('mastery-status-btn'),
    masteryIcon: document.getElementById('mastery-icon'),
    masteryText: document.getElementById('mastery-text'),
    fontSizeGroup: document.getElementById('font-size-group'),
    fontDecBtn: document.getElementById('font-dec-btn'),
    fontIncBtn: document.getElementById('font-inc-btn'),
    fontSizeIndicator: document.getElementById('font-size-indicator'),
    pdfInvertBtn: document.getElementById('pdf-invert-btn'),
    starBtn: document.getElementById('star-btn'),
    copyBtn: document.getElementById('copy-btn'),
    copyMenu: document.getElementById('copy-menu'),
    openExternalBtn: document.getElementById('open-external-btn'),
    zenBtn: document.getElementById('zen-btn'),

    // Viewports
    welcomeScreen: document.getElementById('welcome-screen'),
    pdfViewerWrapper: document.getElementById('pdf-viewer-wrapper'),
    pdfViewer: document.getElementById('pdf-viewer'),
    markdownViewerWrapper: document.getElementById('markdown-viewer-wrapper'),
    drillMetaBanner: document.getElementById('drill-meta-banner'),
    drillScopeBox: document.getElementById('drill-scope-box'),
    drillScopeText: document.getElementById('drill-scope-text'),
    drillOwnerBox: document.getElementById('drill-owner-box'),
    drillOwnerLink: document.getElementById('drill-owner-link'),
    markdownBody: document.getElementById('markdown-body'),
    drillTocSidebar: document.getElementById('drill-toc-sidebar'),
    drillTocNav: document.getElementById('drill-toc-nav'),
    heroMathCount: document.getElementById('hero-math-count'),
    hero408Count: document.getElementById('hero-408-count'),
    heroEngCount: document.getElementById('hero-eng-count'),
    heroSysCount: document.getElementById('hero-sys-count'),
    recentSection: document.getElementById('recent-section'),
    recentChips: document.getElementById('recent-chips'),

    // Command Modal (Spotlight)
    cmdModal: document.getElementById('cmd-modal'),
    cmdInput: document.getElementById('cmd-input'),
    cmdClearBtn: document.getElementById('cmd-clear-btn'),
    cmdFilterTabs: document.getElementById('cmd-filter-tabs'),
    cmdResults: document.getElementById('cmd-results'),
    cmdResultsCount: document.getElementById('cmd-results-count'),
    cmdCloseBtn: document.getElementById('cmd-close-btn'),
    toast: document.getElementById('toast'),

    // Image Lightbox Modal
    imageLightboxOverlay: document.getElementById('image-lightbox-overlay'),
    imageLightboxBackdrop: document.getElementById('image-lightbox-backdrop'),
    imageLightboxClose: document.getElementById('image-lightbox-close'),
    imageLightboxImg: document.getElementById('image-lightbox-img'),
    imageLightboxCaption: document.getElementById('image-lightbox-caption'),

    // Floating Annotation Popovers
    selectionPopover: document.getElementById('selection-popover'),
    highlightActionPopover: document.getElementById('highlight-action-popover'),
    highlightCurrentTag: document.getElementById('highlight-current-tag'),
    highlightBtnDelete: document.getElementById('highlight-btn-delete'),
  };

  // --------------------------------------------------------------------------
  // Font Size Scaling System
  // --------------------------------------------------------------------------
  const FONT_SCALE_STEPS = [0.85, 0.92, 1.0, 1.10, 1.20, 1.32, 1.45, 1.60, 1.80];

  function applyFontScale(scale) {
    state.fontScale = Math.max(0.75, Math.min(2.0, scale));
    document.documentElement.style.setProperty('--article-font-scale', state.fontScale.toString());
    if (el.fontSizeIndicator) {
      el.fontSizeIndicator.textContent = Math.round(state.fontScale * 100) + '%';
    }
    localStorage.setItem('kaoyan_font_scale', state.fontScale.toString());
  }

  function adjustFontScale(direction) {
    let current = state.fontScale || 1.0;
    if (direction > 0) {
      const next = FONT_SCALE_STEPS.find(s => s > current + 0.02);
      applyFontScale(next !== undefined ? next : Math.min(2.0, current * 1.1));
    } else {
      const prev = [...FONT_SCALE_STEPS].reverse().find(s => s < current - 0.02);
      applyFontScale(prev !== undefined ? prev : Math.max(0.75, current * 0.9));
    }
  }

  // --------------------------------------------------------------------------
  // Initialization
  // --------------------------------------------------------------------------
  async function init() {
    applyTheme(state.theme);
    applyPdfInvert(state.pdfInvert);
    applyFontScale(state.fontScale);
    bindEvents();
    await loadManifest();
  }

  // --------------------------------------------------------------------------
  // Data Loading (Dual Mode: window.__KAOYAN_MANIFEST__ for file:// & fetch for http://)
  // --------------------------------------------------------------------------
  async function loadManifest() {
    // 1. Direct memory / JS manifest (100% immune to CORS on file:// protocol)
    if (window.__KAOYAN_MANIFEST__ && window.__KAOYAN_MANIFEST__.meta) {
      state.manifest = window.__KAOYAN_MANIFEST__;
      state.documents = state.manifest.documents || [];
      renderInitialData();
      return;
    }

    // 2. Fetch fallback (for HTTP servers)
    try {
      const res = await fetch('data/manifest.json?v=' + Date.now());
      if (!res.ok) throw new Error('HTTP ' + res.status);
      state.manifest = await res.json();
      state.documents = state.manifest.documents || [];
      renderInitialData();
    } catch (err) {
      console.warn('Direct fetch failed, checking fallback...', err);
      el.documentList.innerHTML = `
        <div class="empty-state">
          <span>❌ 无法读取 manifest 数据</span>
          <small style="margin-top:8px;">请先运行 <code>python3 infra/scripts/generate_portal_manifest.py</code> 生成数据，或使用 <code>python3 infra/scripts/serve_portal.py</code> 启动服务。</small>
        </div>
      `;
    }
  }

  function renderInitialData() {
    const meta = state.manifest.meta;
    // Counts in tabs
    if (document.getElementById('count-all')) document.getElementById('count-all').textContent = meta.total_documents;
    if (meta.subject_counts) {
      if (document.getElementById('count-math1')) document.getElementById('count-math1').textContent = meta.subject_counts.math1 || 0;
      if (document.getElementById('count-408')) document.getElementById('count-408').textContent = meta.subject_counts['408'] || 0;
      if (document.getElementById('count-english1')) document.getElementById('count-english1').textContent = meta.subject_counts.english1 || 0;
      if (document.getElementById('count-system')) document.getElementById('count-system').textContent = meta.subject_counts.system || 0;
    }
    // Hero counts
    if (el.heroMathCount) el.heroMathCount.textContent = meta.subject_counts.math1 || 0;
    if (el.hero408Count) el.hero408Count.textContent = meta.subject_counts['408'] || 0;
    if (el.heroEngCount) el.heroEngCount.textContent = meta.subject_counts.english1 || 0;
    if (el.heroSysCount) el.heroSysCount.textContent = meta.subject_counts.system || 0;

    if (el.manifestDate) {
      const d = new Date(meta.generated_at);
      el.manifestDate.textContent = '已索引: ' + d.toLocaleDateString();
    }

    renderSubFilterChips();
    renderDocumentList();
    renderRecents();

    // Auto-select last doc if in URL hash
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      selectDocument(hash);
    }
  }

  // --------------------------------------------------------------------------
  // Theme & Reading Modes
  // --------------------------------------------------------------------------
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('kaoyan_theme', theme);
    if (el.themeToggle) {
      el.themeToggle.querySelector('.theme-icon').textContent = theme === 'dark' ? '☀️' : '🌓';
    }
  }

  function toggleTheme() {
    applyTheme(state.theme === 'dark' ? 'light' : 'dark');
  }

  function applyPdfInvert(invert) {
    state.pdfInvert = invert;
    localStorage.setItem('kaoyan_pdf_invert', invert ? 'true' : 'false');
    if (el.pdfViewerWrapper) {
      el.pdfViewerWrapper.classList.toggle('pdf-invert', invert);
    }
    if (el.pdfInvertBtn) {
      el.pdfInvertBtn.classList.toggle('active', invert);
      el.pdfInvertBtn.querySelector('.btn-text').textContent = invert ? '普通阅读' : '护眼暗色';
    }
  }

  function togglePdfInvert() {
    applyPdfInvert(!state.pdfInvert);
    showToast(state.pdfInvert ? '🌙 已开启 PDF 护眼夜间反色模式' : '☀️ 已切换回常规 PDF 显示');
  }

  function toggleSidebar(forceState) {
    state.sidebarCollapsed = typeof forceState === 'boolean' ? forceState : !state.sidebarCollapsed;
    el.sidebar.classList.toggle('collapsed', state.sidebarCollapsed);
    if (el.sidebarOverlay) {
      el.sidebarOverlay.classList.toggle('show', !state.sidebarCollapsed && window.innerWidth <= 768);
    }
  }

  function toggleZenMode(forceState) {
    state.zenMode = typeof forceState === 'boolean' ? forceState : !state.zenMode;
    document.body.classList.toggle('zen-mode', state.zenMode);
    el.zenBtn.querySelector('.btn-text').textContent = state.zenMode ? '退出专注' : '专注阅读';
    showToast(state.zenMode ? '已进入全屏专注模式 (按 ESC 或 F 退出)' : '已退出专注模式');
  }

  // --------------------------------------------------------------------------
  // Filtering & Document List Rendering
  // --------------------------------------------------------------------------
  function getFilteredDocuments() {
    return state.documents.filter(doc => {
      // Subject filter
      if (state.currentSubject !== 'all' && doc.subject !== state.currentSubject) return false;
      // Sub-subject filter
      if (state.currentSubSubject !== 'all' && doc.sub_subject !== state.currentSubSubject) return false;
      // Type filter
      if (state.currentType !== 'all' && doc.type !== state.currentType) return false;
      // Star filter
      if (state.starOnly && !state.starredIds.has(doc.id)) return false;
      return true;
    });
  }

  function renderSubFilterChips() {
    let subSubjects = new Set();
    state.documents.forEach(doc => {
      if (state.currentSubject === 'all' || doc.subject === state.currentSubject) {
        if (doc.sub_subject) subSubjects.add(doc.sub_subject);
      }
    });

    let list = Array.from(subSubjects);
    if (state.manifest && state.manifest.sub_subjects && state.manifest.sub_subjects[state.currentSubject]) {
      const order = state.manifest.sub_subjects[state.currentSubject];
      list.sort((a, b) => {
        const idxA = order.indexOf(a);
        const idxB = order.indexOf(b);
        if (idxA !== -1 && idxB !== -1) return idxA - idxB;
        if (idxA !== -1) return -1;
        if (idxB !== -1) return 1;
        return a.localeCompare(b, 'zh-CN');
      });
    }

    if (list.length <= 1) {
      el.subFilterSection.style.display = 'none';
      state.currentSubSubject = 'all';
      return;
    }

    el.subFilterSection.style.display = 'block';
    let html = `<button class="chip-btn ${state.currentSubSubject === 'all' ? 'active' : ''}" data-sub="all">全部模块</button>`;
    list.forEach(sub => {
      const active = state.currentSubSubject === sub ? 'active' : '';
      html += `<button class="chip-btn ${active}" data-sub="${escapeHtml(sub)}">${escapeHtml(sub)}</button>`;
    });
    el.subFilterChips.innerHTML = html;
  }

  function renderDocumentList() {
    const docs = getFilteredDocuments();
    el.listStats.textContent = `${docs.length} 篇`;

    if (docs.length === 0) {
      el.documentList.innerHTML = `
        <div class="empty-state">
          <span>🔍 无匹配的手册文件</span>
        </div>
      `;
      updateStepperUI();
      return;
    }

    const html = docs.map(doc => {
      const isSelected = doc.id === state.selectedDocId;
      const isStarred = state.starredIds.has(doc.id);
      const isDrill = doc.type === 'Drill' || doc.format === 'markdown';
      
      let masteryBadge = '';
      if (isDrill) {
        const m = state.drillMastery[doc.id] || 'unstarted';
        const icon = m === 'mastered' ? '🟢' : (m === 'review' ? '🟡' : '⚪');
        masteryBadge = `<span class="card-mastery-badge" title="掌握状态: ${m}">${icon}</span>`;
      }

      const codeHtml = doc.code ? `<span class="badge-code">${escapeHtml(doc.code)}</span>` : '';

      return `
        <div class="doc-card ${isSelected ? 'active' : ''}" data-id="${escapeHtml(doc.id)}" id="card-${escapeHtml(doc.id)}">
          <div class="doc-card-top">
            <span class="badge-type ${doc.type}">${doc.type}</span>
            ${codeHtml}
            <span class="badge-sub">${escapeHtml(doc.sub_subject)}</span>
          </div>
          <div class="doc-card-title">${masteryBadge}${escapeHtml(doc.title)}</div>
          <div class="doc-card-bottom">
            <span>${escapeHtml(doc.size_human)} · ${escapeHtml(doc.modified_date)}</span>
            <button class="card-star-toggle ${isStarred ? 'starred' : ''}" data-star-id="${escapeHtml(doc.id)}" title="${isStarred ? '取消收藏' : '收藏'}">
              ${isStarred ? '★' : '☆'}
            </button>
          </div>
        </div>
      `;
    }).join('');

    el.documentList.innerHTML = html;
    updateStepperUI();
  }

  // --------------------------------------------------------------------------
  // Document Selection & Dual-Engine View
  // --------------------------------------------------------------------------
  function selectDocument(docId) {
    const extCourse = EXTERNAL_COURSES.find(c => c.id === docId);
    if (extCourse) {
      window.open(extCourse.url, '_blank');
      showToast('🚀 已在新窗口启动 ' + extCourse.title);
      return;
    }

    const doc = state.documents.find(d => d.id === docId);
    if (!doc) return;

    state.selectedDocId = docId;
    window.location.hash = docId;

    // Save to recents
    state.recentIds = [docId, ...state.recentIds.filter(id => id !== docId)].slice(0, 10);
    localStorage.setItem('kaoyan_recents', JSON.stringify(state.recentIds));

    // Update List UI Active state
    document.querySelectorAll('.doc-card').forEach(c => c.classList.remove('active'));
    const activeCard = document.getElementById('card-' + docId);
    if (activeCard) {
      activeCard.classList.add('active');
      activeCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Update Breadcrumbs
    el.crumbSubject.textContent = doc.subject_name;
    el.crumbSubject.setAttribute('data-subject', doc.subject);
    el.crumbModule.textContent = doc.sub_subject;
    el.crumbModule.setAttribute('data-module', doc.sub_subject);
    el.crumbTitle.textContent = (doc.code ? `[${doc.code}] ` : '') + doc.title;

    // Update Action Buttons
    el.starBtn.disabled = false;
    el.copyBtn.disabled = false;
    el.openExternalBtn.disabled = false;
    el.zenBtn.disabled = false;

    const isStarred = state.starredIds.has(docId);
    el.starBtn.classList.toggle('starred', isStarred);
    el.starBtn.querySelector('.action-icon').textContent = isStarred ? '★' : '☆';
    el.starBtn.querySelector('.btn-text').textContent = isStarred ? '已收藏' : '收藏';

    // Route between Markdown Drill Engine and PDF Viewer Engine
    if (doc.format === 'markdown') {
      renderMarkdownDoc(doc);
    } else {
      renderPdfDoc(doc);
    }

    updateStepperUI();

    // Auto-close sidebar on small screens
    if (window.innerWidth <= 768) {
      toggleSidebar(true);
    }
  }

  function renderPdfDoc(doc) {
    el.welcomeScreen.style.display = 'none';
    if (el.markdownViewerWrapper) el.markdownViewerWrapper.style.display = 'none';
    el.pdfViewerWrapper.style.display = 'block';

    if (el.twinModelBtn) el.twinModelBtn.style.display = 'none';
    if (el.masteryStatusBtn) el.masteryStatusBtn.style.display = 'none';
    if (el.fontSizeGroup) el.fontSizeGroup.style.display = 'none';
    el.pdfInvertBtn.disabled = false;
    
    // Set PDF src with standard Open Parameters (Fit Width + Auto Bookmarks)
    const pdfUrlWithParams = `${doc.url}#view=FitH&pagemode=bookmarks`;
    if (el.pdfViewer.src !== pdfUrlWithParams) {
      el.pdfViewer.src = pdfUrlWithParams;
    }
  }

  // Helper to render inline markdown links and KaTeX formulas in banner & callouts
  function renderInlineContentWithKaTeX(text) {
    if (!text) return '';
    let res = text;

    // 1. Format markdown links [title](url) -> <span class="doc-inline-chip">title</span>
    res = res.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<span class="doc-inline-chip">$1</span>');

    // 2. Render LaTeX inline math $...$ or \(...\)
    res = res.replace(/\$([^\$\n\r]+?)\$/g, (match, formula) => {
      if (window.katex) {
        try {
          return katex.renderToString(formula.trim(), { displayMode: false, throwOnError: false });
        } catch (e) {
          return match;
        }
      }
      return match;
    });

    res = res.replace(/\\\(([\s\S]*?)\\\)/g, (match, formula) => {
      if (window.katex) {
        try {
          return katex.renderToString(formula.trim(), { displayMode: false, throwOnError: false });
        } catch (e) {
          return match;
        }
      }
      return match;
    });

    return res;
  }

  // Image Lightbox Controls
  function openImageLightbox(src, caption) {
    if (!el.imageLightboxOverlay || !el.imageLightboxImg) return;
    el.imageLightboxImg.src = src;
    if (el.imageLightboxCaption) {
      el.imageLightboxCaption.innerHTML = caption ? `<span class="caption-icon">📐</span> ${renderInlineContentWithKaTeX(caption)}` : '';
      el.imageLightboxCaption.style.display = caption ? 'block' : 'none';
    }
    el.imageLightboxOverlay.style.display = 'flex';
    requestAnimationFrame(() => {
      el.imageLightboxOverlay.classList.add('active');
    });
  }

  function closeImageLightbox() {
    if (!el.imageLightboxOverlay) return;
    el.imageLightboxOverlay.classList.remove('active');
    setTimeout(() => {
      el.imageLightboxOverlay.style.display = 'none';
      if (el.imageLightboxImg) el.imageLightboxImg.src = '';
    }, 200);
  }

  // Preprocess Markdown & Custom Callouts
  function preprocessMarkdown(content) {
    if (!content) return '';
    let text = content;

    // Strip YAML frontmatter at the beginning of the file
    text = text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '');

    // Strip Obsidian comments %% ... %%
    text = text.replace(/%%[\s\S]*?%%/g, '');

    // Convert Obsidian Wikilink images ![[assets/xxx.svg]] or ![[assets/xxx.svg|400]]
    text = text.replace(/!\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]/g, (match, path, altOrWidth) => {
      const alt = altOrWidth ? altOrWidth : '';
      return `![${alt}](${path})`;
    });

    const formatInlineLinks = (str) => {
      return str.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, title, url) => {
        return `<a href="${url}" class="doc-inline-link">${title}</a>`;
      });
    };

    // Convert custom semantic callouts
    text = text.replace(/^>\s*(?:\[!TRAIN\]|\*?\*?训练定位\*?\*?)[：:]\s*(.+)$/gm, 
      (m, p1) => `<div class="callout callout-train"><div class="callout-title">🎯 训练定位</div>${formatInlineLinks(p1)}</div>`);
    
    text = text.replace(/^>\s*(?:\[!MODEL\]|\*?\*?模型归属\*?\*?)[：:]\s*(.+)$/gm, 
      (m, p1) => `<div class="callout callout-model"><div class="callout-title">📘 模型归属</div>${formatInlineLinks(p1)}</div>`);

    text = text.replace(/^>\s*(?:\[!TRAP\]|\[!WARNING\]|\*?\*?易错警示\*?\*?|\*?\*?风险警示\*?\*?)[：:]\s*(.+)$/gm, 
      (m, p1) => `<div class="callout callout-trap"><div class="callout-title">⚠️ 易错警示 / 不可逆变形债务</div>${formatInlineLinks(p1)}</div>`);

    text = text.replace(/^>\s*(?:\[!RULE\]|\[!TIP\]|\*?\*?解题规则\*?\*?|\*?\*?动作规则\*?\*?)[：:]\s*(.+)$/gm, 
      (m, p1) => `<div class="callout callout-rule"><div class="callout-title">💡 解题动作规则</div>${formatInlineLinks(p1)}</div>`);

    // Standfirst subtitle italic line: *A review of thousands...*
    text = text.replace(/^\*([^\*\n\r]{15,})\*$/gm, '<div class="article-standfirst">$1</div>');

    // Convert paragraph anchor ^p01 -> subtle anchor badge
    text = text.replace(/\^p(\d{2})/g, '<span class="block-anchor" data-anchor="^p$1" title="Obsidian 段落锚点 ^p$1">#p$1</span>');

    // Convert Obsidian diagnostic highlights ==span== [?] or ==span== [!] or ==span== [★] or ==span== [~]
    text = text.replace(/==([\s\S]+?)==\s*(\[\?\]|\[!\]|\[★\]|\[\~\]|\?|!|★|~)/g, (match, span, tag) => {
      const tagClean = tag.replace(/[\[\]]/g, '');
      let tagClass = 'anno-unknown';
      let label = '[?] 词义不懂';
      if (tagClean === '!') { tagClass = 'anno-syntax'; label = '[!] 句法脱节'; }
      else if (tagClean === '★') { tagClass = 'anno-star'; label = '[★] 优质表达'; }
      else if (tagClean === '~') { tagClass = 'anno-verify'; label = '[~] 存疑验证'; }
      return `<mark class="anno-highlight ${tagClass}" data-raw-span="${escapeHtml(span)}" data-raw-tag="[${tagClean}]" title="${label}">${span}<span class="anno-badge">[${tagClean}]</span></mark>`;
    });

    // Convert plain Obsidian highlights ==span==
    text = text.replace(/==([\s\S]+?)==/g, (match, span) => {
      return `<mark class="anno-highlight anno-plain" data-raw-span="${escapeHtml(span)}" data-raw-tag="==" title="高亮标记">${span}</mark>`;
    });

    return text;
  }

  function renderMarkdownDoc(doc, preserveScroll = false) {
    const stage = document.querySelector('.drill-stage');
    const savedScrollTop = stage ? stage.scrollTop : 0;

    el.welcomeScreen.style.display = 'none';
    el.pdfViewerWrapper.style.display = 'none';
    if (el.markdownViewerWrapper) el.markdownViewerWrapper.style.display = 'flex';

    el.pdfInvertBtn.disabled = true;
    if (el.masteryStatusBtn) {
      el.masteryStatusBtn.style.display = 'inline-flex';
      updateMasteryButtonUI(doc.id);
    }
    if (el.fontSizeGroup) {
      el.fontSizeGroup.style.display = 'inline-flex';
    }

    // Training Scope with KaTeX
    if (el.drillScopeBox) {
      if (doc.training_scope) {
        el.drillScopeBox.style.display = 'flex';
        el.drillScopeText.innerHTML = renderInlineContentWithKaTeX(doc.training_scope);
      } else {
        el.drillScopeBox.style.display = 'none';
      }
    }

    // Model Owner & Twin Model Link with KaTeX
    if (el.drillOwnerBox && el.twinModelBtn) {
      if (doc.model_owner) {
        el.drillOwnerBox.style.display = 'flex';
        el.drillOwnerLink.innerHTML = renderInlineContentWithKaTeX(doc.model_owner);
        el.drillOwnerLink.onclick = (e) => {
          e.preventDefault();
          if (doc.model_owner_id) selectDocument(doc.model_owner_id);
          else showToast('关联模型: ' + doc.model_owner);
        };

        el.twinModelBtn.style.display = 'inline-flex';
        el.twinModelBtn.onclick = () => {
          if (doc.model_owner_id) selectDocument(doc.model_owner_id);
          else showToast('关联模型: ' + doc.model_owner);
        };
      } else {
        el.drillOwnerBox.style.display = 'none';
        el.twinModelBtn.style.display = 'none';
      }
    }

    // =========================================================================
    // Markdown + KaTeX Mathematical Isolation Pipeline
    // =========================================================================
    let raw = doc.content || '';

    // Extract metadata for English Daily Reading articles
    let isEnglishArticle = doc.subject === 'english1' && (doc.id.includes('reading') || (doc.code && doc.code.startsWith('ENG-READ')));
    let metaHeaderHtml = '';

    if (isEnglishArticle && raw) {
      const fmMatch = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
      if (fmMatch) {
        const fmLines = fmMatch[1].split('\n');
        const articleMeta = { topics: [] };
        let currentKey = '';
        for (const line of fmLines) {
          const mKey = line.match(/^([a-zA-Z0-9_-]+):\s*(.*)$/);
          if (mKey) {
            currentKey = mKey[1].trim();
            const val = mKey[2].trim();
            if (val) articleMeta[currentKey] = val;
          } else if (line.trim().startsWith('-') && currentKey === 'topics') {
            articleMeta.topics.push(line.replace(/^\s*-\s*/, '').trim());
          }
        }

        metaHeaderHtml = `
          <div class="english-article-header">
            <div class="english-meta-pills">
              ${articleMeta.source ? `<span class="meta-pill pill-source">📰 ${escapeHtml(articleMeta.source)}</span>` : ''}
              ${articleMeta.published ? `<span class="meta-pill pill-date">📅 ${escapeHtml(articleMeta.published)}</span>` : ''}
              ${articleMeta.section ? `<span class="meta-pill pill-section">🏷️ ${escapeHtml(articleMeta.section)}</span>` : ''}
              ${articleMeta.author ? `<span class="meta-pill pill-author">✍️ ${escapeHtml(articleMeta.author)}</span>` : ''}
              ${articleMeta.source_page ? `<span class="meta-pill pill-page">📄 P.${escapeHtml(articleMeta.source_page)}</span>` : ''}
            </div>
            ${articleMeta.topics && articleMeta.topics.length > 0 ? `
              <div class="english-topic-chips">
                ${articleMeta.topics.map(t => `<span class="topic-chip">#${escapeHtml(t)}</span>`).join('')}
              </div>
            ` : ''}
            <div class="english-diag-legend">
              <span class="legend-title">⚡ 首读诊断：</span>
              <span class="legend-item"><span class="anno-badge anno-unknown">[?]</span> 词义不懂</span>
              <span class="legend-item"><span class="anno-badge anno-syntax">[!]</span> 句法脱节</span>
              <span class="legend-item"><span class="anno-badge anno-star">[★]</span> 优质表达</span>
              <span class="legend-item"><span class="anno-badge anno-verify">[~]</span> 存疑验证</span>
            </div>
          </div>
        `;
      }
    }

    const mathStore = [];
    const codeStore = [];

    // Step 1: Protect fenced code blocks and inline code
    raw = raw.replace(/```[\s\S]*?```/g, (match) => {
      const id = `%%%CODE_BLOCK_${codeStore.length}%%%`;
      codeStore.push(match);
      return id;
    });

    raw = raw.replace(/`[^`\n\r]+`/g, (match) => {
      const id = `%%%CODE_INLINE_${codeStore.length}%%%`;
      codeStore.push(match);
      return id;
    });

    // Step 2: Extract Display Math: $$...$$ or \[...\]
    raw = raw.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
      const id = `\n\n%%%MATH_DISPLAY_${mathStore.length}%%%\n\n`;
      mathStore.push({ type: 'display', formula: formula.trim() });
      return id;
    });

    raw = raw.replace(/\\\[([\s\S]*?)\\\]/g, (match, formula) => {
      const id = `\n\n%%%MATH_DISPLAY_${mathStore.length}%%%\n\n`;
      mathStore.push({ type: 'display', formula: formula.trim() });
      return id;
    });

    // Step 3: Extract Inline Math: $...$ or \(...\)
    raw = raw.replace(/\$([^\$\n\r]+?)\$/g, (match, formula) => {
      if (!formula.trim()) return match;
      const id = `%%%MATH_INLINE_${mathStore.length}%%%`;
      mathStore.push({ type: 'inline', formula: formula.trim() });
      return id;
    });

    raw = raw.replace(/\\\(([\s\S]*?)\\\)/g, (match, formula) => {
      const id = `%%%MATH_INLINE_${mathStore.length}%%%`;
      mathStore.push({ type: 'inline', formula: formula.trim() });
      return id;
    });

    // Step 4: Restore code blocks before parsing Markdown
    raw = raw.replace(/%%%CODE_BLOCK_(\d+)%%%/g, (m, idx) => codeStore[parseInt(idx, 10)]);
    raw = raw.replace(/%%%CODE_INLINE_(\d+)%%%/g, (m, idx) => codeStore[parseInt(idx, 10)]);

    // Step 5: Process semantic callouts (Train, Model, Trap, Rule)
    raw = preprocessMarkdown(raw);

    // Step 6: Parse Markdown cleanly with Marked (No LaTeX symbols to corrupt)
    let html = '';
    if (window.marked && typeof window.marked.parse === 'function') {
      html = window.marked.parse(raw);
    } else {
      html = raw
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/\n\n/gim, '<p></p>');
    }

    // Step 7: Restore & Render KaTeX Math directly to HTML
    html = html.replace(/<p>\s*%%%MATH_DISPLAY_(\d+)%%%\s*<\/p>/g, (m, idx) => {
      const item = mathStore[parseInt(idx, 10)];
      if (!item) return m;
      if (window.katex) {
        try {
          return katex.renderToString(item.formula, { displayMode: true, throwOnError: false });
        } catch (e) {
          return `<div class="katex-error">${escapeHtml(item.formula)}</div>`;
        }
      }
      return `<div class="katex-display">$$${escapeHtml(item.formula)}$$</div>`;
    });

    html = html.replace(/%%%MATH_DISPLAY_(\d+)%%%/g, (m, idx) => {
      const item = mathStore[parseInt(idx, 10)];
      if (!item) return m;
      if (window.katex) {
        try {
          return katex.renderToString(item.formula, { displayMode: true, throwOnError: false });
        } catch (e) {
          return `<div class="katex-error">${escapeHtml(item.formula)}</div>`;
        }
      }
      return `<div class="katex-display">$$${escapeHtml(item.formula)}$$</div>`;
    });

    html = html.replace(/%%%MATH_INLINE_(\d+)%%%/g, (m, idx) => {
      const item = mathStore[parseInt(idx, 10)];
      if (!item) return m;
      if (window.katex) {
        try {
          return katex.renderToString(item.formula, { displayMode: false, throwOnError: false });
        } catch (e) {
          return `<span class="katex-error">${escapeHtml(item.formula)}</span>`;
        }
      }
      return `<span class="katex-inline">$${escapeHtml(item.formula)}$</span>`;
    });

    el.markdownBody.innerHTML = metaHeaderHtml + html;

    if (isEnglishArticle) {
      el.markdownBody.classList.add('english-reading-mode');
    } else {
      el.markdownBody.classList.remove('english-reading-mode');
    }

    // =========================================================================
    // Image & Diagram Card Polish Pipeline (Size, Centering, Caption & Lightbox)
    // =========================================================================
    const lastSlash = doc.url ? doc.url.lastIndexOf('/') : -1;
    const baseDir = lastSlash !== -1 ? doc.url.substring(0, lastSlash + 1) : '';

    el.markdownBody.querySelectorAll('img').forEach(img => {
      const src = img.getAttribute('src');
      if (src && !src.startsWith('http://') && !src.startsWith('https://') && !src.startsWith('/') && !src.startsWith('data:')) {
        const cleanSrc = src.replace(/^\.\//, '');
        img.src = baseDir + cleanSrc;
      }

      img.classList.add('diagram-asset');

      // Parse custom width and caption from alt (e.g. "alt text|495" or "500")
      let alt = img.getAttribute('alt') || '';
      let customWidth = null;
      let cleanCaption = alt;

      const widthMatch = alt.match(/\|\s*(\d+)(?:x\d+)?\s*$/);
      if (widthMatch) {
        customWidth = widthMatch[1] + 'px';
        cleanCaption = alt.replace(/\|\s*(\d+)(?:x\d+)?\s*$/, '').trim();
      } else if (/^\d+$/.test(alt.trim())) {
        customWidth = alt.trim() + 'px';
        cleanCaption = '';
      }

      if (customWidth) {
        img.style.maxWidth = `min(100%, ${customWidth})`;
      }

      // Add Lightbox Click Event
      img.title = '点击放大查看高清图示';
      img.addEventListener('click', () => openImageLightbox(img.src, cleanCaption || '图示查看'));

      // Wrap image into elegant figure card with caption
      const parent = img.parentElement;
      const figure = document.createElement('figure');
      figure.className = 'diagram-figure-card';

      // Insert figure before image or replace parent p if single
      if (parent && parent.tagName === 'P' && parent.children.length === 1 && parent.textContent.trim() === '') {
        parent.parentNode.insertBefore(figure, parent);
        figure.appendChild(img);
        parent.remove();
      } else {
        img.parentNode.insertBefore(figure, img);
        figure.appendChild(img);
      }

      if (cleanCaption && cleanCaption !== '题目图示' && cleanCaption !== '图示') {
        const figcaption = document.createElement('figcaption');
        figcaption.className = 'diagram-caption';
        figcaption.innerHTML = `<span class="caption-icon">📐</span> ${renderInlineContentWithKaTeX(cleanCaption)}`;
        figure.appendChild(figcaption);
      }
    });

    // Step 9: Attach click listeners on Obsidian diagnostic highlights
    el.markdownBody.querySelectorAll('.anno-highlight').forEach(hl => {
      hl.addEventListener('click', (e) => {
        e.stopPropagation();
        const span = hl.getAttribute('data-raw-span') || hl.textContent;
        const tag = hl.getAttribute('data-raw-tag') || '[?]';
        const rect = hl.getBoundingClientRect();

        activeHighlightElement = {
          span: span,
          tag: tag,
          pElem: hl.closest('p, li, blockquote, div')
        };

        if (el.highlightActionPopover) {
          if (el.selectionPopover) el.selectionPopover.style.display = 'none';
          if (el.highlightCurrentTag) {
            const tagMap = {
              '[?]': '[?] 词义不懂',
              '[!]': '[!] 句法脱节',
              '[★]': '[★] 优质表达',
              '[~]': '[~] 存疑验证',
              '==': '普通高亮'
            };
            el.highlightCurrentTag.textContent = tagMap[tag] || `${tag} 标注`;
          }
          el.highlightActionPopover.style.display = 'flex';
          el.highlightActionPopover.style.left = `${rect.left + rect.width / 2}px`;
          el.highlightActionPopover.style.top = `${rect.top}px`;
        }
      });
    });

    // Generate TOC
    generateDrillTOC();

    // Scroll stage to top or preserve
    if (stage) {
      if (preserveScroll) {
        stage.scrollTop = savedScrollTop;
      } else {
        stage.scrollTop = 0;
      }
    }
  }

  // --------------------------------------------------------------------------
  // Annotation & Selection Engine
  // --------------------------------------------------------------------------
  let currentSelectionContext = null;
  let activeHighlightElement = null;

  function hidePopovers() {
    if (el.selectionPopover) el.selectionPopover.style.display = 'none';
    if (el.highlightActionPopover) el.highlightActionPopover.style.display = 'none';
    currentSelectionContext = null;
    activeHighlightElement = null;
  }

  let selectionRafId = null;

  function handleTextSelection() {
    if (selectionRafId) cancelAnimationFrame(selectionRafId);
    selectionRafId = requestAnimationFrame(() => {
      const selection = window.getSelection();
      if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
        if (!activeHighlightElement) {
          if (el.selectionPopover) el.selectionPopover.style.display = 'none';
        }
        return;
      }

      const selectedText = selection.toString().trim();
      if (!selectedText || selectedText.length < 1) {
        if (el.selectionPopover) el.selectionPopover.style.display = 'none';
        return;
      }

      // Ensure selection is inside markdownBody
      const range = selection.getRangeAt(0);
      let container = range.commonAncestorContainer;
      if (container.nodeType === Node.TEXT_NODE) container = container.parentElement;
      if (!el.markdownBody || (!el.markdownBody.contains(container) && el.markdownBody !== container)) {
        if (el.selectionPopover) el.selectionPopover.style.display = 'none';
        return;
      }

      // Find closest paragraph or block ID
      let paragraphId = '';
      let pElem = container.closest('p, li, blockquote, div, h1, h2, h3');
      if (pElem) {
        const match = pElem.textContent.match(/\^p\d{2}/);
        if (match) paragraphId = match[0];
      }

      const rect = range.getBoundingClientRect();
      if (rect.width === 0 && rect.height === 0) return;

      currentSelectionContext = {
        selected_text: selectedText,
        paragraph_id: paragraphId,
        doc_id: state.selectedDocId
      };

      if (el.selectionPopover) {
        if (el.highlightActionPopover) el.highlightActionPopover.style.display = 'none';
        el.selectionPopover.style.display = 'flex';
        el.selectionPopover.style.left = `${rect.left + rect.width / 2}px`;
        el.selectionPopover.style.top = `${rect.top}px`;
      }
    });
  }

  function applyAnnotation(markType) {
    if (!currentSelectionContext || !state.selectedDocId) return;
    const doc = state.documents.find(d => d.id === state.selectedDocId);
    if (!doc || !doc.local_path) return;

    const payload = {
      local_path: doc.local_path,
      action: 'add',
      selected_text: currentSelectionContext.selected_text,
      mark_type: markType,
      paragraph_id: currentSelectionContext.paragraph_id || ''
    };

    fetch('/api/annotate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        showToast(`✅ ${markType} 标注已同步至本地 Markdown`);
        doc.content = data.content;
        renderMarkdownDoc(doc, true);
        hidePopovers();
        window.getSelection().removeAllRanges();
      } else {
        showToast('⚠️ 标注保存失败: ' + (data.error || '未知错误'));
      }
    })
    .catch(() => {
      showToast(`📝 离线模式: 运行 python3 infra/scripts/serve_portal.py 享受实时落盘`);
      hidePopovers();
    });
  }

  function removeAnnotation(spanText, tag, paragraphId) {
    if (!state.selectedDocId) return;
    const doc = state.documents.find(d => d.id === state.selectedDocId);
    if (!doc || !doc.local_path) return;

    const payload = {
      local_path: doc.local_path,
      action: 'remove',
      selected_text: spanText,
      mark_type: tag,
      paragraph_id: paragraphId || ''
    };

    fetch('/api/annotate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        showToast('🗑️ 已从本地 Markdown 中清除标注');
        doc.content = data.content;
        renderMarkdownDoc(doc, true);
        hidePopovers();
      } else {
        showToast('⚠️ 清除失败: ' + (data.error || '未知错误'));
      }
    })
    .catch(() => {
      showToast('⚠️ 服务未连接，无法修改本地文件');
      hidePopovers();
    });
  }

  function generateDrillTOC() {
    if (!el.drillTocNav || !el.markdownBody) return;
    const headings = el.markdownBody.querySelectorAll('h2, h3');
    if (headings.length === 0) {
      el.drillTocNav.innerHTML = '<span style="font-size:12px;color:var(--text-muted);">暂无子标题</span>';
      return;
    }

    let tocHtml = '';
    headings.forEach((h, idx) => {
      const id = 'drill-h-' + idx;
      h.id = id;
      const isH3 = h.tagName.toLowerCase() === 'h3';
      const text = h.textContent.replace(/^#+\s*/, '').trim();
      tocHtml += `<a href="#${id}" class="drill-toc-link ${isH3 ? 'h3' : ''}" title="${escapeHtml(text)}">${escapeHtml(text)}</a>`;
    });
    el.drillTocNav.innerHTML = tocHtml;

    // Smooth scroll on TOC click
    el.drillTocNav.querySelectorAll('.drill-toc-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').replace('#', '');
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  function updateMasteryButtonUI(docId) {
    if (!el.masteryIcon || !el.masteryText) return;
    const mastery = state.drillMastery[docId] || 'unstarted';
    const masteryMeta = {
      'unstarted': { icon: '⚪', text: '未练' },
      'review': { icon: '🟡', text: '存疑二刷' },
      'mastered': { icon: '🟢', text: '已掌握' }
    };
    const meta = masteryMeta[mastery] || masteryMeta.unstarted;
    el.masteryIcon.textContent = meta.icon;
    el.masteryText.textContent = meta.text;
  }

  function cycleMastery(docId) {
    if (!docId) return;
    const levels = ['unstarted', 'review', 'mastered'];
    const current = state.drillMastery[docId] || 'unstarted';
    const nextLevel = levels[(levels.indexOf(current) + 1) % levels.length];
    state.drillMastery[docId] = nextLevel;
    localStorage.setItem('kaoyan_drill_mastery', JSON.stringify(state.drillMastery));
    
    updateMasteryButtonUI(docId);
    
    const msgs = {
      'unstarted': '⚪ 标记为: 未练',
      'review': '🟡 标记为: 存疑需二刷',
      'mastered': '🟢 标记为: 已完全掌握！'
    };
    showToast(msgs[nextLevel]);
    renderDocumentList();
  }

  function updateStepperUI() {
    const docs = getFilteredDocuments();
    if (!state.selectedDocId || docs.length === 0) {
      el.navStepper.style.display = 'none';
      return;
    }
    el.navStepper.style.display = 'flex';
    const currentIndex = docs.findIndex(d => d.id === state.selectedDocId);
    if (currentIndex === -1) {
      el.docStepperPos.textContent = `- / ${docs.length}`;
      el.prevDocBtn.disabled = true;
      el.nextDocBtn.disabled = true;
    } else {
      el.docStepperPos.textContent = `${currentIndex + 1} / ${docs.length}`;
      el.prevDocBtn.disabled = false;
      el.nextDocBtn.disabled = false;
      
      const prevDoc = docs[(currentIndex - 1 + docs.length) % docs.length];
      const nextDoc = docs[(currentIndex + 1) % docs.length];
      el.prevDocBtn.title = `上一篇: ${prevDoc.title} (K)`;
      el.nextDocBtn.title = `下一篇: ${nextDoc.title} (J)`;
    }
  }

  function renderRecents() {
    if (state.recentIds.length === 0) {
      el.recentSection.style.display = 'none';
      return;
    }
    el.recentSection.style.display = 'block';
    const recentDocs = state.recentIds.map(id => state.documents.find(d => d.id === id)).filter(Boolean);
    el.recentChips.innerHTML = recentDocs.map(doc => `
      <div class="recent-chip" data-id="${escapeHtml(doc.id)}">
        <span class="badge-type ${doc.type}" style="font-size:9px;">${doc.type}</span>
        <span>${escapeHtml(doc.title)}</span>
      </div>
    `).join('');
  }

  function toggleStar(docId) {
    if (state.starredIds.has(docId)) {
      state.starredIds.delete(docId);
      showToast('已取消收藏');
    } else {
      state.starredIds.add(docId);
      showToast('⭐ 已添加到收藏');
    }
    localStorage.setItem('kaoyan_stars', JSON.stringify(Array.from(state.starredIds)));
    renderDocumentList();
    if (state.selectedDocId === docId) {
      const isStarred = state.starredIds.has(docId);
      el.starBtn.classList.toggle('starred', isStarred);
      el.starBtn.querySelector('.action-icon').textContent = isStarred ? '★' : '☆';
      el.starBtn.querySelector('.btn-text').textContent = isStarred ? '已收藏' : '收藏';
    }
  }

  // --------------------------------------------------------------------------
  // Command Palette / Spotlight Search (Raycast-grade Evolution)
  // --------------------------------------------------------------------------
  function openCmdPalette() {
    el.cmdModal.style.display = 'flex';
    el.cmdInput.value = '';
    if (el.cmdClearBtn) el.cmdClearBtn.style.display = 'none';
    el.cmdInput.focus();
    state.cmdScope = 'all';
    updateCmdScopeTabsUI();
    searchCmd('');
  }

  function closeCmdPalette() {
    el.cmdModal.style.display = 'none';
  }

  function updateCmdScopeTabsUI() {
    document.querySelectorAll('.cmd-scope-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-cmd-scope') === state.cmdScope);
    });
  }

  function cycleCmdScope() {
    const scopes = ['all', 'math1', '408', 'english1', 'Atlas', 'star'];
    const currIdx = scopes.indexOf(state.cmdScope);
    state.cmdScope = scopes[(currIdx + 1) % scopes.length];
    updateCmdScopeTabsUI();
    searchCmd(el.cmdInput.value);
  }

  function highlightMatches(text, query) {
    if (!query || !text) return escapeHtml(text);
    const escapedText = escapeHtml(text);
    const escapedQuery = escapeHtml(query).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(${escapedQuery})`, 'gi');
    return escapedText.replace(regex, '<mark class="search-hl">$1</mark>');
  }

  function searchCmd(query) {
    let q = query.trim().toLowerCase();
    
    // Toggle Clear button
    if (el.cmdClearBtn) {
      el.cmdClearBtn.style.display = q.length > 0 ? 'inline-flex' : 'none';
    }

    // Auto-scope shortcuts (e.g. @math, @408, @atlas, @star)
    if (q.startsWith('@math') || q.startsWith('@数')) {
      state.cmdScope = 'math1';
      q = q.replace(/^(@math|@数)\s*/, '');
      updateCmdScopeTabsUI();
    } else if (q.startsWith('@408') || q.startsWith('@计')) {
      state.cmdScope = '408';
      q = q.replace(/^(@408|@计)\s*/, '');
      updateCmdScopeTabsUI();
    } else if (q.startsWith('@eng') || q.startsWith('@英')) {
      state.cmdScope = 'english1';
      q = q.replace(/^(@eng|@英)\s*/, '');
      updateCmdScopeTabsUI();
    } else if (q.startsWith('@atlas') || q.startsWith('@总图')) {
      state.cmdScope = 'Atlas';
      q = q.replace(/^(@atlas|@总图)\s*/, '');
      updateCmdScopeTabsUI();
    } else if (q.startsWith('@star') || q.startsWith('@藏')) {
      state.cmdScope = 'star';
      q = q.replace(/^(@star|@藏)\s*/, '');
      updateCmdScopeTabsUI();
    }

    // Filter by Scope
    let pool = state.documents;
    if (state.cmdScope === 'math1') pool = pool.filter(d => d.subject === 'math1');
    else if (state.cmdScope === '408') pool = pool.filter(d => d.subject === '408');
    else if (state.cmdScope === 'english1') pool = pool.filter(d => d.subject === 'english1');
    else if (state.cmdScope === 'Atlas') pool = pool.filter(d => d.type === 'Atlas');
    else if (state.cmdScope === 'star') pool = pool.filter(d => state.starredIds.has(d.id));

    if (!q) {
      state.cmdMatches = pool.slice(0, 30);
    } else {
      state.cmdMatches = pool.filter(doc => {
        const titleMatch = doc.title.toLowerCase().includes(q);
        const codeMatch = doc.code && doc.code.toLowerCase().includes(q);
        const filenameMatch = doc.filename.toLowerCase().includes(q);
        const subMatch = doc.sub_subject.toLowerCase().includes(q);
        const tagMatch = doc.tags && doc.tags.some(t => t.toLowerCase().includes(q));
        const scopeMatch = doc.training_scope && doc.training_scope.toLowerCase().includes(q);
        return titleMatch || codeMatch || filenameMatch || subMatch || tagMatch || scopeMatch;
      }).slice(0, 40);

      // Match external courses if applicable
      if (state.cmdScope === 'all' || state.cmdScope === 'english1') {
        const matchedCourses = EXTERNAL_COURSES.filter(c => {
          const tMatch = c.title.toLowerCase().includes(q);
          const cMatch = c.code.toLowerCase().includes(q);
          const tagMatch = c.tags.some(t => t.toLowerCase().includes(q));
          return tMatch || cMatch || tagMatch;
        });
        state.cmdMatches = [...matchedCourses, ...state.cmdMatches];
      }
    }

    state.cmdSelectedIndex = 0;
    renderCmdResults(q);
  }

  function renderCmdResults(query) {
    if (el.cmdResultsCount) {
      el.cmdResultsCount.textContent = `找到 ${state.cmdMatches.length} 篇手册`;
    }

    if (state.cmdMatches.length === 0) {
      el.cmdResults.innerHTML = `
        <div class="empty-state">
          <span>🔍 未找到相关手册或知识点</span>
          <small style="margin-top:4px;">试试切换分类范围或输入核心词（如 <code>Cache</code>、<code>Taylor</code>、<code>树</code>）</small>
        </div>
      `;
      return;
    }

    el.cmdResults.innerHTML = state.cmdMatches.map((doc, idx) => {
      const isSelected = idx === state.cmdSelectedIndex;
      const codeHtml = doc.code ? `<span class="badge-code">${highlightMatches(doc.code, query)}</span>` : '';
      const highlightedTitle = highlightMatches(doc.title, query);
      const isStarred = state.starredIds.has(doc.id);

      return `
        <div class="cmd-result-item ${isSelected ? 'selected' : ''}" data-index="${idx}" data-id="${escapeHtml(doc.id)}">
          <div class="cmd-result-left">
            <span class="badge-type ${doc.type}">${doc.type}</span>
            ${codeHtml}
            <span class="cmd-result-title">${highlightedTitle}</span>
            ${isStarred ? '<span style="color:#f59e0b;font-size:11px;">★</span>' : ''}
          </div>
          <div class="cmd-result-right">
            <span class="cmd-result-meta">${escapeHtml(doc.subject_name)} · ${escapeHtml(doc.sub_subject)}</span>
          </div>
        </div>
      `;
    }).join('');
  }

  // --------------------------------------------------------------------------
  // Navigation & Shortcuts
  // --------------------------------------------------------------------------
  function navigateList(direction) {
    const docs = getFilteredDocuments();
    if (docs.length === 0) return;
    const currentIndex = docs.findIndex(d => d.id === state.selectedDocId);
    let nextIndex = 0;
    if (currentIndex !== -1) {
      nextIndex = (currentIndex + direction + docs.length) % docs.length;
    }
    selectDocument(docs[nextIndex].id);
  }

  // --------------------------------------------------------------------------
  // Copy Actions
  // --------------------------------------------------------------------------
  function copyTextToClipboard(text, successMsg) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(successMsg);
    }).catch(() => {
      showToast('❌ 复制失败');
    });
  }

  function handleCopyAction(type) {
    const doc = state.documents.find(d => d.id === state.selectedDocId);
    if (!doc) return;
    
    if (type === 'rel-path') {
      copyTextToClipboard(doc.local_path, '📋 已复制相对路径: ' + doc.local_path);
    } else if (type === 'obsidian') {
      const link = `[[${doc.full_name}]]`;
      copyTextToClipboard(link, '📋 已复制 Obsidian 双链: ' + link);
    } else if (type === 'latex') {
      const cmd = `\\href{run:${doc.local_path}}{${doc.code ? `[${doc.code}] ` : ''}${doc.title}}`;
      copyTextToClipboard(cmd, '📋 已复制 LaTeX 引用命令');
    }
    if (el.copyMenu) el.copyMenu.style.display = 'none';
  }

  // --------------------------------------------------------------------------
  // Toast & Utilities
  // --------------------------------------------------------------------------
  let toastTimer = null;
  function showToast(msg) {
    el.toast.textContent = msg;
    el.toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      el.toast.classList.remove('show');
    }, 2400);
  }

  function openExternal() {
    const doc = state.documents.find(d => d.id === state.selectedDocId);
    if (!doc) return;
    window.open(doc.url, '_blank');
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // --------------------------------------------------------------------------
  // Event Binding
  // --------------------------------------------------------------------------
  function bindEvents() {
    // Theme toggle
    if (el.themeToggle) el.themeToggle.addEventListener('click', toggleTheme);

    // Sidebar toggles
    if (el.sidebarToggle) el.sidebarToggle.addEventListener('click', () => toggleSidebar(true));
    if (el.expandSidebarBtn) el.expandSidebarBtn.addEventListener('click', () => toggleSidebar(false));
    if (el.mobileMenuBtn) el.mobileMenuBtn.addEventListener('click', () => toggleSidebar(false));
    if (el.sidebarOverlay) el.sidebarOverlay.addEventListener('click', () => toggleSidebar(true));

    // Command palette trigger
    if (el.cmdTrigger) el.cmdTrigger.addEventListener('click', openCmdPalette);
    if (el.cmdCloseBtn) el.cmdCloseBtn.addEventListener('click', closeCmdPalette);
    if (el.cmdClearBtn) {
      el.cmdClearBtn.addEventListener('click', () => {
        el.cmdInput.value = '';
        el.cmdInput.focus();
        searchCmd('');
      });
    }
    if (el.cmdModal) {
      el.cmdModal.addEventListener('click', (e) => {
        if (e.target === el.cmdModal) closeCmdPalette();
      });
    }

    if (el.cmdInput) el.cmdInput.addEventListener('input', (e) => searchCmd(e.target.value));

    // Modal scope tabs
    if (el.cmdFilterTabs) {
      el.cmdFilterTabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.cmd-scope-btn');
        if (!btn) return;
        state.cmdScope = btn.getAttribute('data-cmd-scope');
        updateCmdScopeTabsUI();
        searchCmd(el.cmdInput.value);
      });
    }

    // Interactive Breadcrumbs
    if (el.crumbRoot) {
      el.crumbRoot.addEventListener('click', () => {
        const allTab = document.querySelector(`.tab-btn[data-subject="all"]`);
        if (allTab) allTab.click();
      });
    }
    if (el.crumbSubject) {
      el.crumbSubject.addEventListener('click', () => {
        const sub = el.crumbSubject.getAttribute('data-subject');
        if (sub) {
          const tab = document.querySelector(`.tab-btn[data-subject="${sub}"]`);
          if (tab) tab.click();
        }
      });
    }
    if (el.crumbModule) {
      el.crumbModule.addEventListener('click', () => {
        const mod = el.crumbModule.getAttribute('data-module');
        if (mod) {
          const chip = document.querySelector(`.chip-btn[data-sub="${mod}"]`);
          if (chip) chip.click();
        }
      });
    }

    // Stepper navigation
    if (el.prevDocBtn) el.prevDocBtn.addEventListener('click', () => navigateList(-1));
    if (el.nextDocBtn) el.nextDocBtn.addEventListener('click', () => navigateList(1));

    // Subject tabs click
    if (el.subjectTabs) {
      el.subjectTabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.tab-btn');
        if (!btn) return;
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.currentSubject = btn.getAttribute('data-subject');
        state.currentSubSubject = 'all';
        renderSubFilterChips();
        renderDocumentList();
      });
    }

    // Hero stat cards click
    document.querySelectorAll('.stat-box').forEach(box => {
      box.addEventListener('click', () => {
        const sub = box.getAttribute('data-subject');
        const tab = document.querySelector(`.tab-btn[data-subject="${sub}"]`);
        if (tab) tab.click();
      });
    });

    // Sub-subject chips click
    if (el.subFilterChips) {
      el.subFilterChips.addEventListener('click', (e) => {
        const btn = e.target.closest('.chip-btn');
        if (!btn) return;
        document.querySelectorAll('.chip-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.currentSubSubject = btn.getAttribute('data-sub');
        renderDocumentList();
      });
    }

    // Type pills click
    if (el.typePills) {
      el.typePills.addEventListener('click', (e) => {
        const btn = e.target.closest('.pill-btn');
        if (!btn) return;
        document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.currentType = btn.getAttribute('data-type');
        renderDocumentList();
      });
    }

    // Filter Star only
    if (el.filterStarBtn) {
      el.filterStarBtn.addEventListener('click', () => {
        state.starOnly = !state.starOnly;
        el.filterStarBtn.classList.toggle('active', state.starOnly);
        renderDocumentList();
      });
    }

    // Document Card & Star click in List
    if (el.documentList) {
      el.documentList.addEventListener('click', (e) => {
        const starBtn = e.target.closest('.card-star-toggle');
        if (starBtn) {
          e.stopPropagation();
          toggleStar(starBtn.getAttribute('data-star-id'));
          return;
        }
        const card = e.target.closest('.doc-card');
        if (card) {
          selectDocument(card.getAttribute('data-id'));
        }
      });
    }

    // Recent chips click
    if (el.recentChips) {
      el.recentChips.addEventListener('click', (e) => {
        const chip = e.target.closest('.recent-chip');
        if (chip) selectDocument(chip.getAttribute('data-id'));
      });
    }

    // Top action bar buttons
    if (el.pdfInvertBtn) el.pdfInvertBtn.addEventListener('click', togglePdfInvert);
    if (el.starBtn) {
      el.starBtn.addEventListener('click', () => {
        if (state.selectedDocId) toggleStar(state.selectedDocId);
      });
    }

    if (el.masteryStatusBtn) {
      el.masteryStatusBtn.addEventListener('click', () => {
        if (state.selectedDocId) cycleMastery(state.selectedDocId);
      });
    }
    
    // Copy dropdown
    if (el.copyBtn) {
      el.copyBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isHidden = el.copyMenu.style.display === 'none';
        el.copyMenu.style.display = isHidden ? 'flex' : 'none';
      });
    }
    if (el.copyMenu) {
      el.copyMenu.addEventListener('click', (e) => {
        const item = e.target.closest('.copy-menu-item');
        if (item) {
          handleCopyAction(item.getAttribute('data-copy-type'));
        }
      });
    }
    document.addEventListener('click', () => {
      if (el.copyMenu) el.copyMenu.style.display = 'none';
    }, { passive: true });

    if (el.openExternalBtn) el.openExternalBtn.addEventListener('click', openExternal);
    if (el.zenBtn) el.zenBtn.addEventListener('click', () => toggleZenMode());

    // Image Lightbox Close bindings
    if (el.imageLightboxClose) el.imageLightboxClose.addEventListener('click', closeImageLightbox);
    if (el.imageLightboxBackdrop) el.imageLightboxBackdrop.addEventListener('click', closeImageLightbox);

    // Selection Popover Type Buttons
    document.querySelectorAll('.selection-popover .popover-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const mark = btn.getAttribute('data-mark');
        if (mark) applyAnnotation(mark);
      });
    });

    // Highlight Action Popover Tag Switch Buttons
    document.querySelectorAll('.highlight-action-popover .popover-mini-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const mark = btn.getAttribute('data-switch-mark');
        if (activeHighlightElement && mark) {
          const pMatch = activeHighlightElement.pElem ? activeHighlightElement.pElem.textContent.match(/\^p\d{2}/) : null;
          currentSelectionContext = {
            selected_text: activeHighlightElement.span,
            paragraph_id: pMatch ? pMatch[0] : '',
            doc_id: state.selectedDocId
          };
          applyAnnotation(mark);
        }
      });
    });

    // Highlight Action Delete Button
    if (el.highlightBtnDelete) {
      el.highlightBtnDelete.addEventListener('click', (e) => {
        e.stopPropagation();
        if (activeHighlightElement) {
          const pMatch = activeHighlightElement.pElem ? activeHighlightElement.pElem.textContent.match(/\^p\d{2}/) : null;
          removeAnnotation(activeHighlightElement.span, activeHighlightElement.tag, pMatch ? pMatch[0] : '');
        }
      });
    }

    // Prevent popover buttons from clearing browser text selection
    if (el.selectionPopover) {
      el.selectionPopover.addEventListener('mousedown', (e) => {
        e.preventDefault();
        e.stopPropagation();
      });
    }

    if (el.highlightActionPopover) {
      el.highlightActionPopover.addEventListener('mousedown', (e) => {
        e.preventDefault();
        e.stopPropagation();
      });
    }

    // Text Selection Event on Markdown Body
    document.addEventListener('mouseup', (e) => {
      if (el.selectionPopover && el.selectionPopover.contains(e.target)) return;
      if (el.highlightActionPopover && el.highlightActionPopover.contains(e.target)) return;
      setTimeout(handleTextSelection, 15);
    });

    document.addEventListener('keyup', (e) => {
      if (e.shiftKey) {
        setTimeout(handleTextSelection, 15);
      }
    });

    // Dismiss popovers on outside click
    document.addEventListener('mousedown', (e) => {
      if (el.selectionPopover && el.selectionPopover.style.display !== 'none' && !el.selectionPopover.contains(e.target)) {
        if (!e.target.closest('.anno-highlight')) {
          hidePopovers();
        }
      }
      if (el.highlightActionPopover && el.highlightActionPopover.style.display !== 'none' && !el.highlightActionPopover.contains(e.target)) {
        if (!e.target.closest('.anno-highlight')) {
          hidePopovers();
        }
      }
    });

    // Command palette click
    if (el.cmdResults) {
      el.cmdResults.addEventListener('click', (e) => {
        const item = e.target.closest('.cmd-result-item');
        if (item) {
          const id = item.getAttribute('data-id');
          selectDocument(id);
          closeCmdPalette();
        }
      });
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      // Image Lightbox Close (ESC)
      if (el.imageLightboxOverlay && el.imageLightboxOverlay.classList.contains('active')) {
        if (e.key === 'Escape') {
          e.preventDefault();
          closeImageLightbox();
          return;
        }
      }

      // Command palette open (Cmd+K / Ctrl+K)
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (el.cmdModal.style.display === 'flex') closeCmdPalette();
        else openCmdPalette();
        return;
      }

      // If Command Modal is Open
      if (el.cmdModal.style.display === 'flex') {
        if (e.key === 'Escape') {
          e.preventDefault();
          closeCmdPalette();
        } else if (e.key === 'Tab') {
          e.preventDefault();
          cycleCmdScope();
        } else if (e.key === 'ArrowDown') {
          e.preventDefault();
          state.cmdSelectedIndex = Math.min(state.cmdSelectedIndex + 1, state.cmdMatches.length - 1);
          renderCmdResults(el.cmdInput.value);
          const selected = el.cmdResults.querySelector('.cmd-result-item.selected');
          if (selected) selected.scrollIntoView({ block: 'nearest' });
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          state.cmdSelectedIndex = Math.max(state.cmdSelectedIndex - 1, 0);
          renderCmdResults(el.cmdInput.value);
          const selected = el.cmdResults.querySelector('.cmd-result-item.selected');
          if (selected) selected.scrollIntoView({ block: 'nearest' });
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (state.cmdMatches[state.cmdSelectedIndex]) {
            selectDocument(state.cmdMatches[state.cmdSelectedIndex].id);
            closeCmdPalette();
          }
        }
        return;
      }

      // Outside inputs shortcuts
      if (['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
        return;
      }

      if (e.key === '/' && !e.metaKey && !e.ctrlKey) {
        e.preventDefault();
        openCmdPalette();
      } else if (e.key === '[') {
        e.preventDefault();
        toggleSidebar();
      } else if (e.key.toLowerCase() === 'f') {
        e.preventDefault();
        toggleZenMode();
      } else if (e.key.toLowerCase() === 'j') {
        e.preventDefault();
        navigateList(1);
      } else if (e.key.toLowerCase() === 'k') {
        e.preventDefault();
        navigateList(-1);
      } else if (e.key.toLowerCase() === 'm') {
        e.preventDefault();
        if (state.selectedDocId) cycleMastery(state.selectedDocId);
      } else if (e.key === 'Escape' && state.zenMode) {
        e.preventDefault();
        toggleZenMode(false);
      } else if (e.key.toLowerCase() === 't') {
        e.preventDefault();
        toggleTheme();
      } else if (e.shiftKey && e.key.toLowerCase() === 'd') {
        e.preventDefault();
        togglePdfInvert();
      } else if ((e.metaKey || e.ctrlKey) && (e.key === '=' || e.key === '+')) {
        e.preventDefault();
        adjustFontScale(1);
      } else if ((e.metaKey || e.ctrlKey) && e.key === '-') {
        e.preventDefault();
        adjustFontScale(-1);
      } else if ((e.metaKey || e.ctrlKey) && e.key === '0') {
        e.preventDefault();
        applyFontScale(1.0);
      }
    });

    // Font Size Stepper Listeners
    if (el.fontDecBtn) el.fontDecBtn.addEventListener('click', () => adjustFontScale(-1));
    if (el.fontIncBtn) el.fontIncBtn.addEventListener('click', () => adjustFontScale(1));
    if (el.fontSizeIndicator) el.fontSizeIndicator.addEventListener('click', () => applyFontScale(1.0));

    // Handle responsive resize
    window.addEventListener('resize', () => {
      if (window.innerWidth <= 768) {
        if (!state.sidebarCollapsed) {
          el.sidebar.classList.add('collapsed');
          state.sidebarCollapsed = true;
        }
      }
    }, { passive: true });
  }

  // Run on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
