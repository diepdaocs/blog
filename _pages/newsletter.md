---
layout: single
title: "Newsletter"
permalink: /newsletter/
---

{% assign _mc_u  = site.newsletter.mailchimp_action | split: "u="  | last | split: "&" | first %}
{% assign _mc_id = site.newsletter.mailchimp_action | split: "id=" | last | split: "&" | first %}

<div class="newsletter-page">

  <section class="newsletter-page__section">
    <h2 class="newsletter-page__section-title">Subscribe</h2>
    <p class="newsletter-page__desc">
      Get new posts delivered straight to your inbox. No spam &mdash; unsubscribe anytime.
    </p>

    <form class="newsletter-page__form"
          action="https://diepdao.us11.list-manage.com/subscribe/post"
          method="POST"
          target="_blank"
          rel="noopener noreferrer">
      <input type="hidden" name="u"  value="{{ _mc_u }}">
      <input type="hidden" name="id" value="{{ _mc_id }}">
      <div style="position:absolute;left:-5000px" aria-hidden="true">
        <input type="text" name="b_{{ _mc_u }}_{{ _mc_id }}" tabindex="-1" value="">
      </div>
      <div class="newsletter-page__row">
        <input
          type="email"
          name="MERGE0"
          class="newsletter-page__input"
          placeholder="your@email.com"
          required
          aria-label="Email address"
        />
        <button type="submit" class="newsletter-page__btn">Subscribe</button>
      </div>
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

    <form class="newsletter-page__form"
          action="https://diepdao.us11.list-manage.com/unsubscribe/post"
          method="POST"
          target="_blank"
          rel="noopener noreferrer">
      <input type="hidden" name="u"  value="{{ _mc_u }}">
      <input type="hidden" name="id" value="{{ _mc_id }}">
      <div style="position:absolute;left:-5000px" aria-hidden="true">
        <input type="text" name="b_{{ _mc_u }}_{{ _mc_id }}" tabindex="-1" value="">
      </div>
      <div class="newsletter-page__row">
        <input
          type="email"
          name="email"
          class="newsletter-page__input"
          placeholder="your@email.com"
          required
          aria-label="Email address to unsubscribe"
        />
        <button type="submit" class="newsletter-page__btn newsletter-page__btn--unsub">Unsubscribe</button>
      </div>
    </form>
  </section>

</div>
