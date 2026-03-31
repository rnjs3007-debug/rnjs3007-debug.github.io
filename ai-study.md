---
layout: default
title: AI Study
permalink: /ai-study/
---
<div style="max-width:860px;margin:0 auto;padding:48px 32px 32px;font-family:'Noto Sans KR',sans-serif;">
  <div style="margin-bottom:40px;">
    <a href="/" style="font-size:13px;color:#aaa;text-decoration:none;">← 홈으로</a>
    <h1 style="font-size:26px;font-weight:700;margin:12px 0 8px;color:#37352f;">🤖 AI Study</h1>
    <p style="font-size:14px;color:#aaa;">머신러닝, 딥러닝 학습 기록</p>
  </div>
  <hr style="height:0.5px;background:#e0e0e0;border:none;margin-bottom:32px;">
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">글 목록</p>
  {% assign cat_posts = site.posts | where_exp: "post", "post.categories contains 'ai-study'" %}
  {% if cat_posts.size > 0 %}
    {% for post in cat_posts %}
    <div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0;border-bottom:0.5px solid #e0e0e0;">
      <a href="{{ post.url }}" style="font-size:14px;color:#37352f;">{{ post.title }}</a>
      <span style="font-size:12px;color:#aaa;margin-left:16px;">{{ post.date | date: "%Y-%m-%d" }}</span>
    </div>
    {% endfor %}
  {% else %}
  <p style="font-size:14px;color:#aaa;">아직 작성된 글이 없습니다.</p>
  {% endif %}
</div>
