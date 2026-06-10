---
layout: post
title: "Node.js + Express 백엔드 복습"
date: 2026-06-10 11:21:41 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/Node.js-Express-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%B3%B5%EC%8A%B5-%EA%B0%80%EC%9D%B4%EB%93%9C
---

<hr />
<h2 id="1-개념-정리">1. 개념 정리</h2>
<h3 id="nodejs란">Node.js란?</h3>
<p>브라우저 밖에서 JavaScript를 실행할 수 있게 해주는 환경.<br />원래 JS는 브라우저에서만 돌아갔는데, Node.js 덕분에 서버에서도 JS를 쓸 수 있게 됨.</p>
<h3 id="express란">Express란?</h3>
<p>Node.js로 서버를 쉽게 만들 수 있게 도와주는 라이브러리(패키지).<br /><code>npm install express</code> 로 설치해서 씀.</p>
<h3 id="ejs란">EJS란?</h3>
<p>HTML 파일 안에서 JavaScript 문법을 쓸 수 있게 해주는 템플릿 엔진.<br />확장자가 <code>.ejs</code>이고 <code>views</code> 폴더 안에 넣어야 함.</p>
<pre><code>&lt;% %&gt;   → JS 실행 (if문, for문 등)
&lt;%= %&gt;  → 값 출력</code></pre><h3 id="http-메서드-crud">HTTP 메서드 (CRUD)</h3>
<table>
<thead>
<tr>
<th>동작</th>
<th>메서드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>Create</td>
<td>POST</td>
<td>데이터 생성</td>
</tr>
<tr>
<td>Read</td>
<td>GET</td>
<td>데이터 조회</td>
</tr>
<tr>
<td>Update</td>
<td>PUT / PATCH</td>
<td>데이터 수정</td>
</tr>
<tr>
<td>Delete</td>
<td>DELETE</td>
<td>데이터 삭제</td>
</tr>
</tbody></table>
<hr />
<h2 id="2-파일-구조-만들기">2. 파일 구조 만들기</h2>
<p>아래 순서대로 폴더와 파일을 직접 만들어보기.</p>
<pre><code>my-project/
  ├── views/
  │     └── index.ejs
  ├── package.json
  └── server.js</code></pre><h3 id="터미널에서-순서대로-입력">터미널에서 순서대로 입력</h3>
<pre><code class="language-bash"># 1. 프로젝트 폴더 생성 및 이동
mkdir my-project
cd my-project

# 2. package.json 자동 생성
npm init -y

# 3. 필요한 패키지 설치
npm install express ejs

# 4. views 폴더 생성
mkdir views</code></pre>
<p>그 다음 VS Code에서 <code>server.js</code>와 <code>views/index.ejs</code> 파일 직접 생성.</p>
<hr />
<h2 id="3-serverjs-작성">3. server.js 작성</h2>
<pre><code class="language-javascript">// 1. express 불러오기
const express = require('express');
const app = express();

// 2. EJS 뷰 엔진 설정
app.set('view engine', 'ejs');

// 3. POST 요청 body 파싱 설정 (폼 데이터 받을 때 필수!)
app.use(express.urlencoded({ extended: true }));

// 4. 임시 데이터 저장소 (DB 대신)
const data = [];

// 5. GET - 메인화면
app.get('/', function(req, res) {
    res.render('index', { data });
});

// 6. POST - 데이터 등록
app.post('/add', function(req, res) {
    if (req.body.content) {
        data.push(req.body.content);
    }
    res.redirect('/');
});

// 7. 서버 실행 (포트 80)
app.listen(80);</code></pre>
<h3 id="핵심-포인트">핵심 포인트</h3>
<p><code>req.body</code> → POST로 받은 폼 데이터 (urlencoded 설정 필수)<br /><code>req.query</code> → GET으로 받은 URL 파라미터 (<code>?name=홍길동</code>)  
<code>req.params</code> → URL 경로 파라미터 (<code>/user/:id</code> 에서 <code>:id</code> 부분)</p>
<p><code>res.render('index', { data })</code> → index.ejs를 렌더링하면서 data 전달<br /><code>res.send('내용')</code> → 문자열 그대로 응답<br /><code>res.redirect('/')</code> → 다른 주소로 이동</p>
<hr />
<h2 id="4-viewsindexejs-작성">4. views/index.ejs 작성</h2>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;title&gt;나의 앱&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

    &lt;!-- 데이터 목록 출력 (for문) --&gt;
    &lt;ul&gt;
        &lt;% for(let i = 0; i &lt; data.length; i++) { %&gt;
            &lt;li&gt;&lt;%= data[i] %&gt;&lt;/li&gt;
        &lt;% } %&gt;
    &lt;/ul&gt;

    &lt;!-- 데이터 입력 폼 --&gt;
    &lt;form action=&quot;/add&quot; method=&quot;post&quot;&gt;
        &lt;input name=&quot;content&quot; placeholder=&quot;내용 입력&quot;&gt;
        &lt;button type=&quot;submit&quot;&gt;등록&lt;/button&gt;
    &lt;/form&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>
<h3 id="ejs-핵심-문법">EJS 핵심 문법</h3>
<pre><code class="language-html">&lt;!-- 조건문 --&gt;
&lt;% if(data.length &gt; 0) { %&gt;
    &lt;p&gt;데이터가 있습니다.&lt;/p&gt;
&lt;% } %&gt;

&lt;!-- 반복문 --&gt;
&lt;% for(let i = 0; i &lt; data.length; i++) { %&gt;
    &lt;p&gt;&lt;%= data[i] %&gt;&lt;/p&gt;
&lt;% } %&gt;

&lt;!-- 값 출력 --&gt;
&lt;p&gt;&lt;%= 변수명 %&gt;&lt;/p&gt;</code></pre>
<hr />
<h2 id="5-서버-실행">5. 서버 실행</h2>
<pre><code class="language-bash">node server.js</code></pre>
<p>터미널에 아무것도 안 뜨고 커서만 깜빡이면 → 정상! 서버 켜진 것.</p>
<p>브라우저에서 <code>localhost</code> 접속.</p>
<p>서버 종료: <code>Ctrl + C</code></p>
<h3 id="nodemon-사용-코드-저장시-자동-재시작">nodemon 사용 (코드 저장시 자동 재시작)</h3>
<pre><code class="language-bash">npm install -g nodemon
nodemon server.js</code></pre>
<hr />
<h2 id="6-자주-나왔던-오류-정리">6. 자주 나왔던 오류 정리</h2>
<table>
<thead>
<tr>
<th>오류</th>
<th>원인</th>
<th>해결</th>
</tr>
</thead>
<tbody><tr>
<td><code>Cannot find module 'express'</code></td>
<td>express 미설치</td>
<td><code>npm install express</code></td>
</tr>
<tr>
<td><code>req.body is undefined</code></td>
<td>urlencoded 미설정</td>
<td><code>app.use(express.urlencoded({extended:true}))</code> 추가</td>
</tr>
<tr>
<td><code>Missing script: &quot;start&quot;</code></td>
<td>package.json에 start 없음</td>
<td><code>node server.js</code> 로 직접 실행</td>
</tr>
<tr>
<td><code>JSONParseError</code></td>
<td>package.json 쉼표 오타</td>
<td>scripts 항목 사이 <code>,</code> 확인</td>
</tr>
<tr>
<td><code>Cannot GET /</code></td>
<td>해당 라우터 없음</td>
<td><code>app.get('/', ...)</code> 추가</td>
</tr>
<tr>
<td><code>views 폴더 못 찾음</code></td>
<td>views가 server.js랑 다른 위치</td>
<td>server.js와 같은 폴더 안에 views 넣기</td>
</tr>
</tbody></table>
<hr />
<h2 id="7-전체흐름">7. 전체흐름</h2>
<pre><code>브라우저 요청
    ↓
server.js (라우터가 요청 받음)
    ↓
req.body / req.query / req.params 로 데이터 꺼냄
    ↓
로직 처리 (배열에 저장, 삭제 등)
    ↓
res.render() / res.send() / res.redirect() 로 응답
    ↓
브라우저 화면 출력</code></pre><hr />
<h2 id="8-혼자-복습순서">8. 혼자 복습순서</h2>
<p>아래 순서대로 처음부터 혼자 만들어보기.</p>
<ol>
<li>새 폴더 만들고 <code>npm init -y</code></li>
<li><code>npm install express ejs</code></li>
<li><code>server.js</code> 작성 (GET / POST 라우터 포함)</li>
<li><code>views/index.ejs</code> 작성 (for문으로 목록 출력 + 폼)</li>
<li><code>node server.js</code> 실행</li>
<li>브라우저에서 <code>localhost</code> 접속해서 확인</li>
</ol>