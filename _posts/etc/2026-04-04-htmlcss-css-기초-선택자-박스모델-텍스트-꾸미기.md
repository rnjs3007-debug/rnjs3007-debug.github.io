---
layout: post
title: "[HTML/CSS] CSS 기초 - 선택자, 박스모델, 텍스트 꾸미기"
date: 2026-04-04 23:57:24 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/HTMLCSS-CSS-%EA%B8%B0%EC%B4%88-%EC%84%A0%ED%83%9D%EC%9E%90-%EB%B0%95%EC%8A%A4%EB%AA%A8%EB%8D%B8-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EA%BE%B8%EB%AF%B8%EA%B8%B0
---

<p><strong>(260326)</strong> 오늘은 CSS의 핵심 개념들을 한꺼번에 배웠다. 스타일을 어떻게 입히는지부터, 박스모델 구조, 배경 다루기, 텍스트 꾸미기까지. 양이 많았지만 하나씩 정리해보겠다. 바로바로 복습하지 않으면 정말이지, 금방 잊어버릴것 같음에 꾸준히 연습해야 겠다. 교수님이 과제도 내주셨다!</p>
<hr />
<h2 id="1-css-스타일-선언-방법-3가지">1. CSS 스타일 선언 방법 3가지</h2>
<h3 id="가-인라인-스타일--html-태그에-직접-입히기">가. 인라인 스타일 — HTML 태그에 직접 입히기</h3>
<pre><code class="language-html">&lt;p style=&quot;color: blue;&quot;&gt;글자색을 변경해봅시다&lt;/p&gt;</code></pre>
<h3 id="나-내부-스타일-시트--style-태그-안에-작성">나. 내부 스타일 시트 — <code>&lt;style&gt;</code> 태그 안에 작성</h3>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
  &lt;style&gt;
    p {
      color: green;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;p&gt;식육목 고양이과의 포유류에 속하며, 반려묘 또는 고양이과의 총칭.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<h3 id="다-외부-스타일-시트--별도-css-파일로-연결">다. 외부 스타일 시트 — 별도 <code>.css</code> 파일로 연결</h3>
<pre><code class="language-html">&lt;link rel=&quot;stylesheet&quot; href=&quot;style.css&quot;&gt;</code></pre>
<blockquote>
<p><strong>언제 뭘 쓰나?</strong>
인라인은 테스트할 때만, 실무에서는 거의 무조건 외부 스타일 시트를 씀.</p>
</blockquote>
<hr />
<h2 id="2-css-기본-선택자">2. CSS 기본 선택자</h2>
<h3 id="1-전체-선택자--문서-전체에-적용">1) 전체 선택자 — 문서 전체에 적용</h3>
<pre><code class="language-css">* {
  margin: 0;
  padding: 0;
}</code></pre>
<h3 id="2-태그-선택자--특정-태그에-적용">2) 태그 선택자 — 특정 태그에 적용</h3>
<pre><code class="language-css">span {
  color: red;
}</code></pre>
<p><strong>HTML 주요 태그 한 번 더 정리</strong></p>
<table>
<thead>
<tr>
<th>분류</th>
<th>태그</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>구조</td>
<td><code>&lt;header&gt;</code> <code>&lt;main&gt;</code> <code>&lt;footer&gt;</code></td>
<td>상단/본문/하단 영역</td>
</tr>
<tr>
<td>텍스트</td>
<td><code>&lt;h1&gt;~&lt;h6&gt;</code> <code>&lt;p&gt;</code> <code>&lt;span&gt;</code></td>
<td>제목, 문단, 인라인 강조</td>
</tr>
<tr>
<td>목록</td>
<td><code>&lt;ul&gt;</code> <code>&lt;ol&gt;</code> <code>&lt;li&gt;</code></td>
<td>순서 없는/있는 목록</td>
</tr>
<tr>
<td>멀티미디어</td>
<td><code>&lt;img&gt;</code> <code>&lt;video&gt;</code> <code>&lt;audio&gt;</code></td>
<td>이미지, 영상, 음원</td>
</tr>
<tr>
<td>입력</td>
<td><code>&lt;input&gt;</code> <code>&lt;form&gt;</code> <code>&lt;button&gt;</code></td>
<td>입력창, 폼, 버튼</td>
</tr>
</tbody></table>
<h3 id="3-클래스-선택자--점-기호-사용">3) 클래스 선택자 — 점(.) 기호 사용</h3>
<pre><code class="language-css">/* 해당 클래스 전체 */
.클래스명 {
  color: blue;
}

/* 특정 태그의 클래스만 */
p.클래스명 {
  color: blue;
}</code></pre>
<h3 id="4-아이디-선택자--해시-기호-사용">4) 아이디 선택자 — 해시(#) 기호 사용</h3>
<pre><code class="language-css">#아이디명 {
  color: red;
}</code></pre>
<blockquote>
<p><strong>클래스 vs 아이디 차이</strong></p>
<ul>
<li>클래스(<code>.</code>) : 여러 요소에 반복 사용 가능</li>
<li>아이디(<code>#</code>) : 페이지에서 딱 하나만 사용 (고유한 값)</li>
</ul>
</blockquote>
<h3 id="5-그룹-선택자--여러-선택자를-쉼표로-묶기">5) 그룹 선택자 — 여러 선택자를 쉼표로 묶기</h3>
<pre><code class="language-css">h2, p, li {
  color: brown;
}</code></pre>
<h3 id="6-선택자-우선순위">6) 선택자 우선순위</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/35e3ce50-52e8-4f0d-a64c-8338ee8e761c/image.png" /></p>
<blockquote>
<p>우선순위 요약: 인라인 스타일 &gt; 아이디 &gt; 클래스 &gt; 태그</p>
</blockquote>
<hr />
<h2 id="3-박스-모델-이해하기">3. 박스 모델 이해하기</h2>
<h3 id="가-박스-모델-구성-요소">가. 박스 모델 구성 요소</h3>
<p>모든 HTML 요소는 박스 형태로 되어 있다.</p>
<ul>
<li><strong>content</strong> : 실제 내용이 들어가는 영역 (<code>width</code>, <code>height</code>)</li>
<li><strong>padding</strong> : 내용과 테두리 사이 안쪽 여백</li>
<li><strong>border</strong> : 테두리</li>
<li><strong>margin</strong> : 테두리 바깥 여백</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/4e4547c4-2dcf-4e76-8230-19dc4d2e489d/image.png" /></p>
<h3 id="나-경계선border-관련-속성">나. 경계선(border) 관련 속성</h3>
<pre><code class="language-css">div {
  border-top: 1px solid red;
  border-right: 5px dotted orange;
  border-bottom: 10px dashed yellow;
  border-left: 20px double green;
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/9a39caec-41ba-4dc1-816c-242f2760a120/image.png" /></p>
<p>한꺼번에 지정도 가능하다!</p>
<pre><code class="language-css">div {
  border-width: 1px 5px 10px 20px;   /* 상 우 하 좌 */
  border-style: solid dotted dashed double;
  border-color: red orange yellow green;
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/873d8378-e6ea-4849-8f55-1da15f2ac627/image.png" /></p>
<blockquote>
<p><strong>방향 순서 외우기:</strong> 시계방향 — 위 → 오른쪽 → 아래 → 왼쪽</p>
</blockquote>
<h3 id="border-radius--모서리-둥글게">border-radius — 모서리 둥글게</h3>
<pre><code class="language-css">/* 절대 단위: 좌상단부터 시계 방향으로 */
.abs { border-radius: 10px 30px 50px 100px; }

/* 50%로 설정하면 원이 됨 */
.rel { border-radius: 50%; }</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/743feef9-2e82-43ea-ad1c-63feab49b7b5/image.png" /></p>
<h3 id="다-box-sizing--박스-크기-계산-방식">다. box-sizing — 박스 크기 계산 방식</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/9b57ba16-b170-49dd-aadb-d946f67570bc/image.png" /></p>
<pre><code class="language-css">/* content-box: 크기 = 내용만 (테두리 붙이면 상자가 커짐) */
.content-box { box-sizing: content-box; }

/* border-box: 크기 = 테두리 포함 전체 (크기 고정) */
.border-box { box-sizing: border-box; }</code></pre>
<p><strong>실무에서는 거의 <code>border-box</code> 씀.</strong> 크기 계산이 직관적으로 편하기 때문이다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/8ce34be2-f736-4392-aa26-a73b0c711d30/image.png" /></p>
<hr />
<h2 id="4-박스에-배경-추가하기">4. 박스에 배경 추가하기</h2>
<h3 id="주요-배경-속성-정리">주요 배경 속성 정리</h3>
<pre><code class="language-css">body {
  background-color: darkgray;
  background-image: url(&quot;bg.jpg&quot;);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  min-height: 100vh;
}</code></pre>
<table>
<thead>
<tr>
<th>속성</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>background-color</code></td>
<td>배경 색상</td>
</tr>
<tr>
<td><code>background-image</code></td>
<td>배경 이미지</td>
</tr>
<tr>
<td><code>background-repeat</code></td>
<td>이미지 반복 여부</td>
</tr>
<tr>
<td><code>background-position</code></td>
<td>이미지 위치</td>
</tr>
<tr>
<td><code>background-size</code></td>
<td>이미지 크기</td>
</tr>
<tr>
<td><code>background-clip</code></td>
<td>배경 색상 적용 범위</td>
</tr>
<tr>
<td><code>background-origin</code></td>
<td>이미지 시작 기준점</td>
</tr>
</tbody></table>
<h3 id="background-clip--배경색-적용-범위">background-clip — 배경색 적용 범위</h3>
<pre><code class="language-css">.first  { background-clip: border-box; }   /* 테두리까지 */
.second { background-clip: content-box; }  /* 내용 영역만 */
.third  { background-clip: padding-box; }  /* 패딩까지 */</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/341ca5ba-3ab9-4a61-97c7-6bbd0a4a8f90/image.png" /></p>
<h3 id="background-repeat-속성값">background-repeat 속성값</h3>
<ul>
<li><code>repeat</code> : 기본값, 영역 채울 때까지 반복</li>
<li><code>repeat-x</code> : 가로 방향만 반복</li>
<li><code>repeat-y</code> : 세로 방향만 반복</li>
<li><code>no-repeat</code> : 한 번만 표시</li>
<li><code>space</code> : 이미지 잘리지 않게 최대 개수 반복</li>
</ul>
<h3 id="background-origin">background-origin</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/7fa51365-838f-487a-8a7c-07dedcc8aac2/image.png" /></p>
<p>배경 이미지의 (0, 0) 좌표를 어디에 맞출지 결정한다.</p>
<h3 id="background-size">background-size</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/5e28b40c-7449-4ab0-b499-11670c6df899/image.png" /></p>
<pre><code class="language-css">background-size: cover;
/* contain보다 cover가 더 보기 좋음 */
/* 가운데 콘텐츠 유지하면서 크기 유동적으로 변경 가능 */
/* 배경화면에 많이 사용 */</code></pre>
<h3 id="background-position">background-position</h3>
<pre><code class="language-css">/* 키워드 사용 */
background-position: right bottom;

/* px 사용 */
background-position: 50px 100px;

/* % 사용 (center와 동일) */
background-position: 50% 50%;</code></pre>
<hr />
<h2 id="5-텍스트-꾸미기">5. 텍스트 꾸미기</h2>
<h3 id="가-font-family--글꼴-지정">가. font-family — 글꼴 지정</h3>
<pre><code class="language-css">p {
  font-family: Arial, Helvetica, sans-serif;
}</code></pre>
<p>여러 개 지정하면 앞에서부터 순서대로 적용한다. 앞 글꼴이 없으면 다음 글꼴로 넘어감.</p>
<h3 id="나-웹폰트-사용하기">나. 웹폰트 사용하기</h3>
<pre><code class="language-css">@font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/...');
}

body {
    font-family: 'Pretendard-Regular', sans-serif;
}</code></pre>
<blockquote>
<p>noonnu.cc 에서 무료 폰트 찾을 수 있음!</p>
</blockquote>
<h3 id="다-font-size--글자-크기">다. font-size — 글자 크기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/71e1615b-5e64-4ba3-9b3b-282c5dfa29e6/image.png" /></p>
<table>
<thead>
<tr>
<th>단위</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>px</code></td>
<td>절대 단위</td>
<td><code>font-size: 16px</code></td>
</tr>
<tr>
<td><code>%</code></td>
<td>부모 기준 백분율</td>
<td>부모 20px × 150% = 30px</td>
</tr>
<tr>
<td><code>em</code></td>
<td>부모 글자 크기 기준 배수</td>
<td>부모 16px × 1.5em = 24px</td>
</tr>
<tr>
<td><code>rem</code></td>
<td>html 루트 기준 배수</td>
<td>html 20px × 2rem = 40px</td>
</tr>
</tbody></table>
<pre><code class="language-css">html { font-size: 20px; }
div  { font-size: 30px; }
p    { font-size: 2rem; } /* 부모(div) 무시, html 기준 40px */</code></pre>
<p><strong>rem vs em 차이:</strong></p>
<ul>
<li><code>em</code> : 부모 요소 기준 → 중첩되면 계산이 복잡해짐</li>
<li><code>rem</code> : 항상 html 루트 기준 → 일관성 있어서 실무에서 선호</li>
</ul>
<h3 id="라-text-decoration--텍스트-줄-표시">라. text-decoration — 텍스트 줄 표시</h3>
<pre><code class="language-css">a { text-decoration: none; }       /* 밑줄 제거 */
p { text-decoration: underline; }  /* 밑줄 */
p { text-decoration: overline; }   /* 윗줄 */
p { text-decoration: line-through; } /* 취소선 */</code></pre>
<h3 id="마-색상-지정하기">마. 색상 지정하기</h3>
<pre><code class="language-css">p { color: red; }                   /* 색상 이름 */
p { color: rgb(255, 0, 0); }        /* RGB 함수 */
p { color: hsl(0, 100%, 50%); }     /* HSL 함수 */
p { color: #ff0000; }               /* 16진수 */
p { opacity: 0.5; }                 /* 투명도 (0~1) */</code></pre>
<h3 id="바-display--요소-유형-바꾸기">바. display — 요소 유형 바꾸기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/c29ca740-dcfe-4c88-ae1d-d01af38df56f/image.png" /></p>
<hr />
<h2 id="6-실습-코드-분석--메뉴와-버튼-꾸미기">6. 실습 코드 분석 — 메뉴와 버튼 꾸미기</h2>
<pre><code class="language-css">/* 링크 메뉴 꾸미기 */
a.menu {
    display: inline-block; /* 크기 조절 가능하게 변경 */
    font-size: 25pt;
    text-decoration: none;
    min-width: 120px;
    text-align: center;
}

/* 마우스 올렸을 때 효과 */
a.menu:hover {
    color: #FAE251;
    text-decoration: underline;
}

/* 박스 크기 계산 방식 고정 */
#box {
    box-sizing: border-box;
}</code></pre>
<hr />
<h2 id="7-유용한-사이트-모음">7. 유용한 사이트 모음</h2>
<p>수업에서 언급된 사이트들, 꼭 북마크 해두기!</p>
<ul>
<li><strong><a href="https://caniuse.com">caniuse.com</a></strong> : 특정 태그/속성이 어떤 브라우저에서 작동하는지 확인</li>
<li><strong><a href="https://colorhunt.co">colorhunt.co</a></strong> : 어울리는 색상 조합 추천</li>
<li><strong><a href="https://noonnu.cc">noonnu.cc</a></strong> : 상업용 무료 폰트 모음</li>
</ul>
<hr />
<h2 id="오늘-수업-마무리">오늘 수업 마무리</h2>
<p>오늘은 CSS의 핵심 개념들을 한꺼번에 익혀보는 수업시간을 가졌다. 선택자 우선순위, 박스모델, 배경 속성, 텍스트까지... 양이 많아서 다 소화하려면 직접 코드 쳐보는 게 최선인 것 같다. 특히 <code>box-sizing: border-box</code>랑 <code>rem</code> 단위는 실무에서 자주 쓴다고 하니까 확실히 익혀둬야겠다! 복습의 또 복습을! 과제도 열심히!</p>