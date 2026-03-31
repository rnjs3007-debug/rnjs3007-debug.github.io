---
layout: default
title: Home
permalink: /
---
<div style="max-width:860px;margin:0 auto;padding:48px 32px 32px;font-family:'Noto Sans KR',sans-serif;">
  <div style="margin-bottom:40px;">
    <h1 style="font-size:26px;font-weight:700;letter-spacing:-0.5px;margin-bottom:8px;color:#37352f;">A-reum Blog</h1>
    <p style="font-size:14px;color:#aaa;line-height:1.7;">안녕하세요. 초보 개발자의 프로그래밍언어를 공부하고, 기록하는 공간입니다.</p>
  </div>
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">카테고리</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:48px;">
    <a href="/programming-language/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#E1F5EE;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">💻</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">Programming Language</div>
      <div style="font-size:12px;color:#aaa;">Python, C, Java, HTML 학습 기록</div>
    </a>
    <a href="/ai-study/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#EEEDFE;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">🤖</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">AI Study</div>
      <div style="font-size:12px;color:#aaa;">머신러닝, 딥러닝 학습 기록</div>
    </a>
    <a href="/data-analysis/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#FAEEDA;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">📊</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">Data Analysis</div>
      <div style="font-size:12px;color:#aaa;">데이터 분석 학습 기록</div>
    </a>
    <a href="/projects/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#FAECE7;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">🚀</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">Projects</div>
      <div style="font-size:12px;color:#aaa;">개인 프로젝트 기록</div>
    </a>
    <a href="/about/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#F1EFE8;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">👤</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">About Me</div>
      <div style="font-size:12px;color:#aaa;">소개 및 개발 일지</div>
    </a>
  </div>
  <hr style="height:0.5px;background:#e0e0e0;border:none;margin-bottom:32px;">
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">최근 글</p>
  {% for post in site.posts limit:10 %}
  <div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0;border-bottom:0.5px solid #e0e0e0;">
    <div style="display:flex;align-items:baseline;gap:10px;">
      <span style="font-size:11px;padding:2px 8px;border-radius:4px;font-weight:500;{% if post.categories contains 'python' %}background:#EAF3DE;color:#3B6D11;{% elsif post.categories contains 'c-language' %}background:#E6F1FB;color:#185FA5;{% elsif post.categories contains 'html-css' %}background:#FAEEDA;color:#854F0B;{% elsif post.categories contains 'java' %}background:#FAECE7;color:#993C1D;{% elsif post.categories contains 'ai-study' %}background:#EEEDFE;color:#3C3489;{% else %}background:#F1EFE8;color:#5F5E5A;{% endif %}">{{ post.categories | first }}</span>
      <a href="{{ post.url }}" style="font-size:14px;color:#37352f;">{{ post.title }}</a>
    </div>
    <span style="font-size:12px;color:#aaa;margin-left:16px;">{{ post.date | date: "%Y-%m-%d" }}</span>
  </div>
  {% endfor %}
</div>
