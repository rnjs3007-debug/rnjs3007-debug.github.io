---
layout: post
title: "Node.js EJS 템플릿 엔진 조사 보고서"
date: 2026-05-13 11:08:51 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/Node.js-EJS-%ED%85%9C%ED%94%8C%EB%A6%BF-%EC%97%94%EC%A7%84-%EC%A1%B0%EC%82%AC-%EB%B3%B4%EA%B3%A0%EC%84%9C
---

<p>자료 참고: <a href="https://ejs.co/">https://ejs.co/</a></p>
<hr />
<h2 id="1-템플릿-엔진이란">1. 템플릿 엔진이란?</h2>
<p>웹사이트를 만들 때, 모든 사람에게 똑같은 화면을 보여주면 안 되는 경우가 있다.</p>
<p>예를 들어 쇼핑몰에 로그인하면 &quot;아름님, 환영합니다!&quot;라고 뜨는 것처럼, 사람마다 다른 내용이 표시되어야 한다.</p>
<p>그런데 HTML은 기본적으로 정해진 내용만 보여줄 수 있다. 마치 인쇄된 종이처럼, 한번 찍히면 내용을 바꿀 수 없다.</p>
<p><strong>'템플릿 엔진'은 이 문제를 해결해주는 도구라고 할수있다.</strong></p>
<blockquote>
<p>간단한 예시를 들면,
빈칸이 있는 문서양식이라고 생각하면 쉽다.
&quot;OO님, 주문하신 OO이 배송되었습니다.&quot; 처럼 틀(템플릿)을 만들어두고,
실제 이름과 상품명만 서버에서 채워 넣는 방식이다.</p>
</blockquote>
<pre><code>[틀(HTML 템플릿)] + [채울 내용(데이터)]  →  [완성된 HTML]  →  [사용자 화면]</code></pre><hr />
<h2 id="2-ejs란">2. EJS란?</h2>
<p>EJS(Embedded JavaScript Templating)는 <strong>Node.js</strong>에서 가장 많이 사용되는 템플릿 엔진이다.</p>
<p>이름 그대로 HTML 파일 안에 JavaScript 코드를 심어서(Embed) 동적인 페이지를 만들 수 있다.</p>
<ul>
<li>비교적 용량이 작고(119KB), 따로 설치해야 하는 다른 패키지가 없다</li>
<li>새로운 언어를 배울 필요 없이, 이미 아는 JavaScript를 그대로 사용할 수 있다.</li>
</ul>
<h3 id="주요-특징">주요 특징</h3>
<table>
<thead>
<tr>
<th>특징</th>
<th>쉬운 설명</th>
</tr>
</thead>
<tbody><tr>
<td>친숙한 문법</td>
<td>새 언어 필요 없음. JavaScript 그대로 사용가능</td>
</tr>
<tr>
<td>빠른 실행</td>
<td>한 번 만든 페이지를 기억해뒀다가 빠르게 재사용</td>
</tr>
<tr>
<td>간편한 디버깅</td>
<td>오류가 나면 몇 번째 줄인지 알려줌</td>
</tr>
<tr>
<td>Partial 지원</td>
<td>헤더·푸터 같은 공통 부분을 따로 파일로 저장해 재사용</td>
</tr>
<tr>
<td>Express 연동</td>
<td>Node.js의 대표 웹 프레임워크인 Express와 바로 연결 가능</td>
</tr>
</tbody></table>
<hr />
<h2 id="3-동작-방식">3. 동작 방식</h2>
<p>사용자가 웹페이지를 열면 내부적으로 다음 순서로 동작한다.</p>
<pre><code>1. 사용자가 브라우저에서 주소를 입력 (예: 뭐시기쇼핑몰.com/mypage)
         ↓
2. 서버가 요청을 받아 처리 시작
         ↓
3. &quot;mypage.ejs 파일을 이 데이터로 완성해줘&quot; 라고 EJS에 요청
         ↓
4. EJS가 .ejs 파일(빈칸 있는 틀-양식/문서)을 읽음
         ↓
5. 빈칸에 실제 데이터를 채워 넣음
         ↓
6. 완성된 HTML 문서가 만들어짐
         ↓
7. 사용자의 브라우저에 완성된 페이지 전달</code></pre><blockquote>
<p>쉽게 말하면 &quot;미리 작성해둔 고정양식에 내용을 자동으로 채워주는 기계&quot;라고 생각하면 될 것 같다.</p>
</blockquote>
<hr />
<h2 id="4-설치-및-기본-설정">4. 설치 및 기본 설정</h2>
<h3 id="4-1-패키지-설치">4-1. 패키지 설치</h3>
<p>터미널에서 아래 명령어를 입력하면 Express와 EJS가 함께 설치된다.</p>
<pre><code>npm install express ejs</code></pre><h3 id="4-2-express와-연동">4-2. Express와 연동</h3>
<pre><code class="language-javascript">// app.js
const express = require('express');
const path = require('path');
const app = express();

// &quot;나는 EJS를 사용할 거야&quot; 라고 Express에게 알려주는 설정
app.set('view engine', 'ejs');

// EJS 파일들이 들어있는 폴더 위치 알려주기
app.set('views', path.join(__dirname, 'views'));

// 누군가 첫 페이지('/')에 접속하면
app.get('/', (req, res) =&gt; {
  // index.ejs 파일에 아래 데이터를 채워서 보내줘
  res.render('index', { title: 'EJS 예제', userName: '아름' });
});

app.listen(3000, () =&gt; {
  console.log('서버 실행 중: http://localhost:3000');
});</code></pre>
<h3 id="4-3-디렉토리폴더-구조">4-3. 디렉토리(폴더) 구조</h3>
<pre><code>project/
├── app.js              ← 서버 실행 파일
├── package.json        ← 프로젝트 정보 및 패키지 목록
├── views/              ← EJS 템플릿(틀) 파일 모음
│   ├── index.ejs       ← 메인 페이지 틀
│   ├── header.ejs      ← 공통 헤더 (모든 페이지 상단)
│   └── footer.ejs      ← 공통 푸터 (모든 페이지 하단)
└── public/
    └── style.css       ← 디자인(CSS) 파일</code></pre><blockquote>
<p>EJS 자체 기능인 'include'를 사용해서 파일을 나눈다.</p>
</blockquote>
<hr />
<h2 id="5-ejs-문법">5. EJS 문법</h2>
<p>EJS에서는 HTML 코드 사이에 <code>&lt;% %&gt;</code>처럼 생긴 특수 태그를 사용해서 JavaScript를 실행하거나 데이터를 출력한다.</p>
<h3 id="5-1-태그-종류-요약">5-1. 태그 종류 요약</h3>
<table>
<thead>
<tr>
<th>태그</th>
<th>역할</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;% %&gt;</code></td>
<td>JavaScript 실행 (화면에 출력 안 됨)</td>
<td><code>&lt;% const x = 10; %&gt;</code></td>
</tr>
<tr>
<td><code>&lt;%= %&gt;</code></td>
<td>값을 화면에 출력 (안전하게)</td>
<td><code>&lt;%= userName %&gt;</code></td>
</tr>
<tr>
<td><code>&lt;%- %&gt;</code></td>
<td>값을 화면에 출력 (HTML 그대로)</td>
<td><code>&lt;%- htmlContent %&gt;</code></td>
</tr>
<tr>
<td><code>&lt;%# %&gt;</code></td>
<td>주석. 화면에 표시 안 됨</td>
<td><code>&lt;%# 이건 주석 %&gt;</code></td>
</tr>
</tbody></table>
<blockquote>
<p><code>&lt;%= %&gt;</code>와 <code>&lt;%- %&gt;</code>의 차이:
만일 사용자가 '악의적인 코드'를 입력했을 때, <code>&lt;%= %&gt;</code>는 그걸 그냥 문자로 처리해서 안전하다.
<code>&lt;%- %&gt;</code>는 그대로 실행시키게 됨으로, 믿을 수 있는 내용에 대해서만 사용해야 한다.</p>
</blockquote>
<h3 id="5-2-변수-출력--빈칸-채우기">5-2. 변수 출력 — 빈칸 채우기</h3>
<p>서버에서 보낸 데이터를 HTML의 원하는 자리에 출력한다.</p>
<pre><code class="language-html">&lt;!-- views/index.ejs --&gt;
&lt;h1&gt;안녕하세요, &lt;%= userName %&gt;님!&lt;/h1&gt;
&lt;p&gt;페이지 제목: &lt;%= title %&gt;&lt;/p&gt;</code></pre>
<pre><code class="language-javascript">// 서버에서 데이터 전달
res.render('index', { title: 'EJS 예제', userName: '아름' });</code></pre>
<p>결과 화면:</p>
<pre><code>안녕하세요, 아름님!
페이지 제목: EJS 예제</code></pre><h3 id="5-3-조건문--상황에-따라-다른-내용-보여주기">5-3. 조건문 — 상황에 따라 다른 내용 보여주기</h3>
<pre><code class="language-html">&lt;% if (isLoggedIn) { %&gt;
  &lt;p&gt;로그인 상태입니다.&lt;/p&gt;
&lt;% } else { %&gt;
  &lt;p&gt;로그인이 필요합니다.&lt;/p&gt;
&lt;% } %&gt;</code></pre>
<p>로그인 여부에 따라 다른 문장이 화면에 표시된다.</p>
<h3 id="5-4-appget-코드-해석">5-4. app.get() 코드 해석</h3>
<pre><code class="language-javascript">app.get('/', (req, res) =&gt; {
  res.render('index', { isLoggedIn: true });
});</code></pre>
<p><strong><code>app.get('/', (req, res) =&gt; {</code></strong></p>
<p>누군가 웹사이트 첫 페이지(<code>/</code>)에 접속하면 이 코드를 실행해라.</p>
<ul>
<li><code>app.get</code> → &quot;GET 요청이 오면&quot; (브라우저 주소창에 주소 입력하는 것)</li>
<li><code>'/'</code> → 첫 페이지 주소 (예: www.뭐시기뭐시기.com)</li>
<li><code>(req, res)</code> → req는 <strong>요청</strong>(Request, 사용자가 보낸 것), res는 <strong>응답</strong>(Response, 서버가 돌려줄 것)</li>
</ul>
<p><strong><code>res.render('index', { isLoggedIn: true });</code></strong></p>
<p>사용자에게 응답으로 <code>index.ejs</code> 파일을 완성해서 보내라.</p>
<ul>
<li><code>res.render</code> → &quot;이 파일을 완성해서 브라우저에 보내줘&quot;</li>
<li><code>'index'</code> → <code>views/index.ejs</code> 파일을 사용해라</li>
<li><code>{ isLoggedIn: true }</code> → EJS 파일에 이 데이터를 넘겨줘라</li>
</ul>
<p><strong><code>{ isLoggedIn: true }</code> 이 부분만 따로 해석을하면,</strong></p>
<p>이게 EJS 파일로 전달되면, EJS 안에서 <code>isLoggedIn</code>을 변수처럼 바로 쓸 수 있게 된다.</p>
<pre><code class="language-html">&lt;% if (isLoggedIn) { %&gt;   &lt;!-- 여기서 true/false를 받아서 판단 --&gt;
&lt;% } %&gt;</code></pre>
<blockquote>
<p>&quot;누군가 첫 페이지에 접속하면, <code>isLoggedIn = true</code> 라는 데이터를 <code>index.ejs</code>에 넘겨서 완성된 HTML을 만들어 브라우저에 보내라.&quot;</p>
</blockquote>
<hr />
<h3 id="5-5-반복문-목록-자동으로-만들기">5-5. 반복문: 목록 자동으로 만들기</h3>
<p>상품 목록, 게시글 목록처럼 비슷한 항목이 여러 개일 때 유용하다.</p>
<pre><code class="language-html">&lt;ul&gt;
  &lt;% items.forEach(function(item) { %&gt;
    &lt;li&gt;&lt;%= item %&gt;&lt;/li&gt;
  &lt;% }); %&gt;
&lt;/ul&gt;</code></pre>
<p>서버에서 <code>{ items: ['티셔츠', '반바지', '남방'] }</code>를 보내면 아래처럼 자동으로 만들어진다.</p>
<pre><code class="language-html">&lt;ul&gt;
  &lt;li&gt;티셔츠&lt;/li&gt;
  &lt;li&gt;반바지&lt;/li&gt;
  &lt;li&gt;남방&lt;/li&gt;
&lt;/ul&gt;</code></pre>
<hr />
<h2 id="6-partial-공통-부분-재사용하기">6. Partial: 공통 부분 재사용하기</h2>
<p>모든 페이지에 똑같이 들어가는 헤더(상단 메뉴)나 푸터(하단 정보)를 매번 복사해서 넣으면 수정할 때 모든 파일을 일일이 고쳐야 한다.</p>
<p>Partial 기능을 쓰면 공통 부분을 별도 파일로 만들어두고, 필요한 곳에서 불러오기만 하면 된다. 수정도 그 파일 하나만 고치면 끝이다.</p>
<pre><code class="language-html">&lt;!-- views/header.ejs (공통 헤더 파일) --&gt;
&lt;header&gt;
  &lt;h1&gt;내 웹사이트&lt;/h1&gt;
  &lt;nav&gt;&lt;a href=&quot;/&quot;&gt;홈&lt;/a&gt; | &lt;a href=&quot;/about&quot;&gt;소개&lt;/a&gt;&lt;/nav&gt;
&lt;/header&gt;</code></pre>
<pre><code class="language-html">&lt;!-- views/index.ejs --&gt;
&lt;%- include('header') %&gt;   &lt;!-- 여기에 header.ejs 내용이 통째로 삽입됨 --&gt;

&lt;main&gt;
  &lt;h2&gt;메인 콘텐츠&lt;/h2&gt;
&lt;/main&gt;

&lt;%- include('footer') %&gt;   &lt;!-- 여기에 footer.ejs 내용이 통째로 삽입됨 --&gt;</code></pre>
<blockquote>
<p>include는 반드시 <code>&lt;%- %&gt;</code>와 함께 사용한다. <code>&lt;%= %&gt;</code>를 쓰면 HTML이 문자로 출력되어 깨진다.</p>
</blockquote>
<hr />
<h2 id="7-주요-api">7. 주요 API</h2>
<p>EJS를 코드에서 직접 호출하는 방법은 크게 세 가지가 있다. </p>
<pre><code class="language-javascript">
const ejs = require('ejs');

// 방법 1. 문자열(HTML 코드)을 직접 렌더링
const html = ejs.render('&lt;p&gt;&lt;%= msg %&gt;&lt;/p&gt;', { msg: 'Hello EJS!' });
// 결과: '&lt;p&gt;Hello EJS!&lt;/p&gt;'

// 방법 2. .ejs 파일을 읽어서 렌더링 
ejs.renderFile('./views/index.ejs', { title: '제목' }, (err, html) =&gt; {
  console.log(html); // 완성된 HTML 출력
});

// 방법 3. 템플릿을 미리 컴파일해두고 여러 번 재사용 (속도 최적화)
const template = ejs.compile('&lt;p&gt;&lt;%= name %&gt;&lt;/p&gt;');
console.log(template({ name: '아름1' })); // =&gt; &lt;p&gt;아름1&lt;/p&gt; 으로 출력됨
console.log(template({ name: '아름2' })); // =&gt; &lt;p&gt;아름2&lt;/p&gt; 으로 출력됨
</code></pre>
<hr />
<h2 id="8-캐싱-caching">8. 캐싱 (Caching)</h2>
<p>EJS는 같은 템플릿을 두 번째 요청할 때부터는-&gt; 처음부터 다시 처리하지 않고, 첫 번째에 만들어둔 결과를 기억해뒀다가 빠르게 재사용한다. 이것을 '캐싱'이라고 한다.</p>
<p>방문자가 많은 대규모 사이트에서는 'lru-cache' 라이브러리를 연동해 캐시 개수를 제한할 수 있다.</p>
<pre><code class="language-javascript">import ejs from 'ejs';
import { LRUCache } from 'lru-cache';

//import { LRUCache, LRUMap, LinkedList } from 'lru-cache';
//       ↑ 이것도    ↑ 이것도  ↑ 이것도 가져와줘  (작성방법)

ejs.cache = new LRUCache({ max: 100 }); // 최대 100개까지 기억
ejs.clearCache(); // 기억 전체 삭제</code></pre>
<hr />
<h2 id="9-커스텀-구분자">9. 커스텀 구분자</h2>
<p>기본적으로 EJS는 <code>&lt;% %&gt;</code>를 구분자로 사용하지만, 다른 기호로 바꿀 수도 있다.</p>
<p>기존 코드와 기호가 겹쳐서 충돌이 생길 때 유용하다.</p>
<pre><code class="language-javascript">// '?' 를 구분자로 사용하기
ejs.render('&lt;?= users.join(&quot; | &quot;); ?&gt;', { users: ['A', 'B'] }, { delimiter: '?' });
//{ delimiter: '?' } → 이번엔 % 대신 ?를 구분자로 쓸게


// '$' 를 전역 구분자로 설정
ejs.delimiter = '$';
ejs.render('&lt;$= name $&gt;', { name: '아름' }); // =&gt; 아름</code></pre>
<hr />
<h2 id="10-cli-사용법">10. CLI 사용법</h2>
<p>EJS는 터미널(명령 프롬프트)에서 직접 실행할 수도 있다. 코드 없이 간단히 HTML 파일을 만들어낼 때 유용하다.</p>
<pre><code># 템플릿 파일로 HTML 파일 만들기
&gt;&gt; ejs template.ejs -o output.html

-&gt;결과: template.ejs → 완성된 output.html 파일이 만들어짐

# 데이터 파일(.json)을 지정해서 사용
&gt;&gt; ejs template.ejs -f data.json -o output.html
-&gt;결과: template.ejs 파일을 사용해서, 채워넣을 데이터는 '-f data.json'파일에서 가져온뒤에, '-o output.html'결과물을 저장.

# 변수를 직접 입력해서 사용
&gt;&gt; ejs template.ejs name=아름</code></pre><hr />
<h2 id="11-ejs-vs-react--vue">11. EJS vs React / Vue</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>EJS + Express</th>
<th>React / Vue</th>
</tr>
</thead>
<tbody><tr>
<td>언제 HTML을 만드나</td>
<td>서버에서 미리 만들어서 전달</td>
<td>브라우저에서 JavaScript로 실시간 생성</td>
</tr>
<tr>
<td>빌드 도구 필요 여부</td>
<td>불필요 (설치 후 바로 사용)</td>
<td>필요 (webpack, vite 등)</td>
</tr>
<tr>
<td>화면 반응성</td>
<td>제한적 (클릭하면 서버에 다시 요청)</td>
<td>풍부 (클릭 즉시 화면 바뀜)</td>
</tr>
<tr>
<td>적합한 상황</td>
<td>블로그, 관리자 페이지, 간단한 웹앱</td>
<td>카카오톡 웹, 인스타그램 같은 앱</td>
</tr>
<tr>
<td>시작 난이도</td>
<td>쉬움</td>
<td>어려움</td>
</tr>
</tbody></table>
<hr />
<h2 id="내용정리">내용정리.</h2>
<ul>
<li>EJS는 'HTML 틀에 JavaScript로 데이터를 채워 넣어' 동적인 웹 페이지를 만드는 도구다.</li>
<li><code>&lt;%= %&gt;</code>로 데이터 출력, <code>&lt;% %&gt;</code>로 조건·반복 제어, <code>&lt;%- include() %&gt;</code>로 공통 부분 재사용이 핵심이다.</li>
<li>Express.js와 간단히 연동되며, 새로운 언어 없이 JavaScript만으로 동작한다.</li>
</ul>
<hr />