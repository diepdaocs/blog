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
          id="newsletter-page-email"
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
      To stop receiving emails, click the <strong>Unsubscribe</strong> link at the bottom of any
      newsletter email you received &mdash; it is the fastest way.
    </p>
    <p class="newsletter-page__desc">
      Alternatively, enter your email below and we will send you an unsubscribe confirmation.
    </p>

    <form class="newsletter-page__form" id="newsletter-unsub-form" novalidate>
      <div class="newsletter-page__row">
        <input
          type="email"
          name="EMAIL"
          id="newsletter-unsub-email"
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
  var MAILCHIMP_URL = '{{ site.newsletter.mailchimp_action }}';

  /* --- helpers --- */
  function showStatus(id, msg, type) {
    var el = document.getElementById(id);
    if (!el) return;
    el.textContent = msg;
    el.className   = 'newsletter-page__status' + (type ? ' newsletter-page__status--' + type : '');
  }

  function mcJsonp(email, mode, statusId, form) {
    if (!MAILCHIMP_URL || MAILCHIMP_URL.indexOf('list-manage.com') === -1) {
      showStatus(statusId, 'Newsletter is not configured yet.', 'error');
      return;
    }

    showStatus(statusId, (mode === 'unsub' ? 'Processing\u2026' : 'Subscribing\u2026'), '');

    var endpoint = mode === 'unsub'
      ? MAILCHIMP_URL.replace('/subscribe/post', '/unsubscribe/post')
      : MAILCHIMP_URL;

    var jsonUrl = endpoint
      .replace('/post?', '/post-json?')
      .replace(/[?&]c=[^&]*/, '');

    var cbName = 'mc_cb_' + Date.now();
    var sep    = jsonUrl.indexOf('?') === -1 ? '?' : '&';
    var src    = jsonUrl + sep + 'EMAIL=' + encodeURIComponent(email) + '&c=' + cbName;

    window[cbName] = function (data) {
      delete window[cbName];
      var s = document.getElementById('mc_jsonp_' + cbName);
      if (s) s.parentNode.removeChild(s);

      if (data && data.result === 'success') {
        if (mode === 'unsub') {
          showStatus(statusId, 'Unsubscribed successfully.', 'success');
        } else {
          showStatus(statusId, 'Subscribed! Check your inbox to confirm.', 'success');
        }
        if (form) form.reset();
      } else {
        var msg = (data && data.msg) ? data.msg : 'Something went wrong.';
        if (msg.indexOf('already subscribed') > -1) {
          showStatus(statusId, 'You\'re already subscribed!', 'info');
        } else if (msg.indexOf('not subscribed') > -1) {
          showStatus(statusId, 'That email is not on the list.', 'info');
        } else {
          showStatus(statusId, msg.split(' - ').pop().replace(/<[^>]+>/g, ''), 'error');
        }
      }
    };

    var script = document.createElement('script');
    script.id  = 'mc_jsonp_' + cbName;
    script.src = src;
    document.body.appendChild(script);
  }

  /* --- subscribe form --- */
  var subForm = document.getElementById('newsletter-page-form');
  if (subForm) {
    subForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (subForm.querySelector('input[name="EMAIL"]').value || '').trim();
      if (!email) return;
      mcJsonp(email, 'sub', 'newsletter-page-status', subForm);
    });
  }

  /* --- unsubscribe form --- */
  var unsubForm = document.getElementById('newsletter-unsub-form');
  if (unsubForm) {
    unsubForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (unsubForm.querySelector('input[name="EMAIL"]').value || '').trim();
      if (!email) return;
      mcJsonp(email, 'unsub', 'newsletter-unsub-status', unsubForm);
    });
  }
})();
</script>
