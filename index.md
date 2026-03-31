---
layout: default
title: Home
---

<div class="home-hero">
  <h1>A-reum Blog ✦</h1>
  <p>초보 개발자의 프로그래밍 언어 공부 & 기록 공간입니다.</p>
</div>

<p class="section-title">카테고리</p>

<div class="category-grid">
  <a class="category-card" href="/programming-language/">
    <div class="card-icon">💻</div>
    <div class="card-title">프로그래밍 언어</div>
    <div class="card-desc">C언어 · Java · HTML/CSS</div>
  </a>
  <a class="category-card" href="/ai-study/">
    <div class="card-icon">🤖</div>
    <div class="card-title">AI Study</div>
    <div class="card-desc">머신러닝 · 딥러닝 · LLM</div>
  </a>
  <a class="category-card" href="/data-analysis/">
    <div class="card-icon">📊</div>
    <div class="card-title">데이터 분석</div>
    <div class="card-desc">Pandas · 시각화 · 통계</div>
  </a>
  <a class="category-card" href="/python/">
    <div class="card-icon">🐍</div>
    <div class="card-title">Python</div>
    <div class="card-desc">파이썬 기초 · 라이브러리</div>
  </a>
  <a class="category-card" href="/projects/">
    <div class="card-icon">🛠</div>
    <div class="card-title">프로젝트</div>
    <div class="card-desc">개인 프로젝트 · 토이</div>
  </a>
  <a class="category-card" href="/about/">
    <div class="card-icon">🙋</div>
    <div class="card-title">About Me</div>
    <div class="card-desc">나에 대한 이야기</div>
  </a>
</div>

<p class="section-title">최근 글</p>

<ul class="post-list">
  {% assign recent_posts = site.posts | limit: 10 %}
  {% for post in recent_posts %}
  <li class="post-list-item">
    {% assign cat = post.categories[0] %}
    {% if cat %}<span class="tag tag-{{ cat }}">{{ cat }}</span>{% endif %}
    <a class="post-title-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time class="post-date">{{ post.date | date: "%Y. %m. %d" }}</time>
  </li>
  {% endfor %}
</ul>
