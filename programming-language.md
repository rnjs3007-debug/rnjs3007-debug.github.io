---
layout: default
title: Programming language
permalink: /programming-language/
---

# Programming Language 공부 기록

이 페이지는 `programming-language` 카테고리로 분류된 모든 학습 기록을 보여주는 게시판입니다.

<div class="post-container">
  {% for post in site.categories.programming-language %}
    <article style="margin-bottom: 40px; border-bottom: 1px solid #eee; padding-bottom: 20px;">
      <header>
        <span style="color: #666; font-size: 0.9rem;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
        <h2 style="margin: 10px 0;">
          <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #007bff; font-size: 1.5rem;">
            {{ post.title }}
          </a>
        </h2>
      </header>
      
      <div style="color: #444; line-height: 1.6;">
        {{ post.excerpt | strip_html | truncate: 160 }}
      </div>
      
      <a href="{{ post.url | relative_url }}" style="display: inline-block; margin-top: 10px; color: #007bff; font-weight: bold; text-decoration: none;">
        더 읽어보기 →
      </a>
    </article>
  {% else %}
    <p style="padding: 20px; background: #f9f9f9; border-radius: 8px;">
      아직 등록된 포스트가 없습니다. <code>_posts</code> 폴더에 카테고리를 <code>programming-language</code>로 설정한 글을 작성해 보세요!
    </p>
  {% endfor %}
</div>

<style>
  .post-container {
    max-width: 800px;
    margin: 30px auto;
  }
</article:hover h2 a {
    color: #0056b3 !important;
    text-decoration: underline !important;
  }
</style>
