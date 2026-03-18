---
layout: single
title: "Newsletter"
permalink: /newsletter/
---

<div class="newsletter-page">

  <section class="newsletter-page__section">
    <h2 class="newsletter-page__section-title">Subscribe</h2>
    <p class="newsletter-page__desc">
      Get new posts delivered straight to your inbox. No spam &mdash; unsubscribe anytime.
    </p>

    <form class="newsletter-page__form" id="newsletter-page-form" novalidate>
      <div class="newsletter-page__row">
        <input
          type="email"
          name="EMAIL"
          class="newsletter-page__input"
          placeholder="your@email.com"
          required
          aria-label="Email address"
        />
        <button type="submit" class="newsletter-page__btn">Subscribe</button>
      </div>
      <p class="newsletter-page__status" id="newsletter-page-status" aria-live="polite"></p>
    </form>
  </section>

  <hr class="newsletter-page__divider" id="unsubscribe" />

  <section class="newsletter-page__section">
    <h2 class="newsletter-page__section-title">Unsubscribe</h2>
    <p class="newsletter-page__desc">
      Every newsletter email includes an <strong>Unsubscribe</strong> link at the bottom &mdash;
      clicking it is the quickest way to opt out instantly.
    </p>
    <p class="newsletter-page__desc">
      Alternatively, enter your email below to be removed from the list.
    </p>

    <form class="newsletter-page__form" id="newsletter-unsub-form" novalidate>
      <div class="newsletter-page__row">
        <input
          type="email"
          name="EMAIL"
          class="newsletter-page__input"
          placeholder="your@email.com"
          required
          aria-label="Email address to unsubscribe"
        />
        <button type="submit" class="newsletter-page__btn newsletter-page__btn--unsub">Unsubscribe</button>
      </div>
      <p class="newsletter-page__status" id="newsletter-unsub-status" aria-live="polite"></p>
    </form>
  </section>

</div>

<script>
(function () {
  var MC_URL = '{{ site.newsletter.mailchimp_action }}';

  function handleForm(formId, statusId, mode) {
    var form = document.getElementById(formId);
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (form.querySelector('input[name="EMAIL"]').value || '').trim();
      if (!email) return;
      if (!MC_URL || MC_URL.indexOf('list-manage.com') === -1) {
        showStatus(statusId, 'Newsletter is not configured yet.', 'error'); return;
      }
      showStatus(statusId, (mode === 'unsub' ? 'Processing\u2026' : 'Subscribing\u2026'), '');

      var url = (mode === 'unsub')
        ? MC_URL.replace('/subscribe/post', '/unsubscribe/post')
        : MC_URL;

      mcJsonp(url, email, function (ok, msg) {
        if (ok) {
          showStatus(statusId,
            mode === 'unsub' ? 'You have been unsubscribed.' : 'Subscribed! Check your inbox to confirm.',
            'success');
          form.reset();
        } else {
          showStatus(statusId, msg || 'Something went wrong.', 'error');
        }
      });
    });
  }

  handleForm('newsletter-page-form',  'newsletter-page-status',  'sub');
  handleForm('newsletter-unsub-form', 'newsletter-unsub-status', 'unsub');

  function showStatus(id, msg, type) {
    var el = document.getElementById(id);
    if (!el) return;
    el.textContent = msg;
    el.className   = 'newsletter-page__status' + (type ? ' newsletter-page__status--' + type : '');
  }

  function mcJsonp(baseUrl, email, cb) {
    var url    = baseUrl
      .replace('/subscribe/post?',   '/subscribe/post-json?')
      .replace('/unsubscribe/post?', '/unsubscribe/post-json?')
      .replace(/[?&]c=[^&]*/g, '');
    var cbName = 'mc_cb_' + Date.now();
    var sep    = url.indexOf('?') === -1 ? '?' : '&';

    function cleanup() {
      delete window[cbName];
      var s = document.getElementById('mc_s_' + cbName);
      if (s) s.parentNode.removeChild(s);
    }

    var timer = setTimeout(function () {
      if (window[cbName]) { cleanup(); cb(false, 'Request timed out. Please try again.'); }
    }, 10000);

    window[cbName] = function (data) {
      clearTimeout(timer);
      cleanup();
      if (data && data.result === 'success') {
        cb(true);
      } else {
        var msg = (data && data.msg) ? data.msg.split(' - ').pop().replace(/<[^>]+>/g, '') : null;
        if (msg && (msg.indexOf('already subscribed') > -1)) cb(true, 'You\u2019re already subscribed!');
        else if (msg && msg.indexOf('not subscribed') > -1)  cb(false, 'That email is not on the list.');
        else cb(false, msg);
      }
    };

    var script = document.createElement('script');
    script.id  = 'mc_s_' + cbName;
    script.src = url + sep + 'EMAIL=' + encodeURIComponent(email) + '&c=' + cbName;
    document.body.appendChild(script);
  }
})();
</script>
