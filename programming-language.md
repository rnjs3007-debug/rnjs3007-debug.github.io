---
layout: default
title: Programming Language
permalink: /programming-language/
---

# 📚 Programming Language 

언어별 학습내용 기록

### 🔍 언어별 세부 카테고리
* [🐍 **Python** 공부 기록 보러가기]({{ '/programming-language/python/' | relative_url }})
* [🌐 **HTML & CSS** 공부 기록 보러가기]({{ '/programming-language/html-css/' | relative_url }})
* [💻 **C Language** 공부 기록 보러가기]({{ '/programming-language/c-language/' | relative_url }})
* [☕ **Java** 공부 기록 보러가기]({{ '/programming-language/java/' | relative_url }})
* [📁 **기타 언어** 공부 기록 보러가기]({{ '/programming-language/others/' | relative_url }})

---

### 📝 전체 최근 글 목록 (최신순)
이 아래에는 언어별로 기록한 글이 통합되어 표현

<div class="post-container">
  {% for post in site.categories.programming-language %}
    <article style="margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px;">
      <span style="color: #666; font-size: 0.9rem;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      <h2 style="margin: 5px 0;">
        <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #007bff;">{{ post.title }}</a>
      </h2>
    </article>
  {% endfor %}
</div>

<style>
  .post-container {
    max-width: 800px;
    margin: 20px 0;
  }
  h3 {
    margin-top: 30px;
    color: #333;
  }
  ul {
    list-style: none;
    padding-left: 0;
  }
  li {
    margin-bottom: 10px;
    font-size: 1.1rem;
  }
</style>
