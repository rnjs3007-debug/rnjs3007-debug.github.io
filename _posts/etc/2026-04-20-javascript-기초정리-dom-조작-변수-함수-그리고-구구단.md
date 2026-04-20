---
layout: post
title: "JavaScript 기초정리 — DOM 조작, 변수, 함수, 그리고 구구단!"
date: 2026-04-20 19:59:15 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/JavaScript-%EA%B8%B0%EC%B4%88%EC%A0%95%EB%A6%AC-DOM-%EC%A1%B0%EC%9E%91-%EB%B3%80%EC%88%98-%ED%95%A8%EC%88%98-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EA%B5%AC%EA%B5%AC%EB%8B%A8
---

<p>260416 javascript 첫수업
<img alt="" src="https://velog.velcdn.com/images/addung/post/fac7c5e9-0c9c-4d39-95bc-3eae9aaaec19/image.png" /></p>
<blockquote>
<p>참고 교재: <a href="https://ko.javascript.info/">모던 JavaScript 튜토리얼</a><br />공식 레퍼런스를 꼭 참고</p>
</blockquote>
<hr />
<h2 id="1-javascript란">1. JavaScript란?</h2>
<p>JavaScript는 <strong>객체 기반의 스크립트 언어</strong>다.<br />이름에 Java가 들어가지만, Java와는 전혀 다른 언어다. 헷갈리지 말자! 드디어 CSS를 뒤로하고 새로 배우는 언어!</p>
<p>웹 브라우저에서 실행되며, HTML의 내용을 <strong>동적으로 변경</strong>하는 데 핵심적인 역할을 한다.</p>
<hr />
<h2 id="2-script-태그-사용법--defer--async">2. script 태그 사용법 &amp; defer / async</h2>
<p>JavaScript 코드는 HTML 파일 안에 <code>&lt;script&gt;</code> 태그로 작성하거나, 외부 <code>.js</code> 파일로 분리해서 불러올 수 있다.</p>
<pre><code class="language-html">&lt;!-- 기본 사용 --&gt;
&lt;script&gt;
  var a = 1;
  var b = 2;
  console.log(a + b); // 3
&lt;/script&gt;</code></pre>
<h3 id="⚠️-script-태그-위치-주의">⚠️ script 태그 위치 주의</h3>
<p><code>&lt;script&gt;</code> 태그를 <code>&lt;head&gt;</code>에 넣으면 HTML이 다 로딩되기 전에 스크립트가 실행되어 오류가 날 수 있다.<br />두 가지 해결 방법이 있다.</p>
<p><strong>방법 1.</strong> <code>&lt;body&gt;</code> 맨 아래에 배치</p>
<p><strong>방법 2.</strong> <code>defer</code> 또는 <code>async</code> 속성 사용 (권장)</p>
<pre><code class="language-html">&lt;script defer src=&quot;main.js&quot;&gt;&lt;/script&gt;</code></pre>
<table>
<thead>
<tr>
<th>속성</th>
<th>동작 방식</th>
</tr>
</thead>
<tbody><tr>
<td><code>defer</code></td>
<td>HTML 파싱 완료 후 순서대로 실행</td>
</tr>
<tr>
<td><code>async</code></td>
<td>HTML 파싱과 병렬로 실행, 순서 보장 안 됨</td>
</tr>
</tbody></table>
<blockquote>
<p>보통은 <code>defer</code>를 사용하자. CSS처럼 외부 파일로 분리하는 게 유지보수에 좋다.</p>
</blockquote>
<hr />
<h2 id="3-dom-조작-기초">3. DOM 조작 기초</h2>
<p><strong>DOM(Document Object Model)</strong>은 HTML 문서를 객체로 표현한 것이다.<br />JavaScript에서 <code>document</code> 객체를 통해 HTML 요소에 접근하고 수정할 수 있다.</p>
<h3 id="getelementbyid로-요소-가져오기">getElementById로 요소 가져오기</h3>
<pre><code class="language-html">&lt;h1 id=&quot;title&quot;&gt;제목&lt;/h1&gt;
&lt;button onclick=&quot;changeTitle('바뀐 제목!')&quot;&gt;클릭&lt;/button&gt;

&lt;script&gt;
  function changeTitle(text) {
    var title = document.getElementById('title');
    title.innerText = text; // 텍스트 내용 변경
  }
&lt;/script&gt;</code></pre>
<h3 id="innertext-vs-innerhtml">innerText vs innerHTML</h3>
<pre><code class="language-javascript">var content = document.getElementById('content');

content.innerText = '&lt;h1&gt;어쩌고&lt;/h1&gt;';  // 태그가 문자로 출력됨
content.innerHTML = '&lt;h1&gt;어쩌고&lt;/h1&gt;';  // 태그가 실제 HTML로 렌더링됨</code></pre>
<h3 id="동적으로-요소-추가하기">동적으로 요소 추가하기</h3>
<pre><code class="language-javascript">function addInput() {
  content.innerHTML += '&lt;div&gt;&lt;input type=&quot;text&quot;&gt;&lt;/div&gt;';
}</code></pre>
<hr />
<h2 id="4-함수와-재사용성">4. 함수와 재사용성</h2>
<p>함수를 잘 설계하면 코드 재사용성이 높아진다.</p>
<h3 id="매개변수로-재사용성-높이기">매개변수로 재사용성 높이기</h3>
<pre><code class="language-html">&lt;!-- 비효율적인 방법 --&gt;
&lt;button onclick=&quot;changeTitle1()&quot;&gt;버튼1&lt;/button&gt;
&lt;button onclick=&quot;changeTitle2()&quot;&gt;버튼2&lt;/button&gt;

&lt;!-- 재사용성 좋은 방법 --&gt;
&lt;button onclick=&quot;changeTitle('큰일났음!')&quot;&gt;버튼1&lt;/button&gt;
&lt;button onclick=&quot;changeTitle('큰일났음2')&quot;&gt;버튼2&lt;/button&gt;
&lt;button onclick=&quot;changeTitle('큰일났음3')&quot;&gt;버튼3&lt;/button&gt;

&lt;script&gt;
  function changeTitle(text) {
    var title = document.getElementById('title');
    title.innerText = text;
  }
&lt;/script&gt;</code></pre>
<p>매개변수를 활용하면 동일한 함수로 다양한 동작을 처리할 수 있다.</p>
<h3 id="즉시-실행-함수-iife">즉시 실행 함수 (IIFE)</h3>
<p>함수명 없이 선언과 동시에 바로 실행하는 패턴이다.<br />전역 스코프 오염을 막을 때 유용하다.</p>
<pre><code class="language-javascript">(function () {
  // 이 안의 코드는 즉시 실행됨
  console.log('즉시 실행!');
})();</code></pre>
<hr />
<h2 id="5-이벤트-활용--스크롤-감지--css-동적-변경">5. 이벤트 활용 — 스크롤 감지 &amp; CSS 동적 변경</h2>
<p>스크롤 위치에 따라 스타일을 바꾸는 예제다.</p>
<pre><code class="language-javascript">function onscroll() {
  console.log(window.scrollY); // 현재 스크롤 위치

  if (window.scrollY &gt; 30) {
    document.body.classList.add('bg');    // 클래스 추가
    img.src = 'bg2.webp';                // 이미지 변경
    title.style.color = 'red';           // CSS 변경
  } else {
    document.body.classList.remove('bg');
    img.src = 'bg.jpg';
    title.style.color = 'blue';
  }
}</code></pre>
<blockquote>
<p><code>window</code>는 브라우저 전역 객체라 생략해도 동작하는 경우가 많다.<br /><code>window.alert('hi')</code> = <code>alert('hi')</code></p>
</blockquote>
<hr />
<h2 id="6-변수와-연산자">6. 변수와 연산자</h2>
<h3 id="변수-선언">변수 선언</h3>
<pre><code class="language-javascript">var a = 1;       // 구형 문법 (함수 스코프)
let b = 2;       // 신형 문법 (블록 스코프, 권장)
const c = 3;     // 상수</code></pre>
<h3 id="타입">타입</h3>
<p>JavaScript의 주요 타입: <code>number</code>, <code>string</code>, <code>boolean</code>, <code>object</code>, <code>undefined</code>, <code>null</code></p>
<pre><code class="language-javascript">Number('2');  // → 2 (명시적 형변환)</code></pre>
<h3 id="⚠️-묵시적-형변환-주의">⚠️ 묵시적 형변환 주의</h3>
<p>JavaScript가 &quot;근본 없는 언어&quot;라는 말을 듣는 이유 중 하나가 바로 <strong>묵시적 형변환</strong> 때문이다.</p>
<pre><code class="language-javascript">'0' == 0   // true  ← 타입을 무시하고 비교
'0' === 0  // false ← 타입까지 엄격하게 비교</code></pre>
<p><strong><code>===</code>(삼중 등호)를 습관적으로 쓰자.</strong> <code>==</code>는 예상치 못한 버그를 만든다.</p>
<table>
<thead>
<tr>
<th>연산자</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><code>==</code></td>
<td>값만 비교 (타입 변환 발생)</td>
</tr>
<tr>
<td><code>===</code></td>
<td>값 + 타입 모두 비교</td>
</tr>
<tr>
<td><code>!==</code></td>
<td>값 또는 타입이 다름</td>
</tr>
</tbody></table>
<h3 id="date-객체">Date 객체</h3>
<pre><code class="language-javascript">var d = new Date();
console.log(d.getFullYear());   // 연도
console.log(d.getMonth() + 1); // 월 (0부터 시작해서 +1 필요!)
console.log(d.getDate());       // 일
console.log(d.getMinutes());    // 분
console.log(d.getSeconds());    // 초</code></pre>
<blockquote>
<p><code>getMonth()</code>는 0부터 시작하는 설계 실수로 유명하다. +1 잊지 말자.</p>
</blockquote>
<hr />
<h2 id="7-입력값-유효성-검사">7. 입력값 유효성 검사</h2>
<p>사용자 입력을 받을 때는 항상 검증이 필요하다.<br />오류 처리에만 집중하면 코드를 짧고 명확하게 짤 수 있다.</p>
<pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;age&quot; placeholder=&quot;나이를 입력하세요&quot;&gt;
&lt;button onclick=&quot;validAge()&quot;&gt;확인&lt;/button&gt;

&lt;script&gt;
  function validAge() {
    var age = document.getElementById('age');
    age = Number(age.value);

    // 숫자 여부 검사
    if (isNaN(age)) {
      alert('숫자로 입력해주세요!');
      return;
    }

    // 음수 여부 검사
    if (age &lt; 0) {
      alert('양수로 입력해주세요.');
      return;
    }

    alert('정상적인 나이입니다!');
  }
&lt;/script&gt;</code></pre>
<blockquote>
<p><code>isNaN()</code> : &quot;is Not a Number&quot;의 약자. 숫자가 아니면 <code>true</code>를 반환한다.</p>
</blockquote>
<hr />
<h2 id="8-실습--구구단-만들기">8. 실습 — 구구단 만들기</h2>
<p>배운 내용을 종합해서 구구단 표를 만들어보자.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;title&gt;구구단&lt;/title&gt;
  &lt;style&gt;
    #gugu {
      width: 60%;
      max-width: 500px;
      margin: 50px auto;
      border-collapse: collapse;
      box-shadow: 1px 2px 10px skyblue;
    }
    #gugu td {
      border: 1px solid rgb(0, 166, 255);
      text-align: center;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;input type=&quot;text&quot; id=&quot;num&quot; placeholder=&quot;단 수 입력&quot;&gt;
  &lt;button onclick=&quot;gugu()&quot;&gt;구구단 생성!&lt;/button&gt;

  &lt;table id=&quot;gugu&quot;&gt;&lt;/table&gt;

  &lt;script&gt;
    function gugu() {
      var num = document.getElementById('num').value;

      if (num === &quot;&quot; || isNaN(num)) {
        alert(&quot;숫자를 입력해주세요!&quot;);
        return;
      }

      var rows = &quot;&quot;;
      for (var i = 1; i &lt; 10; i++) {
        // 방법 1: 문자열 연결
        rows += &quot;&lt;tr&gt;&lt;td&gt;&quot; + num + &quot; x &quot; + i + &quot;&lt;/td&gt;&lt;td&gt;&quot; + (num * i) + &quot;&lt;/td&gt;&lt;/tr&gt;&quot;;

        // 방법 2: 템플릿 리터럴 (백틱 사용, 더 가독성 좋음)
        // rows += `&lt;tr&gt;&lt;td&gt;${num} × ${i}&lt;/td&gt;&lt;td&gt;${num * i}&lt;/td&gt;&lt;/tr&gt;`;
      }

      document.getElementById('gugu').innerHTML = rows;
    }
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;


</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/b0feb9b3-24ef-4805-acba-82783718fc6f/image.png" /></p>
<blockquote>
<p>백틱(<code>`</code>)을 이용한 <strong>템플릿 리터럴</strong>은 문자열 안에 변수를 <code>${변수명}</code> 형태로 넣을 수 있어 가독성이 훨씬 좋다.</p>
</blockquote>
<hr />
<h2 id="오늘-수업-마무리">오늘 수업 마무리</h2>
<p>오늘 수업에서 배운 핵심 내용:</p>
<ul>
<li>HTML을 동적으로 바꾸는 건 <code>document.getElementById()</code>로 요소를 가져와서 <code>innerText</code>, <code>innerHTML</code>, <code>style</code>, <code>classList</code> 등을 조작하면 된다.</li>
<li>함수에 매개변수를 잘 활용하면 재사용성이 높아진다.</li>
<li><code>===</code> 삼중 등호를 습관화하자.</li>
<li><code>defer</code>로 스크립트를 외부 파일로 분리하는 게 좋다.</li>
<li>입력값은 항상 <code>isNaN()</code> 등으로 검증하자.</li>
</ul>