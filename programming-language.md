---
layout: default
title: Programming Language
permalink: /programming-language/
---
<div style="max-width:860px;margin:0 auto;padding:48px 32px 32px;font-family:'Noto Sans KR',sans-serif;">
  <div style="margin-bottom:40px;">
    <a href="/" style="font-size:13px;color:#aaa;text-decoration:none;">← 홈으로</a>
    <h1 style="font-size:26px;font-weight:700;margin:12px 0 8px;color:#37352f;">💻 Programming Language</h1>
    <p style="font-size:14px;color:#aaa;">언어별 학습내용 기록</p>
  </div>
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">언어별 카테고리</p>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:48px;">
    <a href="/programming-language/python/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#EAF3DE;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">🐍</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">Python</div>
      <div style="font-size:12px;color:#aaa;">파이썬 기초 · 라이브러리</div>
    </a>
    <a href="/programming-language/html-css/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#FAEEDA;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">🌐</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">HTML & CSS</div>
      <div style="font-size:12px;color:#aaa;">웹 기초 · 스타일링</div>
    </a>
    <a href="/programming-language/c-language/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#E6F1FB;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">💻</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">C Language</div>
      <div style="font-size:12px;color:#aaa;">C언어 기초 · 포인터</div>
    </a>
    <a href="/programming-language/java/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#FAECE7;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">☕</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">Java</div>
      <div style="font-size:12px;color:#aaa;">자바 기초 · 객체지향</div>
    </a>
    <a href="/programming-language/others/" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:20px;display:block;">
      <div style="width:36px;height:36px;border-radius:8px;background:#F1EFE8;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;">📁</div>
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">기타 언어</div>
      <div style="font-size:12px;color:#aaa;">기타 학습 기록</div>
    </a>
  </div>
  <hr style="height:0.5px;background:#e0e0e0;border:none;margin-bottom:32px;">
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">전체 글 목록</p>
  {% for post in site.posts %}
  <div style="display:flex;align-items:baseline;justify-content:space-between;padding:12px 0;border-bottom:0.5px solid #e0e0e0;">
    <div style="display:flex;align-items:baseline;gap:10px;">
      <span style="font-size:11px;padding:2px 8px;border-radius:4px;font-weight:500;{% if post.categories contains 'python' %}background:#EAF3DE;color:#3B6D11;{% elsif post.categories contains 'c-language' %}background:#E6F1FB;color:#185FA5;{% elsif post.categories contains 'html-css' %}background:#FAEEDA;color:#854F0B;{% elsif post.categories contains 'java' %}background:#FAECE7;color:#993C1D;{% elsif post.categories contains 'ai-study' %}background:#EEEDFE;color:#3C3489;{% else %}background:#F1EFE8;color:#5F5E5A;{% endif %}">{{ post.categories | first }}</span>
      <a href="{{ post.url }}" style="font-size:14px;color:#37352f;">{{ post.title }}</a>
    </div>
    <span style="font-size:12px;color:#aaa;margin-left:16px;">{{ post.date | date: "%Y-%m-%d" }}</span>
  </div>
  {% endfor %}
</div>
