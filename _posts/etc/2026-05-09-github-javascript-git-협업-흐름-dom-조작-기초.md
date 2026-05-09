---
layout: post
title: "[GitHub & JavaScript] Git 협업 흐름 & DOM 조작 기초"
date: 2026-05-09 13:00:42 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/GitHub-JavaScript-Git-%ED%98%91%EC%97%85-%ED%9D%90%EB%A6%84-DOM-%EC%A1%B0%EC%9E%91-%EA%B8%B0%EC%B4%88
---

<blockquote>
<p>260417 수업
초반에는 GitHub로 코드를 올리고 내려받는 흐름을 직접 해봤고,
후반부에는 자바스크립트로 HTML을 직접 건드리는 DOM 조작을 다뤘다.
특히 JS 문법이 C나 파이썬이랑 미묘하게 달라서 헷갈리는 부분이 꽤 있었다.</p>
</blockquote>
<hr />
<h2 id="순서">순서</h2>
<ol>
<li><a href="https://v2.velog.io/rss/@addung#github-%EA%B8%B0%EB%B3%B8-%ED%9D%90%EB%A6%84">GitHub 기본 흐름</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EB%B3%80%EC%88%98-%EC%84%A0%EC%96%B8">JavaScript 변수 선언</a></li>
<li><a href="https://v2.velog.io/rss/@addung#dom-%EC%A1%B0%EC%9E%91">DOM 접근과 조작</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%B4%EB%B2%A4%ED%8A%B8">이벤트 연결</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%82%BC%ED%95%AD-%EC%97%B0%EC%82%B0%EC%9E%90">삼항 연산자</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EB%B0%B0%EC%97%B4">배열과 주요 메서드</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%91%EC%9A%A9-%EC%8B%A4%ED%97%98">응용 실험</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC">핵심 정리</a></li>
</ol>
<hr />
<h2 id="1-github-기본-흐름">1. GitHub 기본 흐름</h2>
<p>로컬(내 컴퓨터)과 원격(GitHub 서버) 사이를 왔다갔다 하는 게 Git의 핵심이다.</p>
<pre><code>작업 흐름:

GitHub 서버 ──pull──▶ 내 컴퓨터 (로컬)
              ◀──push── 내 컴퓨터 (로컬)</code></pre><h3 id="기본-순서">기본 순서</h3>
<pre><code>1. sync fork   → 원격 저장소 최신 상태로 동기화
2. git pull    → 서버에 있는 내용을 내 컴퓨터로 가져오기
3. 코드 작업   → VS Code에서 수정
4. commit      → 변경 내용 저장 (로컬)
5. git push    → 내 컴퓨터 작업물을 서버에 올리기</code></pre><blockquote>
<p>작업 시작 전에 <strong>항상 pull 먼저</strong> 하는 습관이 중요하다.
안 하면 다른 사람 작업자와 충돌이 날 수 있다.</p>
</blockquote>
<h3 id="알아두면-좋은-것들">알아두면 좋은 것들</h3>
<ul>
<li><code>README.md</code> — 저장소 첫 화면에 보이는 소개 파일</li>
<li><code>Pull Request</code> — 내 작업을 메인 브랜치에 합쳐달라고 요청하는 것</li>
<li><strong>GitHub Pages</strong> — Settings → Pages 에서 활성화하면 HTML 파일을 웹페이지로 바로 배포 가능</li>
</ul>
<hr />
<h2 id="2-javascript-변수-선언">2. JavaScript 변수 선언</h2>
<p>JS에는 변수를 만드는 방법이 세 가지다.</p>
<pre><code class="language-javascript">var a = 1;    // 옛날 방식. 전역 scope라 if/for 안에서 만들어도 밖에서 접근 가능
let b = 2;    // 요즘 방식. 블록 scope
const c = 3;  // 상수. 한 번 정하면 변경 불가

// c = c + 1;  → 에러</code></pre>
<table>
<thead>
<tr>
<th>키워드</th>
<th>scope</th>
<th>재할당</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><code>var</code></td>
<td>함수 전체</td>
<td>가능</td>
<td>레거시 코드에서 많이 보임</td>
</tr>
<tr>
<td><code>let</code></td>
<td>블록 <code>{}</code></td>
<td>가능</td>
<td>일반 변수는 이걸로</td>
</tr>
<tr>
<td><code>const</code></td>
<td>블록 <code>{}</code></td>
<td>불가</td>
<td>값이 바뀌지 않을 때</td>
</tr>
</tbody></table>
<pre><code class="language-javascript">// 타입 변환 주의
var a = &quot;&quot;;
Number(a)   // → 0

a = &quot;1&quot;;
Number(a)   // → 1</code></pre>
<blockquote>
<p>C언어처럼 타입을 엄격하게 선언하지 않아도 되는데,
그래서 오히려 의도치 않은 타입 변환이 생길 수 있다.</p>
</blockquote>
<hr />
<h2 id="3-dom-접근과-조작">3. DOM 접근과 조작</h2>
<p><strong>DOM(Document Object Model)</strong> 이란 HTML 요소를 JS 객체로 다루는 것이다.
JS로 HTML을 직접 건드릴 수 있다.</p>
<h3 id="요소-찾기">요소 찾기</h3>
<pre><code class="language-javascript">var title1 = document.getElementById(&quot;title&quot;);     // id로 찾기
var title2 = document.querySelector(&quot;#title&quot;);     // CSS 선택자로 찾기 (id)
var items  = document.querySelectorAll(&quot;.item&quot;);   // 같은 클래스 전체 찾기</code></pre>
<h3 id="내용-변경">내용 변경</h3>
<pre><code class="language-javascript">title1.innerText  = '텍스트 변경';              // 순수 텍스트만
title1.innerHTML  = '내부 &lt;mark&gt;HTML&lt;/mark&gt; 변경'; // HTML 태그까지 적용</code></pre>
<h3 id="css-스타일-변경">CSS 스타일 변경</h3>
<pre><code class="language-javascript">title1.style.color           = 'blue';
title1.style.fontSize        = '24px';    // 카멜케이스로 작성 (font-size → fontSize)
title1.style.backgroundColor = 'yellow';</code></pre>
<h3 id="클래스-조작">클래스 조작</h3>
<pre><code class="language-javascript">title1.classList.add('red');      // 클래스 추가
title1.classList.remove('red');   // 클래스 제거
title1.classList.toggle('red');   // 있으면 제거, 없으면 추가</code></pre>
<h3 id="속성attribute-변경">속성(attribute) 변경</h3>
<pre><code class="language-javascript">var img = document.getElementById('img');
img.src   = 'bg.jpg';
img.width = '200';</code></pre>
<hr />
<h2 id="4-이벤트-연결">4. 이벤트 연결</h2>
<p>버튼 클릭 같은 사용자 동작에 함수를 연결하는 방법이다.</p>
<pre><code class="language-html">&lt;h1 id=&quot;title&quot;&gt;제목이다&lt;/h1&gt;
&lt;button onclick=&quot;toggleTitle()&quot;&gt;토글&lt;/button&gt;</code></pre>
<pre><code class="language-javascript">function toggleTitle() {
    var title1 = document.getElementById(&quot;title&quot;);
    title1.classList.toggle('red');
}</code></pre>
<p>전체 구조로 보면 이렇다:</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;style&gt;
        .red { color: red; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1 id=&quot;title&quot;&gt;제목이다&lt;/h1&gt;
    &lt;button onclick=&quot;toggleTitle()&quot;&gt;색상 토글&lt;/button&gt;

    &lt;script&gt;
        function toggleTitle() {
            var title1 = document.getElementById(&quot;title&quot;);
            title1.classList.toggle('red');
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<blockquote>
<p>JS 코드는 보통 <code>&lt;body&gt;</code> 맨 아래에 넣는다.
HTML이 전부 로드된 다음에 JS가 실행돼야 요소를 정상적으로 찾을 수 있기 때문이다.</p>
</blockquote>
<hr />
<h2 id="5-삼항-연산자">5. 삼항 연산자</h2>
<pre><code class="language-javascript">// (조건) ? 참일 때 값 : 거짓일 때 값
var result = (num % 2 == 0) ? '짝수' : '홀수';</code></pre>
<p>실제 활용 예시 — 차량 운행 가능 여부:</p>
<pre><code class="language-javascript">var num   = prompt('차 번호를 입력하세요.');
var today = new Date();
var toDate = today.getDate();   // 오늘 날짜 (1~31)

title.innerText = (num % 2 == toDate % 2) ? '운행 가능합니다.' : '오늘은 쉬세요!';</code></pre>
<blockquote>
<p>날짜의 홀짝과 차 번호의 홀짝을 비교하는 방식이다.
<code>new Date()</code>로 현재 날짜/시간 정보를 가져올 수 있다.</p>
</blockquote>
<hr />
<h2 id="6-배열과-주요-메서드">6. 배열과 주요 메서드</h2>
<pre><code class="language-javascript">var arr = [1, 2, 3, 4, 5];

arr.length   // 5 — 배열 길이 (동적으로 바뀜)
arr[1]       // 2
arr[5] = 6   // 끝에 추가됨 → [1, 2, 3, 4, 5, 6]</code></pre>
<h3 id="자주-쓰는-배열-메서드">자주 쓰는 배열 메서드</h3>
<table>
<thead>
<tr>
<th>메서드</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>push()</code></td>
<td>맨 뒤에 추가</td>
<td><code>arr.push(7)</code></td>
</tr>
<tr>
<td><code>pop()</code></td>
<td>맨 뒤 제거</td>
<td><code>arr.pop()</code></td>
</tr>
<tr>
<td><code>shift()</code></td>
<td>맨 앞 제거 후 당기기</td>
<td><code>arr.shift()</code></td>
</tr>
<tr>
<td><code>sort()</code></td>
<td>알파벳/숫자 순 정렬</td>
<td><code>arr.sort()</code></td>
</tr>
<tr>
<td><code>splice(i, n, val)</code></td>
<td>i번째부터 n개 제거 후 val 삽입</td>
<td><code>arr.splice(2, 3, 999)</code></td>
</tr>
</tbody></table>
<h3 id="forin-vs-forof">for...in vs for...of</h3>
<pre><code class="language-javascript">// for...in → 인덱스(index)를 순회
for (i in [1, 2, 3, 4]) {
    console.log(i);  // 0, 1, 2, 3
}

// for...of → 값(value)을 순회
for (i of [1, 2, 3, 4]) {
    console.log(i);  // 1, 2, 3, 4
}</code></pre>
<blockquote>
<p>파이썬의 <code>for i in list</code> 와 비슷해 보이지만 다르다.
JS에서 <code>for...in</code> 은 값이 아닌 인덱스가 나온다. 헷갈리기 쉬운 포인트.</p>
</blockquote>
<hr />
<h2 id="7-응용-복습">7. 응용 복습:)</h2>
<h3 id="문제1-다크모드-토글-버튼">문제1. 다크모드 토글 버튼</h3>
<p>classList.toggle을 응용해서 다크모드 전환 버튼을 만들어 보기!</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;style&gt;
        body { background: white; color: black; transition: 0.3s; }
        body.dark { background: #1e1e1e; color: white; }
        button { padding: 8px 16px; cursor: pointer; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1 id=&quot;title&quot;&gt;오늘의 학습 기록&lt;/h1&gt;
    &lt;button onclick=&quot;toggleDark()&quot;&gt;🌙 다크모드 전환&lt;/button&gt;

    &lt;script&gt;
        function toggleDark() {
            document.body.classList.toggle('dark');
            var btn = document.querySelector('button');
            btn.innerText = document.body.classList.contains('dark')
                ? '☀️ 라이트모드 전환'
                : '🌙 다크모드 전환';
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<blockquote>
<p>버튼 텍스트도 현재 모드에 따라 같이 바뀌게 삼항 연산자로 처리했다.
<code>classList.contains()</code>로 현재 클래스가 있는지 확인할 수 있다.</p>
</blockquote>
<hr />
<h3 id="문제2-간단한-할-일-목록-배열-메서드-응용">문제2. 간단한 할 일 목록 (배열 메서드 응용)</h3>
<p>배열 메서드 <code>push</code>, <code>splice</code>를 직접 DOM과 연결해봤다.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;style&gt;
        li { margin: 4px 0; }
        .done { text-decoration: line-through; color: gray; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;할 일 목록&lt;/h2&gt;
    &lt;input id=&quot;inputTask&quot; type=&quot;text&quot; placeholder=&quot;할 일 입력&quot;&gt;
    &lt;button onclick=&quot;addTask()&quot;&gt;추가&lt;/button&gt;
    &lt;ul id=&quot;taskList&quot;&gt;&lt;/ul&gt;

    &lt;script&gt;
        var tasks = [];

        function addTask() {
            var input = document.getElementById('inputTask');
            var val = input.value.trim();
            if (!val) return;

            tasks.push(val);
            input.value = '';
            renderList();
        }

        function toggleDone(idx) {
            var items = document.querySelectorAll('#taskList li');
            items[idx].classList.toggle('done');
        }

        function deleteTask(idx) {
            tasks.splice(idx, 1);   // 인덱스 idx에서 1개 제거
            renderList();
        }

        function renderList() {
            var list = document.getElementById('taskList');
            list.innerHTML = '';
            for (var i = 0; i &lt; tasks.length; i++) {
                list.innerHTML +=
                    `&lt;li onclick=&quot;toggleDone(${i})&quot;&gt;
                        ${tasks[i]}
                        &lt;button onclick=&quot;event.stopPropagation(); deleteTask(${i})&quot;&gt;삭제&lt;/button&gt;
                    &lt;/li&gt;`;
            }
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<blockquote>
<p><code>splice(idx, 1)</code> 로 선택한 항목만 배열에서 제거하고, <code>renderList()</code>로 화면을 다시 그렸다.
클릭 이벤트가 부모까지 전달되는 걸 막으려면 <code>event.stopPropagation()</code>이 필요하다는 것도 알게 됐다.</p>
</blockquote>
<hr />
<h2 id="8-핵심-정리">8. 핵심 정리</h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td><code>git pull</code></td>
<td>서버 → 내 컴퓨터로 가져오기</td>
</tr>
<tr>
<td><code>git push</code></td>
<td>내 컴퓨터 → 서버로 올리기</td>
</tr>
<tr>
<td><code>sync fork</code></td>
<td>원본 저장소 최신 상태 동기화</td>
</tr>
<tr>
<td><code>var / let / const</code></td>
<td>전역 / 블록 / 상수</td>
</tr>
<tr>
<td><code>getElementById</code></td>
<td>id로 요소 찾기</td>
</tr>
<tr>
<td><code>querySelector</code></td>
<td>CSS 선택자로 요소 찾기</td>
</tr>
<tr>
<td><code>innerText</code></td>
<td>텍스트 내용 변경</td>
</tr>
<tr>
<td><code>innerHTML</code></td>
<td>HTML 태그 포함 내용 변경</td>
</tr>
<tr>
<td><code>style.속성명</code></td>
<td>CSS 직접 변경 (카멜케이스)</td>
</tr>
<tr>
<td><code>classList.toggle</code></td>
<td>클래스 있으면 제거, 없으면 추가</td>
</tr>
<tr>
<td><code>(조건) ? A : B</code></td>
<td>삼항 연산자</td>
</tr>
<tr>
<td><code>for...in</code></td>
<td>인덱스 순회</td>
</tr>
<tr>
<td><code>for...of</code></td>
<td>값 순회</td>
</tr>
<tr>
<td><code>push / pop</code></td>
<td>배열 맨 뒤 추가 / 제거</td>
</tr>
<tr>
<td><code>splice(i, n, val)</code></td>
<td>i번째부터 n개 제거 후 val 삽입</td>
</tr>
</tbody></table>
<hr />
<blockquote>
<p>C랑 파이썬 이후에, JS  문법이 비슷한 것 같으면서도 미묘하게 달라서 은근 헷갈린다.
특히 <code>for...in</code> 이 인덱스를 반환한다는 거, 처음엔 파이썬이랑 똑같은 줄 알았는데 아니었음.
다음 시간엔 반응형 웹으로 미디어 쿼리까지 나간다고 하니까 오늘 열심히 복습 하는 것으로!</p>
</blockquote>