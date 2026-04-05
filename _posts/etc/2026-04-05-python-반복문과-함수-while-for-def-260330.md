---
layout: post
title: "[Python] 반복문과 함수 - while, for, def (260330)"
date: 2026-04-05 15:51:47 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/Python-%EB%B0%98%EB%B3%B5%EB%AC%B8%EA%B3%BC-%ED%95%A8%EC%88%98-while-for-def-260330
---

<p>지난주 파이썬 수업 시간에는 if문이랑 while문 기초를 배웠다면, 오늘은 반복문을 실제로 다루는 법이랑 함수까지 쭉 이어서 배웠다. 양이 꽤 많았지만 차분하게 하나씩 정리하며 복습을 해보려고 한다.
특히, 별탑... 정말 헷갈렸다...
계속 연습을 꾸준히 해나가야할 문제인듯!</p>
<hr />
<h2 id="1-while문--조건이-참인-동안-반복">1. while문 — 조건이 참인 동안 반복</h2>
<pre><code class="language-python">i = 0
while i &lt; 10:
    i += 1
# i가 10이 되면 조건이 거짓이 되어 빠져나옴</code></pre>
<ul>
<li>반복 횟수를 모를 때, <strong>조건</strong>으로 반복을 제어할 때 씀</li>
<li>무한루프에 빠지면 <strong>Ctrl+C</strong> 로 강제 종료</li>
</ul>
<h3 id="break--반복문-탈출">break — 반복문 탈출</h3>
<pre><code class="language-python">while True:
    choice = int(input(&quot;번호 선택(종료:0): &quot;))
    if choice == 0:
        break  # while문 완전 탈출</code></pre>
<ul>
<li><code>while True</code> : 무한루프 의도적으로 만들기</li>
<li><code>break</code> : 가장 가까운 반복문 하나만 탈출 (중첩일 경우 주의!)</li>
<li>프로그램 전체 종료가 필요하면 <code>exit(1)</code> 사용</li>
</ul>
<h3 id="continue--이번-회차만-건너뜀">continue — 이번 회차만 건너뜀</h3>
<pre><code class="language-python">while True:
    n = int(input(&quot;숫자 입력: &quot;))
    if n &lt; 0:
        continue  # 음수면 건너뛰고 다시 입력받기
    print(n)</code></pre>
<ul>
<li><code>continue</code> : 조건식으로 돌아가서 다음 반복 시작</li>
<li><code>break</code>는 탈출, <code>continue</code>는 건너뜀 — 헷갈리지 말기!</li>
</ul>
<hr />
<h2 id="2-for문--반복-횟수를-알-때">2. for문 — 반복 횟수를 알 때</h2>
<pre><code class="language-python">marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark &gt;= 60:
        print(&quot;%d번 학생은 합격입니다.&quot; % number)
    else:
        print(&quot;%d번 학생은 불합격입니다.&quot; % number)</code></pre>
<ul>
<li>리스트 안의 값을 순서대로 꺼내서 <code>mark</code>에 담아 반복</li>
<li><code>mark</code> : 초기 선언이므로 기본값 0에서 시작</li>
</ul>
<h3 id="range--반복-범위-지정">range() — 반복 범위 지정</h3>
<pre><code class="language-python">range(시작, 끝+1, 증가값)</code></pre>
<ul>
<li>증가값이 1이면 생략 가능</li>
<li><code>range(1, 11)</code> → 1부터 10까지</li>
</ul>
<pre><code class="language-python">add = 0  # 전역변수
for i in range(1, 11):  # i는 지역변수
    add = add + i

print(add)  # 들여쓰기 없음 → for문 밖에서 실행 → 55 출력</code></pre>
<blockquote>
<p><strong>전역변수 vs 지역변수</strong></p>
<ul>
<li>전역변수 : 함수/반복문 밖에서 선언, 어디서든 접근 가능</li>
<li>지역변수 : 함수/반복문 안에서만 존재, 밖에서 접근 불가</li>
</ul>
</blockquote>
<hr />
<h2 id="3-이중-for문--구구단-별탑-만들기">3. 이중 for문 — 구구단, 별탑 만들기</h2>
<h3 id="구구단-출력">구구단 출력</h3>
<pre><code class="language-python">for i in range(2, 10):        # 바깥 for문
    for j in range(1, 10):    # 안쪽 for문
        print(i, &quot;*&quot;, j, &quot;=&quot;, i * j, end=&quot; &quot;)
    print('')  # 줄바꿈</code></pre>
<ul>
<li><code>end=&quot; &quot;</code> : 줄바꿈 대신 공백으로 이어붙이기</li>
<li><code>print('')</code> : 안쪽 for 끝나면 줄바꿈</li>
</ul>
<h3 id="별탑-만들기">별탑 만들기</h3>
<pre><code class="language-python"># 윗부분 (커지는 삼각형)
for i in range(1, 16, 2):
    for j in range(16 - i):
        print(&quot; &quot;, end='')    # 공백
    for j in range(i):
        print(&quot;*&quot;, end='')    # 별
    print()

# 아랫부분 (작아지는 삼각형)
for i in range(13, 0, -2):
    for j in range(16 - i):
        print(&quot; &quot;, end='')
    for j in range(i):
        print(&quot;*&quot;, end='')
    print()
</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/de9f6c02-497b-4d96-8d8c-5c05678d3a32/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/94ab485b-c397-44cc-abdd-f84136b340a3/image.png" /></p>
<p><strong>핵심 패턴:</strong></p>
<ul>
<li>공백 수 + 별 수 = 항상 16 (일정하게 유지)</li>
<li><code>range(13, 0, -2)</code> : 13에서 2씩 줄어들면서 반복</li>
</ul>
<hr />
<h2 id="4-실습--자판기-만들기">4. 실습 — 자판기 만들기</h2>
<pre><code class="language-python">money = int(input(&quot;돈 투입: &quot;))
print(f&quot;투입금액: {money}&quot;)

while True:
    print(&quot;[메뉴정보]&quot;)
    print(&quot;1. 콜라 500원\n2. 사이다 400원\n3. 환타 600원&quot;)

    choice = int(input(&quot;번호선택(종료:0): &quot;))

    if choice == 0:
        print(f&quot;잔액 {money}원을 반환합니다.&quot;)
        break

    elif choice == 1:
        if money &gt;= 500:
            money -= 500
            print(f&quot;콜라 구입 완료\n잔액: {money}원&quot;)
        else:
            print(&quot;잔액이 부족합니다!&quot;)

    elif choice == 2:
        if money &gt;= 400:
            money -= 400
            print(f&quot;사이다 구입 완료\n잔액: {money}원&quot;)
        else:
            print(&quot;잔액이 부족합니다!&quot;)

    elif choice == 3:
        if money &gt;= 600:
            money -= 600
            print(f&quot;환타 구입 완료\n잔액: {money}원&quot;)
        else:
            print(&quot;잔액이 부족합니다!&quot;)</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/6d1ed6b7-2c3a-4069-ba13-9555c98dff43/image.png" /></p>
<blockquote>
<p><strong>교수님 말씀:</strong> 처음엔 목표 달성을 목표로 조금 길게 작성해도 된다. 프로세스 단위로 끊어서, 하나씩 이루고 완성하는 걸 만드는 거다!
추가로, if안에 if과 중첩으로 사용되는 것이 가능하다.</p>
</blockquote>
<hr />
<h2 id="5-함수-def--중복-코드를-하나로">5. 함수 (def) — 중복 코드를 하나로</h2>
<pre><code class="language-python">def 함수이름(매개변수):
    return 결과값</code></pre>
<ul>
<li><code>def</code> : 함수를 만들 때 사용하는 예약어</li>
<li><code>return</code> : 함수를 호출한 쪽에 결과값을 돌려줌</li>
</ul>
<h3 id="기본-함수-만들기">기본 함수 만들기</h3>
<pre><code class="language-python">def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)  # add를 호출한 c에 7이 들어감
print(c)       # 7</code></pre>
<h3 id="return-없는-함수">return 없는 함수</h3>
<pre><code class="language-python">def add(a, b):
    print(&quot;%d, %d의 합은 %d입니다.&quot; % (a, b, a + b))

add(3, 4)  # return이 없으므로 출력만 하고 끝</code></pre>
<h3 id="여러-값-리턴하기">여러 값 리턴하기</h3>
<pre><code class="language-python">def add_and_mul(a, b):
    return a + b, a * b

result1, result2 = add_and_mul(3, 4)
print(result1, result2)  # 7 12</code></pre>
<ul>
<li>return 값이 2개 → 튜플로 반환됨</li>
<li>변수 2개로 나눠 받는 것도 가능</li>
</ul>
<h3 id="args--입력값-개수-제한-없이-받기">*args — 입력값 개수 제한 없이 받기</h3>
<pre><code class="language-python">def add_mul(choice, *args):  #choice의 경우 계산을 할지 정하는 값.
    if choice == &quot;add&quot;:
        result = 0
        for i in args:
            result = result + i
    elif choice == &quot;mul&quot;:
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)  # 15</code></pre>
<ul>
<li><code>*args</code> : 개수 상관없이 여러 값을 받을 수 있음</li>
</ul>
<hr />
<h2 id="6-전역변수-vs-지역변수">6. 전역변수 vs 지역변수</h2>
<pre><code class="language-python">a = 1  # 전역변수

def vartest(a):
    a = a + 1  # 지역변수 a (함수 안에서만 존재)

vartest(a)
print(a)  # 1 (전역변수는 그대로!)</code></pre>
<pre><code class="language-python">a = 1  # 전역변수

def vartest(a):
    a = a + 1
    return a  # 지역변수를 리턴해서 밖으로 전달

a = vartest(a)
print(a)  # 2</code></pre>
<pre><code class="language-python">a = 1

def vartest():
    global a  # 전역변수 a를 직접 호출
    a = a + 1

vartest()
print(a)  # 2</code></pre>
<ul>
<li><code>global</code> : 함수 안에서 전역변수를 직접 수정할 때 사용</li>
<li>가능하면 <code>return</code> 으로 값을 전달하는 방식이 더 깔끔함</li>
</ul>
<hr />
<h2 id="7-람다lambda-함수--한-줄짜리-함수">7. 람다(lambda) 함수 — 한 줄짜리 함수</h2>
<pre><code class="language-python"># 일반 함수
def add(a, b):
    return a + b

# 람다 함수 (같은 기능)
add = lambda a, b: a + b   #람다, 매개변수 : 리컨값

result = add(3, 4)
print(result)  # 7</code></pre>
<ul>
<li>간단한 함수를 한 줄로 표현할 때 사용</li>
<li><code>lambda 매개변수 : 리턴값</code> 형식</li>
</ul>
<hr />
<h2 id="8-컴프리헨션comprehension--리스트를-한-줄로">8. 컴프리헨션(Comprehension) — 리스트를 한 줄로</h2>
<pre><code class="language-python"># 일반 방식
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)  # [3, 6, 9, 12]

# 컴프리헨션 방식 (한 줄!)
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)  # [3, 6, 9, 12]</code></pre>
<hr />
<h2 id="9-절차지향-vs-객체지향">9. 절차지향 vs 객체지향</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>특징</th>
<th>대표 언어</th>
</tr>
</thead>
<tbody><tr>
<td>절차지향</td>
<td>위에서 아래로 순서대로 실행</td>
<td>C언어</td>
</tr>
<tr>
<td>객체지향</td>
<td>객체를 만들어 재사용</td>
<td>Python, Java</td>
</tr>
</tbody></table>
<ul>
<li><strong>C언어</strong> : 코드 길고 수정 어렵지만 단순하고 빠름</li>
<li><strong>Python</strong> : 재사용 좋고 수정 용이, 단 호출 순서가 복잡해질 수 있음</li>
</ul>
<hr />
<h2 id="오늘-수업-마무리">오늘 수업 마무리</h2>
<p>오늘 핵심 세 가지를 꼽으라면:</p>
<ol>
<li><strong>break vs continue</strong> 확실히 구분하기 (탈출 vs 건너뜀)</li>
<li><strong>전역변수 vs 지역변수</strong> — <code>global</code> 쓰는 것보다 <code>return</code>으로 값 전달하는 게 더 좋은 코드</li>
<li><strong>람다, 컴프리헨션</strong> — 파이썬스러운 코드 작성법</li>
</ol>
<p>자판기 실습이 가장 재미있었다. while + if + elif 조합으로 실제로 동작하는 걸 만들어보니까 반복문이랑 조건문이 어떻게 맞물려 돌아가는지 확실히 느껴졌다!</p>