(function () {
  var STORAGE_KEY = 'blog-theme';
  var _giscusObserver = null;

  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function getCurrentTheme() {
    return localStorage.getItem(STORAGE_KEY) || getSystemTheme();
  }

  function sendGiscusTheme(theme) {
    var giscusFrame = document.querySelector('iframe.giscus-frame');
    if (!giscusFrame) return false;
    giscusFrame.contentWindow.postMessage(
      { giscus: { setConfig: { theme: theme === 'dark' ? 'dark' : 'light' } } },
      'https://giscus.app'
    );
    return true;
  }

  function watchForGiscus(theme) {
    if (_giscusObserver) {
      _giscusObserver.disconnect();
    }
    _giscusObserver = new MutationObserver(function () {
      if (sendGiscusTheme(theme)) {
        _giscusObserver.disconnect();
        _giscusObserver = null;
      }
    });
    _giscusObserver.observe(document.body, { childList: true, subtree: true });
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    // Sync Giscus comment widget theme; watch for it if not yet in DOM
    if (!sendGiscusTheme(theme)) {
      watchForGiscus(theme);
    }
  }

  function updateButton(theme) {
    var btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;
    if (theme === 'dark') {
      btn.innerHTML = '<i class="fas fa-sun"></i>';
      btn.title = 'Switch to light mode';
    } else {
      btn.innerHTML = '<i class="fas fa-moon"></i>';
      btn.title = 'Switch to dark mode';
    }
  }

  function toggle() {
    var next = getCurrentTheme() === 'dark' ? 'light' : 'dark';
    localStorage.setItem(STORAGE_KEY, next);
    applyTheme(next);
    updateButton(next);
  }

  function createSwitcher() {
    var btn = document.createElement('button');
    btn.id = 'theme-toggle-btn';
    btn.className = 'theme-toggle-btn';
    btn.addEventListener('click', toggle);

    var slot = document.getElementById('theme-switcher-slot');
    if (slot) slot.appendChild(btn);
    else document.body.appendChild(btn);

    updateButton(getCurrentTheme());
  }

  applyTheme(getCurrentTheme());

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createSwitcher);
  } else {
    createSwitcher();
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if (!localStorage.getItem(STORAGE_KEY)) {
      var t = getSystemTheme();
      applyTheme(t);
      updateButton(t);
    }
  });
})();
