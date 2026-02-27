(function () {
  var STORAGE_KEY = 'blog-theme';

  function getTheme() {
    return localStorage.getItem(STORAGE_KEY) || 'system';
  }

  function applyTheme(theme) {
    var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    if (theme === 'dark' || (theme === 'system' && prefersDark)) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }

  function setTheme(theme) {
    localStorage.setItem(STORAGE_KEY, theme);
    applyTheme(theme);
    updateButtons(theme);
  }

  function updateButtons(theme) {
    document.querySelectorAll('.theme-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.mode === theme);
    });
  }

  function createSwitcher() {
    var switcher = document.createElement('div');
    switcher.id = 'theme-switcher';
    switcher.innerHTML =
      '<button class="theme-btn" data-mode="light"  title="Light mode"><i class="fas fa-sun"></i></button>' +
      '<button class="theme-btn" data-mode="dark"   title="Dark mode"><i class="fas fa-moon"></i></button>' +
      '<button class="theme-btn" data-mode="system" title="System default"><i class="fas fa-adjust"></i></button>';

    // Inject into the dedicated slot in the top-right
    var slot = document.getElementById('theme-switcher-slot');
    if (slot) {
      slot.appendChild(switcher);
    } else {
      document.body.appendChild(switcher);
    }

    switcher.querySelectorAll('.theme-btn').forEach(function (btn) {
      btn.addEventListener('click', function () { setTheme(btn.dataset.mode); });
    });

    updateButtons(getTheme());
  }

  applyTheme(getTheme());

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createSwitcher);
  } else {
    createSwitcher();
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if (getTheme() === 'system') applyTheme('system');
  });
})();
