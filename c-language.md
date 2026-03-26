---
layout: default
title: C-Language
permalink: /programming-language/c-language/
---

# 💻 Programming Language > C언어 학습 기록

이 페이지는 **C언어** 관련 공부 내용만 모아놓은 게시판입니다.

<div class="post-container">
  {% for post in site.categories.c-language %}
    <article style="margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px;">
      <span style="color: #666;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      <h2 style="margin: 10px 0;">
        <a href="{{ post.url | relative_url }}" style="color: #007bff; text-decoration: none;">{{ post.title }}</a>
      </h2>
    </article>
  {% else %}
    <p>아직 등록된 C언어 관련 글이 없습니다.</p>
  {% endfor %}
</div>

<hr>
<a href="{{ '/programming-language/' | relative_url }}">← 전체 언어 목록으로 돌아가기</a>
