---
layout: post
title: "[C언어] 반복문 : for, while, do~while을 언제 써야 할까?"
date: 2026-04-01 13:24:31 +0900
categories: [c-language]
tags: []
velog_url: https://velog.io/@addung/C%EC%96%B8%EC%96%B4-%EB%B0%98%EB%B3%B5%EB%AC%B8-for-while-dowhile%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%8D%A8%EC%95%BC-%ED%95%A0%EA%B9%8C
---

<h4 id="c언어-수업-3주차-20260331">C언어 수업 3주차 (2026.03.31)</h4>
<blockquote>
<p>&quot;코드는 알겠는데... 이 문제에서 왜 for를 쓰고 왜 while을 쓰는 건가요?&quot;</p>
</blockquote>
<p>문법 자체보다 &quot;어떤 상황에서 어떤 반복문을 선택하는가&quot; 를 이해하는 게 핵심이라는 걸 오늘 수업을 통해 깨달았다. 수업시간에 함께 연습해본 예제를 통해서, 간단하게 복습을 기록해 보도록 하겠다. 반복문 많이 헷갈린다.하하...</p>
<h2 id="1-반복문-선택-기준">1. 반복문 선택 기준</h2>
<p>1) 반복이 필요한가?
   └─ NO  → if / else if / else 또는 switch
   └─ YES ↓</p>
<p>2) 반복 횟수가 미리 정해져 있는가?
   └─ YES → for 문
   └─ NO  ↓</p>
<p>3) 루프 시작 전에 조건이 거짓일 수 있는가?
   └─ YES → while 문
   └─ NO  → do~while 문 (최소 1번은 무조건 실행)</p>
<hr />
<h2 id="2-for-문--계획형-반복">2. for 문 — 계획형 반복</h2>
<p><strong>&quot;반복 횟수가 명확할 때&quot;</strong> 사용한다.</p>
<pre><code class="language-c">for (초기화; 조건; 증감) {
    // 반복할 내용
}</code></pre>
<p>초기화, 조건, 증감이 한 줄에 들어가서 코드가 깔끔하다.</p>
<h3 id="예제-구구단-출력">(예제: 구구단 출력)</h3>
<pre><code class="language-c">int i, j; 
for (i = 2; i &lt;= 9; i++) {
    for (j = 1; j &lt;= 9; j++) {
        printf(&quot;%d * %d = %d\n&quot;, i, j, i * j);
    }
    printf(&quot;\n&quot;);
}</code></pre>
<p><strong>포인트:</strong> for 중첩에서는 <code>j</code>를 재초기화할 필요가 없다. <code>for(j=1; ...)</code> 가 매 바깥 루프마다 자동으로 처리해준다. while 중첩에서는 수동으로 <code>j = 1;</code> 을 넣어야 하는 것과 대비된다.</p>
<h3 id="예제-별탑-출력">(예제: 별탑 출력)</h3>
<pre><code class="language-c">int i, j;    //행을 생각하고, 별의 갯수를 생각한다.
for (i = 1; i &lt;= 5; i++) {
    for (j = 1; j &lt;= i; j++) {
        printf(&quot;*&quot;);
    }
    printf(&quot;\n&quot;);
}</code></pre>
<pre><code>*
**
***
****
*****</code></pre><p><strong>핵심 패턴:</strong> 안쪽 조건이 <code>j &lt;= i</code> 인 것이 포인트다. i번째 행에 별이 i개 찍혀야 하기 때문이다.</p>
<hr />
<h2 id="3-while-문--집착형-반복">3. while 문 — 집착형 반복</h2>
<p><strong>&quot;언제 끝날지 모를 때&quot;</strong>, 즉 반복 횟수가 입력이나 조건에 달려 있을 때 사용한다.</p>
<pre><code class="language-c">while (조건) {
    // 반복할 내용
    i++;  // 증감을 직접 써야 한다 — 빠뜨리면 무한루프!
}</code></pre>
<h3 id="예제-입력받은-수의-약수-출력">(예제: 입력받은 수의 약수 출력)</h3>
<pre><code class="language-c">int num, i;
i = 1;
printf(&quot;input number: &quot;);
scanf(&quot;%d&quot;, &amp;num);

if (num &lt;= 0) {
    printf(&quot;please input positive number\n&quot;);
    return 0;
}


while (i &lt;= num) {
    if (num % i == 0)
        printf(&quot;%d &quot;, i);
    i++;
}</code></pre>
<p><strong>핵심 패턴:</strong> <code>num % i == 0</code> 이면 나머지가 0 → 약수. while + if 중첩의 전형적인 패턴이다.</p>
<h3 id="-무한루프--break-패턴예제-입력받는-숫자들의-총합-구하기-단-0입력시에는-종료">-무한루프 + break 패턴(예제: 입력받는 숫자들의 총합 구하기, 단 '0'입력시에는 종료)</h3>
<p>언제 끝날지 모르는 상황에서 자주 쓰는 패턴이다.</p>
<pre><code class="language-c">int n, sum = 0;

while (1) {          // 무한루프
    printf(&quot;input number: &quot;);
    scanf(&quot;%d&quot;, &amp;n);
    if (n == 0)
        break;       // 탈출!
    sum += n;
}
printf(&quot;sum = %d&quot;, sum);</code></pre>
<p><strong>break 위치 주의:</strong> 합산 전에 break 해야 0이 sum에 더해지지 않는다.</p>
<hr />
<h2 id="4-dowhile-문--선실행-반복">4. do~while 문 — 선실행 반복</h2>
<p><strong>&quot;무조건 최소 1번은 실행해야 할 때&quot;</strong> 사용한다. 조건 검사가 루프 끝에 있다.</p>
<pre><code class="language-c">do {
    // 반복할 내용
} while (조건);  // ← 세미콜론 필수!</code></pre>
<h3 id="예제-입력값-범위-검증">(예제: 입력값 범위 검증)</h3>
<pre><code class="language-c">int num;
do {
    printf(&quot;input number(1~9): &quot;);
    scanf(&quot;%d&quot;, &amp;num);
} while (num &lt; 1 || num &gt; 9);

printf(&quot;number is %d&quot;, num);</code></pre>
<p><strong>왜 do~while인가?</strong> 입력을 받는 행동은 무조건 한 번은 해야 한다. while로 구현하면 루프 전에 <code>num</code>을 미리 초기화해야 하는 번거로움이 생기고, <code>scanf</code>가 두 번 반복된다.</p>
<pre><code class="language-c">// while 버전 — scanf가 2번 등장
scanf(&quot;%d&quot;, &amp;num);
while (num &lt; 1 || num &gt; 9) {
    scanf(&quot;%d&quot;, &amp;num);
}

// do~while 버전 — scanf가 1번, 더 깔끔
do {
    scanf(&quot;%d&quot;, &amp;num);
} while (num &lt; 1 || num &gt; 9);</code></pre>
<hr />
<h2 id="5-세-반복문-비교">5. 세 반복문 비교</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>for</th>
<th>while</th>
<th>do~while</th>
</tr>
</thead>
<tbody><tr>
<td>조건 검사 시점</td>
<td>루프 앞 (먼저)</td>
<td>루프 앞 (먼저)</td>
<td>루프 뒤 (나중에)</td>
</tr>
<tr>
<td>0번 실행 가능</td>
<td>O</td>
<td>O</td>
<td>X (최소 1번)</td>
</tr>
<tr>
<td>증감 위치</td>
<td>헤더에 포함</td>
<td>루프 내부에 직접</td>
<td>루프 내부에 직접</td>
</tr>
<tr>
<td>세미콜론</td>
<td>없음</td>
<td>없음</td>
<td><code>while(조건);</code> 필수</td>
</tr>
<tr>
<td>대표 사용처</td>
<td>구구단, 별탑</td>
<td>약수, 0 입력 종료</td>
<td>입력값 검증, 메뉴 선택</td>
</tr>
</tbody></table>
<blockquote>
<p>for와 while은 똑같은 의미이다.
<code>for(i=1; i&lt;=9; i++)</code> = <code>i=1; while(i&lt;=9){ ... i++; }</code>
for가 더 편해서 많이 쓰는 것뿐이고, 둘 다 알아야 한다.</p>
</blockquote>
<hr />
<h2 id="break와-continue">break와 continue</h2>
<h3 id="break--반복문-탈출">break — 반복문 탈출</h3>
<pre><code class="language-c">while (1) {
    scanf(&quot;%d&quot;, &amp;n);
    if (n == 0)
        break;  // 가장 가까운 반복문 하나만 탈출
    sum += n;
}</code></pre>
<p><strong>주의:</strong> 중첩 반복문에서 break는 <strong>가장 가까운 반복문 하나만</strong> 탈출한다. 프로그램 전체를 끝내려면 <code>exit(1)</code> 을 써야 한다.</p>
<h3 id="continue--이번-반복만-건너뜀">continue — 이번 반복만 건너뜀</h3>
<pre><code class="language-c">do {
    scanf(&quot;%d&quot;, &amp;n);
    if (n &lt; 0)
        continue;  // 음수는 건너뛰고 다시 입력받기
    sum += n;
} while (n != 0);</code></pre>
<p><strong>구분 포인트:</strong> continue는 조건식으로 돌아가고, break는 반복문 자체를 탈출한다. 둘 다 반복문 없이 if 단독으로는 사용 불가하다.</p>
<hr />
<h2 id="오늘-겪은-실수들">오늘 겪은 실수들</h2>
<p><strong>1. C언어에서 수학적 범위 표현 안 됨</strong></p>
<pre><code class="language-c">// (X) 파이썬에서는 되지만 C에서는 안 된다
while (1 &lt;= i &lt;= 9)

// (O) 반드시 &amp;&amp; 로 나눠야 한다
while (i &gt;= 1 &amp;&amp; i &lt;= 9)</code></pre>
<p><strong>2. while에서 증감 빠뜨리기</strong></p>
<pre><code class="language-c">// (X) i++ 없으면 무한루프
while (i &lt;= 9) {
    printf(&quot;%d\n&quot;, i);
}

// (O) 증감 필수
while (i &lt;= 9) {
    printf(&quot;%d\n&quot;, i);
    i++;
}</code></pre>
<p><strong>3. for문 헤더에 콤마(,) 쓰기</strong></p>
<pre><code class="language-c">// (X) 콤마가 아니라 세미콜론
for (i = 1; i &lt;= num, i++)

// (O) 세미콜론으로
for (i = 1; i &lt;= num; i++)</code></pre>
<hr />
<h2 id="오늘-수업-마무리내용">오늘 수업 마무리내용</h2>
<p>오늘 수업에서 교수님이 강조한 것은 <strong>문법보다 문제 해결력</strong> 이다. 코드를 외우는 게 아니라 문제를 보고 &quot;반복인가? 횟수가 정해져 있는가? 최소 1번은 실행해야 하는가?&quot; 를 스스로 물어보는 습관이 중요하다!
다양한 예시를 만들어보고, 실행해보는게 중요할 것 같다.
점점 어렵지만, 실제로 구현해 낼 수 있는 것도 많기 때문에 신기하고 재미나기도 한 수업시간.</p>