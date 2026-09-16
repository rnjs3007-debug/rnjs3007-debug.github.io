---
layout: default
title: About Me
permalink: /about/
---
<div style="max-width:860px;margin:0 auto;padding:48px 32px 32px;font-family:'Noto Sans KR',sans-serif;">

  <div style="margin-bottom:40px;">
    <a href="/" style="font-size:13px;color:#aaa;text-decoration:none;">← 홈으로</a>
    <h1 style="font-size:26px;font-weight:700;letter-spacing:-0.5px;margin:12px 0 8px;color:#37352f;">권아름</h1>
    <p style="font-size:14px;color:#aaa;line-height:1.7;">AI 개발을 공부하고 있습니다.<br>데이터 수집부터 모델 검증까지, 직접 부딪히며 배운 과정을 기록합니다.</p>
  </div>

  <hr style="height:0.5px;background:#e0e0e0;border:none;margin-bottom:32px;">

  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">현재</p>
  <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:48px;">
    <div style="border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;font-size:14px;color:#37352f;">한국폴리텍대학 진주캠퍼스 AI소프트웨어과</div>
    <div style="border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;font-size:14px;color:#37352f;">한이음 드림업 BikeEyes 프로젝트 AI 담당</div>
    <div style="border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;font-size:14px;color:#37352f;">2026 데이터+AI 혁신 챌린지(DCC) 팀장</div>
    <div style="border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;font-size:14px;color:#37352f;">사천시 사이클 연맹 사무차장</div>
  </div>

  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">다루는 것</p>
  <table style="width:100%;border-collapse:collapse;margin-bottom:48px;font-size:14px;">
    <thead>
      <tr>
        <th style="text-align:left;padding:10px 14px;border:1px solid #e0e0e0;background:#f8f8f6;font-weight:500;">분야</th>
        <th style="text-align:left;padding:10px 14px;border:1px solid #e0e0e0;background:#f8f8f6;font-weight:500;">내용</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">컴퓨터비전</td>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">YOLOv8 객체탐지 / Segmentation, 데이터셋 구축 및 라벨 검수</td>
      </tr>
      <tr>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">자연어처리</td>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">KLUE-BERT 다중 레이블 분류</td>
      </tr>
      <tr>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">언어</td>
        <td style="padding:10px 14px;border:1px solid #e0e0e0;">Python, C</td>
      </tr>
    </tbody>
  </table>

  {% assign p1 = site.categories.projects | where: "title", "[BikeEyes] pothole mAP 붕괴 원인 추적" | first %}
  {% assign p2 = site.categories.projects | where: "title", "[BikeEyes] 균열 Segmentation 전환과 데이터셋 재구축" | first %}
  {% assign p3 = site.categories.projects | where: "title", "[BikeEyes] 데이터셋 정제와 검수" | first %}
  {% assign p4 = site.categories.projects | where: "title", "[BikeEyes] 요구사항에서 DB까지" | first %}
  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">대표 기록</p>
  <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:48px;">
    <a href="{{ p1.url }}" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;display:block;">
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">pothole mAP 붕괴 원인 추적</div>
      <div style="font-size:12px;color:#aaa;">라벨 오염을 찾아낸 과정</div>
    </a>
    <a href="{{ p2.url }}" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;display:block;">
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">균열 Segmentation 전환</div>
      <div style="font-size:12px;color:#aaa;">BBOX의 한계와 문제 재정의</div>
    </a>
    <a href="{{ p3.url }}" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;display:block;">
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">데이터셋 정제와 검수</div>
      <div style="font-size:12px;color:#aaa;">중복 제거부터 negative 설계까지</div>
    </a>
    <a href="{{ p4.url }}" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;display:block;">
      <div style="font-size:14px;font-weight:500;color:#37352f;margin-bottom:4px;">요구사항에서 DB까지</div>
      <div style="font-size:12px;color:#aaa;">설계 문서를 연결한 방법</div>
    </a>
  </div>

  <p style="font-size:12px;color:#aaa;letter-spacing:0.8px;text-transform:uppercase;margin-bottom:16px;">링크</p>
  <div style="display:flex;flex-direction:column;gap:12px;">
    <a href="https://github.com/rnjs3007-debug" style="text-decoration:none;border:0.5px solid #e0e0e0;border-radius:12px;padding:16px 20px;display:block;font-size:14px;color:#37352f;">GitHub: github.com/rnjs3007-debug</a>
  </div>

</div>
