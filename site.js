// Baptist Temple · menus, reveal-on-scroll, preview-only forms
(function () {
  var head = document.querySelector('.site-head');
  var burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', function () {
    var open = head.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });

  document.querySelectorAll('.nav-group > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var g = btn.parentElement, open = !g.classList.contains('open');
      document.querySelectorAll('.nav-group.open').forEach(function (x) { x.classList.remove('open'); x.querySelector('button').setAttribute('aria-expanded', 'false'); });
      g.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
      g.querySelector('.menu').hidden = !open;
    });
  });
  document.addEventListener('click', function (e) {
    if (e.target.closest('.nav-group')) return;
    document.querySelectorAll('.nav-group.open').forEach(function (g) {
      g.classList.remove('open'); g.querySelector('button').setAttribute('aria-expanded', 'false'); g.querySelector('.menu').hidden = true;
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.nav-group.open > button').forEach(function (b) { b.click(); b.focus(); });
    if (head.classList.contains('open')) { head.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
  });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  // This is a concept preview: forms show a note instead of sending anything.
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
