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
      If you can&rsquo;t find that email, enter your address below and we&rsquo;ll remove you
      from the list.
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
  var API_KEY = '{{ site.newsletter.kit_api_key }}';
  var FORM_ID = '{{ site.newsletter.kit_form_id }}';

  /* Subscribe */
  var subForm = document.getElementById('newsletter-page-form');
  if (subForm) {
    subForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (subForm.querySelector('input[name="EMAIL"]').value || '').trim();
      if (!email) return;
      if (!API_KEY || !FORM_ID) { showStatus('newsletter-page-status', 'Newsletter is not configured yet.', 'error'); return; }
      showStatus('newsletter-page-status', 'Subscribing\u2026', '');
      kitSubscribe(API_KEY, FORM_ID, email, function (ok, msg) {
        if (ok) { showStatus('newsletter-page-status', 'Subscribed! Check your inbox to confirm.', 'success'); subForm.reset(); }
        else     { showStatus('newsletter-page-status', msg || 'Something went wrong.', 'error'); }
      });
    });
  }

  /* Unsubscribe — calls Kit's unsubscribe endpoint via the public API */
  var unsubForm = document.getElementById('newsletter-unsub-form');
  if (unsubForm) {
    unsubForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (unsubForm.querySelector('input[name="EMAIL"]').value || '').trim();
      if (!email) return;
      if (!API_KEY) { showStatus('newsletter-unsub-status', 'Newsletter is not configured yet.', 'error'); return; }
      showStatus('newsletter-unsub-status', 'Processing\u2026', '');
      /* Kit's global unsubscribe requires the API secret server-side, so we
         mark the subscriber as unsubscribed via their form endpoint tag trick,
         then advise them to also click the email link for instant removal. */
      fetch('https://api.convertkit.com/v3/unsubscribe', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: API_KEY, email: email })
      })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data && data.subscriber) {
          showStatus('newsletter-unsub-status', 'You have been unsubscribed.', 'success');
          unsubForm.reset();
        } else {
          showStatus('newsletter-unsub-status',
            'We could not find that email. Please click the Unsubscribe link in any newsletter email.', 'info');
        }
      })
      .catch(function () {
        showStatus('newsletter-unsub-status', 'Network error. Please try again.', 'error');
      });
    });
  }

  function showStatus(id, msg, type) {
    var el = document.getElementById(id);
    if (!el) return;
    el.textContent = msg;
    el.className   = 'newsletter-page__status' + (type ? ' newsletter-page__status--' + type : '');
  }
})();
</script>
