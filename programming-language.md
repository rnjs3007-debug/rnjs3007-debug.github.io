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
  {% for post in site.posts %}
    <article style="margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 15px;">
      <span style="color: #666; font-size: 0.9rem;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      <h2 style="margin: 5px 0;">
        <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #007bff;">
          [{{ post.categories | first | upcase }}] {{ post.title }}
        </a>
      </h2>
    </article>
  {% else %}
    <p>아직 등록된 포스팅이 없습니다. <code>_posts</code> 폴더에 파일을 추가해 보세요!</p>
  {% endfor %}
</div>

