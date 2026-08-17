(() => {
  'use strict';

  const isLesson = Boolean(document.querySelector('.badge'));

  // Thin progress line: useful for the long, single-page lessons.
  const progress = document.createElement('div');
  progress.className = 'reading-progress';
  progress.setAttribute('aria-hidden', 'true');
  progress.innerHTML = '<span></span>';
  document.body.appendChild(progress);
  const bar = progress.firstElementChild;

  const updateProgress = () => {
    const root = document.documentElement;
    const max = Math.max(1, root.scrollHeight - root.clientHeight);
    const ratio = Math.min(1, Math.max(0, root.scrollTop / max));
    bar.style.width = `${(ratio * 100).toFixed(2)}%`;
  };
  document.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();

  if (!isLesson) return;

  // Generate a compact TOC from the lesson's H2 headings. This deliberately
  // uses the existing pedagogical structure instead of introducing a second
  // manually maintained navigation tree.
  const headings = [...document.querySelectorAll('main section h2')];
  headings.forEach((heading, index) => {
    if (!heading.id) heading.id = `section-${index + 1}`;
  });

  if (headings.length >= 5) {
    const toc = document.createElement('details');
    toc.className = 'page-toc';
    toc.innerHTML = '<summary>本页目录 · 快速定位</summary><nav aria-label="本页目录"></nav>';
    const nav = toc.querySelector('nav');

    headings.forEach(heading => {
      const link = document.createElement('a');
      link.href = `#${heading.id}`;
      link.textContent = heading.textContent.trim();
      link.title = heading.textContent.trim();
      nav.appendChild(link);
    });

    const header = document.querySelector('header');
    if (header) header.insertAdjacentElement('afterend', toc);

    if (window.matchMedia('(min-width: 1000px)').matches) toc.open = true;

    const links = [...nav.querySelectorAll('a')];
    const syncActiveHeading = () => {
      let activeIndex = 0;
      headings.forEach((heading, index) => {
        if (heading.getBoundingClientRect().top <= 120) activeIndex = index;
      });
      links.forEach((link, index) => link.classList.toggle('active', index === activeIndex));
    };
    document.addEventListener('scroll', syncActiveHeading, { passive: true });
    window.addEventListener('resize', syncActiveHeading, { passive: true });
    syncActiveHeading();
  }

  // Back-to-top is intentionally unobtrusive and only appears after the first
  // screenful; keyboard users still have normal document navigation.
  const topButton = document.createElement('button');
  topButton.className = 'back-to-top';
  topButton.type = 'button';
  topButton.textContent = '↑';
  topButton.setAttribute('aria-label', '返回页面顶部');
  topButton.title = '返回顶部';
  document.body.appendChild(topButton);

  const updateTopButton = () => {
    topButton.classList.toggle('visible', document.documentElement.scrollTop > 700);
  };
  document.addEventListener('scroll', updateTopButton, { passive: true });
  updateTopButton();

  topButton.addEventListener('click', () => {
    const smooth = window.matchMedia('(prefers-reduced-motion: no-preference)').matches;
    window.scrollTo({ top: 0, behavior: smooth ? 'smooth' : 'auto' });
  });
})();
