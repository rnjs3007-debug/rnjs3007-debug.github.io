---
layout: default
title: Others
permalink: /programming-language/others/
---

# 📁 Programming Language > 기타 언어 학습 기록

이 페이지는 그 외 다양한 언어들의 공부 기록을 모아놓은 게시판입니다.

<div class="post-container">
  {% for post in site.categories.others %}
    <article style="margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px;">
      <span style="color: #666;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      <h2 style="margin: 10px 0;">
        <a href="{{ post.url | relative_url }}" style="color: #007bff; text-decoration: none;">{{ post.title }}</a>
      </h2>
    </article>
  {% endfor %}
</div>

<hr>
<a href="{{ '/programming-language/' | relative_url }}">← 전체 언어 목록으로 돌아가기</a>
