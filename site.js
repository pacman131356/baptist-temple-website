// Baptist Temple · nav that folds into the BT badge, scroll motion, preview-only forms
(function () {
  var nav = document.getElementById('nav');
  var burger = nav.querySelector('.burger');
  var brand = nav.querySelector('.nav-brand');
  var fine = matchMedia('(hover:hover)').matches;
  var still = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- dropdowns
  function closeMenus() {
    nav.querySelectorAll('.nav-group.open').forEach(function (g) {
      g.classList.remove('open'); g.querySelector('button').setAttribute('aria-expanded', 'false'); g.querySelector('.menu').hidden = true;
    });
  }
  nav.querySelectorAll('.nav-group').forEach(function (g) {
    var b = g.querySelector('button'), m = g.querySelector('.menu'), t;
    function open() { clearTimeout(t); closeMenus(); g.classList.add('open'); b.setAttribute('aria-expanded', 'true'); m.hidden = false; }
    b.addEventListener('click', function (e) { e.stopPropagation(); g.classList.contains('open') ? closeMenus() : open(); });
    if (fine) {
      g.addEventListener('mouseenter', open);
      g.addEventListener('mouseleave', function () { t = setTimeout(closeMenus, 180); });
    }
  });
  document.addEventListener('click', function (e) { if (!nav.contains(e.target)) { closeMenus(); setOpen(false); } });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeMenus(); setOpen(false); } });

  // ---- mobile menu
  function setOpen(o) {
    nav.classList.toggle('open', o);
    burger.setAttribute('aria-expanded', o);
    burger.setAttribute('aria-label', o ? 'Close menu' : 'Open menu');
  }
  burger.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });

  // ---- fold into the badge after scrolling; hover, focus or tap opens it back up
  var held = false, leaveT, wasFolded = false;
  function sync() {
    var fold = scrollY > 160 && !held && !nav.classList.contains('open');
    if (fold && !nav.classList.contains('collapsed')) closeMenus();
    nav.classList.toggle('collapsed', fold);
    nav.classList.toggle('scrolled', scrollY > 30);
    brand.setAttribute('aria-label', fold ? 'Open menu' : 'Baptist Temple home');
  }
  addEventListener('scroll', function () { if (!fine) held = false; sync(); }, { passive: true });
  nav.addEventListener('mouseenter', function () { if (!fine) return; clearTimeout(leaveT); held = true; sync(); });
  nav.addEventListener('mouseleave', function () { if (!fine) return; leaveT = setTimeout(function () { held = false; sync(); }, 350); });
  nav.addEventListener('focusin', function () { held = true; sync(); });
  nav.addEventListener('focusout', function (e) { if (!nav.contains(e.relatedTarget)) { held = false; sync(); } });
  brand.addEventListener('pointerdown', function () { wasFolded = nav.classList.contains('collapsed'); });
  brand.addEventListener('click', function (e) {
    if (wasFolded || nav.classList.contains('collapsed')) { e.preventDefault(); wasFolded = false; held = true; sync(); }
  });
  sync();

  // ---- current page in menus
  var here = location.pathname.replace(/index\.html$/, '');
  nav.querySelectorAll('a[href]').forEach(function (a) { if (a.getAttribute('href') === here && here !== '/') a.setAttribute('aria-current', 'page'); });

  // ---- reveal on scroll (reveal, tiles, timeline)
  var targets = document.querySelectorAll('.reveal, .tile, .timeline');
  if ('IntersectionObserver' in window && !still) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -10% 0px' });
    document.querySelectorAll('.stagger').forEach(function (p) {
      [].forEach.call(p.children, function (c, i) { c.style.transitionDelay = (i * 90) + 'ms'; });
    });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('in'); });
  }

  // ---- rotating word in the hero
  var rot = document.querySelector('.rotator');
  if (rot && !still) {
    var words = rot.querySelectorAll('span'), i = 0;
    setInterval(function () {
      var cur = words[i]; i = (i + 1) % words.length; var nxt = words[i];
      cur.classList.remove('on'); cur.classList.add('out');
      nxt.classList.remove('out'); nxt.classList.add('on');
      setTimeout(function () { cur.classList.remove('out'); }, 700);
    }, 2600);
  }

  // ---- statement: light words up as the section scrolls past
  var st = document.querySelector('.statement');
  var ticking = false;
  if (st) {
    st.querySelectorAll('[data-words]').forEach(function (el) {
      el.innerHTML = el.textContent.split(/(\s+)/).map(function (w) { return /\s+/.test(w) ? w : '<span class="w">' + w + '</span>'; }).join('');
    });
    var ws = st.querySelectorAll('.w');
    if (still) ws.forEach(function (w) { w.classList.add('lit'); });
  }

  // ---- parallax backgrounds
  var par = document.querySelectorAll('[data-parallax]');

  function onScroll() {
    ticking = false;
    var vh = innerHeight;
    if (st && !still) {
      var r = st.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      var n = Math.round(p * ws.length);
      ws.forEach(function (w, k) { w.classList.toggle('lit', k < n); });
    }
    if (!still) par.forEach(function (el) {
      var box = el.parentElement.getBoundingClientRect();
      if (box.bottom < 0 || box.top > vh) return;
      var c = (box.top + box.height / 2 - vh / 2) / vh;
      el.style.transform = 'translate3d(0,' + (c * -60).toFixed(1) + 'px,0)';
    });
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // ---- preview-only forms
  document.querySelectorAll('form[data-preview]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var m = f.querySelector('.form-msg');
      m.hidden = false;
      m.textContent = 'Thanks! This is a preview, so nothing was sent. On the live site, this goes straight to the church office.';
      m.focus();
    });
  });

  var y = document.getElementById('yr'); if (y) y.textContent = new Date().getFullYear();
})();
