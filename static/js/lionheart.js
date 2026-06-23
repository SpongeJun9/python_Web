document.addEventListener('DOMContentLoaded', function () {
  var splash = document.getElementById('siteSplash');
  if (splash) {
    var splashTimer;
    var hideSplash = function () {
      splash.classList.add('is-hidden');
      try {
        window.sessionStorage.setItem('lionheartSplashEntered', '1');
      } catch (e) {}
      window.clearTimeout(splashTimer);
      window.setTimeout(function () {
        splash.style.display = 'none';
      }, 520);
    };

    try {
      if (window.sessionStorage.getItem('lionheartSplashEntered') === '1') {
        splash.style.display = 'none';
      } else {
        splashTimer = window.setTimeout(hideSplash, 1600);
      }
    } catch (e) {
      splashTimer = window.setTimeout(hideSplash, 1600);
    }

    splash.addEventListener('click', hideSplash);
    splash.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        hideSplash();
      }
    });
  }

  var header = document.querySelector('.topbar');
  var updateHeader = function () {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 20);
  };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
      });
    });
  }

  function setupCarousel(root, config) {
    if (!root) return;
    var items = root.querySelectorAll(config.itemSelector);
    if (!items.length) return;

    // 按钮可能在 root 内部，也可能在 root 的父级中
    var buttonScope = config.buttonScope || root;
    var indicatorRoot = config.indicatorRoot || root;
    var indicators = indicatorRoot.querySelectorAll(config.indicatorSelector);
    var prevBtn = buttonScope.querySelector(config.prevSelector || '.carousel-prev');
    var nextBtn = buttonScope.querySelector(config.nextSelector || '.carousel-next');
    var autoplay = Number(root.getAttribute('data-autoplay') || config.autoplay || 0);
    var current = 0;
    var timer;

    function show(index) {
      if (!items.length) return;
      current = (index + items.length) % items.length;
      items.forEach(function (item, i) {
        var active = i === current;
        item.classList.toggle('active', active);
        item.style.opacity = active ? '1' : '0';
        item.style.zIndex = active ? '2' : '1';
      });
      indicators.forEach(function (dot, i) {
        var active = i === current;
        dot.classList.toggle('active', active);
        dot.style.opacity = active ? '1' : '0.55';
      });
    }

    function next() { show(current + 1); }
    function prev() { show(current - 1); }
    function stop() { if (timer) window.clearInterval(timer); }
    function start() {
      stop();
      if (autoplay && items.length > 1) timer = window.setInterval(next, autoplay);
    }

    if (items.length <= 1) {
      if (prevBtn) prevBtn.style.display = 'none';
      if (nextBtn) nextBtn.style.display = 'none';
      indicators.forEach(function (dot) { dot.style.display = 'none'; });
      show(0);
      return;
    }

    if (nextBtn) nextBtn.addEventListener('click', function () { stop(); next(); start(); });
    if (prevBtn) prevBtn.addEventListener('click', function () { stop(); prev(); start(); });
    indicators.forEach(function (dot, index) {
      dot.addEventListener('click', function () { stop(); show(index); start(); });
    });
    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);
    show(0);
    start();
  }

  document.querySelectorAll('.hero-bg-carousel').forEach(function (carousel) {
    setupCarousel(carousel, {
      itemSelector: '.hero-carousel-item',
      indicatorSelector: '.hero-indicator',
      indicatorRoot: document.querySelector('.hero'),
      buttonScope: document.querySelector('.hero'),
      prevSelector: '.hero-carousel-prev',
      nextSelector: '.hero-carousel-next',
      autoplay: 6500
    });
  });

  document.querySelectorAll('.about-carousel').forEach(function (carousel) {
    setupCarousel(carousel, {
      itemSelector: '.about-carousel-item',
      indicatorSelector: '.about-indicator',
      prevSelector: '.about-carousel-prev',
      nextSelector: '.about-carousel-next',
      autoplay: 5200
    });
  });

  document.querySelectorAll('.team-carousel').forEach(function (carousel) {
    setupCarousel(carousel, {
      itemSelector: '.carousel-item',
      indicatorSelector: '.indicator',
      prevSelector: '.carousel-prev',
      nextSelector: '.carousel-next',
      autoplay: 5200
    });
  });

  var revealItems = document.querySelectorAll('.reveal, .tech-card, .project-card, .news-list a, .timeline-item, .data-panel, .mini-card');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach(function (item) {
      item.classList.add('reveal');
      observer.observe(item);
    });
  } else {
    revealItems.forEach(function (item) {
      item.classList.add('is-visible');
    });
  }
});
