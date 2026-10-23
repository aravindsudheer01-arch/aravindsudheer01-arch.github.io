/* Progressive enhancement only: every case study and link works without JS. */
(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.hidden = false;
    document.documentElement.classList.add('has-menu');
    const closeMenu = () => { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); };
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('click', e => { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', e => { if(e.key === 'Escape' && nav.classList.contains('is-open')) {closeMenu(); toggle.focus();} });
    const mq = window.matchMedia('(min-width: 761px)');
    if (mq.addEventListener) mq.addEventListener('change', closeMenu);
    else if (mq.addListener) mq.addListener(closeMenu);
  }
  const controls = document.querySelector('.project-controls');
  if (controls) {
    controls.hidden = false;
    const cards = Array.from(document.querySelectorAll('[data-project]'));
    const filters = Array.from(document.querySelectorAll('[data-filter]'));
    const input = document.getElementById('project-search');
    const status = document.getElementById('project-count');
    const empty = document.getElementById('empty-state');
    let active = 'all';
    const apply = () => {
      const term = input.value.trim().toLocaleLowerCase(); let visible = 0;
      cards.forEach(card => {
        const show = (active === 'all' || card.dataset.category === active) && card.dataset.search.includes(term);
        card.hidden = !show; if (show) visible++;
      });
      filters.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.filter === active)));
      status.textContent = `${visible} ${visible === 1 ? 'case study' : 'case studies'}`;
      empty.hidden = visible !== 0;
    };
    filters.forEach(b => b.addEventListener('click', () => { active = b.dataset.filter; apply(); }));
    input.addEventListener('input', apply);
  }
  const copy = document.querySelector('.copy-email');
  if (copy && navigator.clipboard && window.isSecureContext) {
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      const status = document.querySelector('.copy-status');
      try { await navigator.clipboard.writeText(copy.dataset.email); status.textContent = 'Email address copied.'; }
      catch (_) { status.textContent = 'Copy unavailable. Use the email link above.'; }
    });
  }
})();
