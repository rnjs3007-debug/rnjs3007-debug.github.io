---
layout: post
title: "[Python] tkinter로 GUI 프로그램 만들기"
date: 2026-04-29 14:39:40 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/Python-tkinter%EB%A1%9C-GUI-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%A7%8C%EB%93%A4%EA%B8%B0
---

<blockquote>
<p>260420 수업은 지금까지랑 분위기가 좀 달랐다.
터미널 출력창이 아니라, 진짜 '창(Window)' 이 뜨는 프로그램을 만들었다.
처음으로 내 코드가 프로그램처럼 돌아가는 걸 보니까 확실히 신기하기도 하고, 기본적인 문법사용만 하는 것과는 다른 내용임에 긴장도 많이 했다.</p>
</blockquote>
<hr />
<h2 id="📌-목차">📌 목차</h2>
<ol>
<li><a href="https://v2.velog.io/rss/@addung#%EC%99%B8%EB%B6%80-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC">외부 라이브러리 설치</a></li>
<li><a href="https://v2.velog.io/rss/@addung#tkinter%EB%9E%80">tkinter란?</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EA%B8%B0%EB%B3%B8-%EC%B0%BD">기본 창 띄우기</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9C%84%EC%A0%AF">위젯 종류와 사용법</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%99%80-%EB%B2%84%ED%8A%BC">이미지와 버튼</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%B2%B4%ED%81%AC%EB%B0%95%EC%8A%A4-%EB%9D%BC%EB%94%94%EC%98%A4%EB%B2%84%ED%8A%BC">체크박스 / 라디오버튼</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EB%A9%94%EB%89%B4">메뉴 만들기</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%91%EC%9A%A9-%EC%8B%A4%ED%97%98">응용 실험</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC">핵심 정리</a></li>
</ol>
<hr />
<h2 id="1-외부-라이브러리-설치">1. 외부 라이브러리 설치</h2>
<p>파이썬은 외부 라이브러리 설치가 쉽다는 게 진짜 장점이다.
터미널에 한 줄이면 끝난다.</p>
<pre><code class="language-bash">pip install PyQt5 pandas openpyxl</code></pre>
<pre><code class="language-bash">pip list   # 현재 설치된 라이브러리 목록 확인</code></pre>
<blockquote>
<p>나중에 팀 프로젝트나 실무에서는 <strong>아나콘다(Anaconda)</strong> 같은 환경 관리 도구를 써서
프로젝트마다 필요한 라이브러리 버전을 따로 관리한다고 한다.
지금은 pip로 충분하지만 알아두면 좋을 것 같다.</p>
</blockquote>
<hr />
<h2 id="2-tkinter란">2. tkinter란?</h2>
<p><code>tkinter</code>는 파이썬에 기본으로 내장된 GUI 라이브러리다.
별도 설치 없이 바로 쓸 수 있다는 게 가장 큰 장점이다.</p>
<p><strong>역할을 한마디로 표현하면:</strong></p>
<blockquote>
<p>터미널에서만 돌아가던 파이썬 코드에 <strong>클릭 가능한 창</strong>을 씌워주는 것</p>
</blockquote>
<h3 id="tkinter가-하는-일-3가지">tkinter가 하는 일 3가지</h3>
<p><strong>① 위젯(Widget) 생성</strong>
화면에 보이는 버튼, 텍스트, 입력창 같은 부품들을 만든다.</p>
<p><strong>② 레이아웃 배치</strong></p>
<table>
<thead>
<tr>
<th>방법</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>pack()</code></td>
<td>위에서 아래로 차곡차곡 쌓기</td>
</tr>
<tr>
<td><code>grid()</code></td>
<td>엑셀처럼 행/열 격자로 배치</td>
</tr>
<tr>
<td><code>place()</code></td>
<td>x, y 좌표로 직접 위치 지정</td>
</tr>
</tbody></table>
<p><strong>③ 이벤트 처리</strong>
버튼을 눌렀을 때 어떤 함수가 실행될지 연결해준다.
&quot;로그인 버튼 클릭 → 아이디 확인 함수 실행&quot; 같은 구조다.</p>
<hr />
<h2 id="3-기본-창-띄우기">3. 기본 창 띄우기</h2>
<pre><code class="language-python">from tkinter import *

window = Tk()           # 작업 창(window) 생성
window.mainloop()       # 창이 닫힐 때까지 대기</code></pre>
<table>
<thead>
<tr>
<th>단계</th>
<th>코드</th>
<th>역할</th>
</tr>
</thead>
<tbody><tr>
<td>준비</td>
<td><code>from tkinter import *</code></td>
<td>도구들 불러오기</td>
</tr>
<tr>
<td>생성</td>
<td><code>window = Tk()</code></td>
<td>빈 창 만들기</td>
</tr>
<tr>
<td>유지</td>
<td><code>window.mainloop()</code></td>
<td>창 계속 띄워두기</td>
</tr>
</tbody></table>
<hr />
<h2 id="4-위젯-종류와-사용법">4. 위젯 종류와 사용법</h2>
<h3 id="label--텍스트-표시">Label — 텍스트 표시</h3>
<pre><code class="language-python">from tkinter import *
window = Tk()

label1 = Label(window, text=&quot;COOKBOOK, 데이터분석을&quot;)
label2 = Label(window, text=&quot;열심히&quot;, font=(&quot;궁서체&quot;, 30), fg=&quot;blue&quot;)
label3 = Label(window, text=&quot;공부 중입니다.&quot;, bg=&quot;magenta&quot;, width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()</code></pre>
<p>자주 쓰는 옵션들:</p>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>text</code></td>
<td>표시할 텍스트</td>
<td><code>text=&quot;안녕&quot;</code></td>
</tr>
<tr>
<td><code>font</code></td>
<td>글꼴, 크기</td>
<td><code>font=(&quot;궁서체&quot;, 30)</code></td>
</tr>
<tr>
<td><code>fg</code></td>
<td>글자색</td>
<td><code>fg=&quot;blue&quot;</code></td>
</tr>
<tr>
<td><code>bg</code></td>
<td>배경색</td>
<td><code>bg=&quot;magenta&quot;</code></td>
</tr>
<tr>
<td><code>width/height</code></td>
<td>크기</td>
<td><code>width=20, height=5</code></td>
</tr>
<tr>
<td><code>anchor</code></td>
<td>텍스트 정렬 위치</td>
<td><code>anchor=SE</code> (오른쪽 아래)</td>
</tr>
</tbody></table>
<hr />
<h2 id="5-이미지와-버튼">5. 이미지와 버튼</h2>
<h3 id="1-이미지-불러오기">1) 이미지 불러오기</h3>
<pre><code class="language-python"># 절대경로
photo = PhotoImage(file=&quot;C:/python/source/GIF/dog.gif&quot;)

# 상대경로 (현재 폴더 기준)
photo = PhotoImage(file=&quot;source/GIF/dog.gif&quot;)</code></pre>
<blockquote>
<p>⚠️ 파일 경로에 한글 폴더명이 있으면 오류날 수 있다. 영문 경로 사용을 권장한다.</p>
</blockquote>
<pre><code class="language-python">label1 = Label(window, image=photo)
label2 = Label(window, image=photo)

label1.pack(side=LEFT)   # 왼쪽으로 나란히 배치
label2.pack(side=LEFT)</code></pre>
<h3 id="2-버튼--이벤트-연결">2) 버튼 + 이벤트 연결</h3>
<pre><code class="language-python">from tkinter import *
from tkinter import messagebox   # 팝업창은 따로 import 필요!

def myFunc():
    messagebox.showinfo(&quot;강아지 버튼&quot;, &quot;강아지가 귀엽죠?&quot;)

window = Tk()

photo = PhotoImage(file=&quot;source/GIF/dog.gif&quot;)
button1 = Button(window, image=photo, command=myFunc)  # command로 함수 연결
button1.pack()

window.mainloop()</code></pre>
<blockquote>
<p><code>command=myFunc</code> 에서 괄호를 쓰지 않는다.
<code>myFunc()</code> 라고 쓰면 창이 뜨는 순간 바로 실행돼버린다.</p>
</blockquote>
<hr />
<h2 id="6-체크박스--라디오버튼">6. 체크박스 / 라디오버튼</h2>
<h3 id="1-체크박스">1) 체크박스</h3>
<pre><code class="language-python">from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    if chk.get() == 0:
        messagebox.showinfo(&quot;&quot;, &quot;체크버튼이 꺼졌어요&quot;)
    else:
        messagebox.showinfo(&quot;&quot;, &quot;체크버튼이 켜졌어요&quot;)

chk = IntVar()   # tkinter 전용 정수형 변수 — 체크 상태를 실시간 저장
cb1 = Checkbutton(window, text=&quot;클릭하세요&quot;, variable=chk, command=myFunc)
cb1.pack()

window.mainloop()</code></pre>
<h3 id="2-라디오버튼">2) 라디오버튼</h3>
<pre><code class="language-python">from tkinter import *

window = Tk()

def myFunc():
    if var.get() == 1:
        label1.configure(text=&quot;파이썬&quot;)
    elif var.get() == 2:
        label1.configure(text=&quot;C++&quot;)
    else:
        label1.configure(text=&quot;Java&quot;)

var = IntVar()   # 선택된 라디오버튼의 value 값이 여기 저장됨
rb1 = Radiobutton(window, text=&quot;파이썬&quot;, variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text=&quot;C++&quot;,   variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text=&quot;Java&quot;,  variable=var, value=3, command=myFunc)

label1 = Label(window, text=&quot;선택한 언어: &quot;, fg=&quot;red&quot;)

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()</code></pre>
<p>** 체크박스 vs 라디오버튼 차이:**</p>
<table>
<thead>
<tr>
<th>위젯</th>
<th>특징</th>
<th>사용 예</th>
</tr>
</thead>
<tbody><tr>
<td><code>Checkbutton</code></td>
<td>각각 독립적으로 on/off</td>
<td>동의 여부, 옵션 선택</td>
</tr>
<tr>
<td><code>Radiobutton</code></td>
<td>하나만 선택 가능</td>
<td>성별, 언어 선택</td>
</tr>
</tbody></table>
<blockquote>
<p><code>IntVar()</code> 는 tkinter 전용 변수다.
파이썬 일반 변수(<code>int a = 0</code>)와 다르게 위젯과 <strong>실시간으로 연동</strong>된다.</p>
</blockquote>
<hr />
<h2 id="7-메뉴-만들기">7. 메뉴 만들기</h2>
<p>메뉴는 <strong>상위 메뉴 → 하위 메뉴</strong> 구조로 구성한다.</p>
<pre><code class="language-python">from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)   # 창에 메뉴바 붙이기

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label=&quot;파일&quot;, menu=fileMenu)   # 상위 메뉴에 파일 추가
fileMenu.add_command(label=&quot;열기&quot;)
fileMenu.add_separator()                             # 구분선
fileMenu.add_command(label=&quot;저장&quot;)
fileMenu.add_command(label=&quot;종료&quot;)

window.mainloop()</code></pre>
<pre><code>창 구조:
┌─────────────────────┐
│ [파일]               │  ← mainMenu
├─────────────────────┤
│   열기               │  ← fileMenu
│   ─────────         │  ← separator
│   저장               │
│   종료               │
└─────────────────────┘</code></pre><blockquote>
<p>기능이 많아지면 메뉴 코드도 함수로 분리해서 관리하는 게 좋다.</p>
</blockquote>
<hr />
<h2 id="8-응용-연습">8. 응용 연습</h2>
<h3 id="문제1-간단한-계산기-gui">문제1. 간단한 계산기 GUI</h3>
<p>수업에서 배운 <code>Entry</code>(입력창)와 <code>Button</code>을 조합해 덧셈 계산기를 만들어봤다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(&quot;간단 계산기&quot;)

def calculate():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result_label.configure(text=f&quot;결과: {num1 + num2}&quot;)
    except ValueError:
        messagebox.showerror(&quot;오류&quot;, &quot;숫자만 입력해주세요!&quot;)

Label(window, text=&quot;첫 번째 숫자:&quot;).pack()
entry1 = Entry(window)
entry1.pack()

Label(window, text=&quot;두 번째 숫자:&quot;).pack()
entry2 = Entry(window)
entry2.pack()

Button(window, text=&quot;더하기&quot;, command=calculate, bg=&quot;skyblue&quot;).pack(pady=5)
result_label = Label(window, text=&quot;결과: &quot;, fg=&quot;red&quot;, font=(&quot;Arial&quot;, 14))
result_label.pack()

window.mainloop()</code></pre>
<blockquote>
<p><code>Entry</code> 위젯으로 사용자 입력을 받고, <code>label.configure()</code>로 결과를 실시간 갱신했다.
예외처리까지 붙이니까 숫자가 아닌 입력도 안전하게 처리할 수 있었다.</p>
</blockquote>
<hr />
<h3 id="문제-2-grid-레이아웃으로-로그인-화면-구성">문제 2. grid() 레이아웃으로 로그인 화면 구성</h3>
<p><code>pack()</code> 대신 <code>grid()</code>를 써서 정렬된 레이아웃을 만들어봤다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(&quot;로그인&quot;)
window.geometry(&quot;300x150&quot;)   # 창 크기 고정

def login():
    id_val = entry_id.get()
    pw_val = entry_pw.get()
    if id_val == &quot;admin&quot; and pw_val == &quot;1234&quot;:
        messagebox.showinfo(&quot;성공&quot;, &quot;로그인 성공!&quot;)
    else:
        messagebox.showerror(&quot;실패&quot;, &quot;아이디 또는 비밀번호가 틀렸습니다.&quot;)

Label(window, text=&quot;아이디:&quot;).grid(row=0, column=0, padx=10, pady=10)
entry_id = Entry(window)
entry_id.grid(row=0, column=1)

Label(window, text=&quot;비밀번호:&quot;).grid(row=1, column=0, padx=10)
entry_pw = Entry(window, show=&quot;*&quot;)   # 입력값을 *로 가리기
entry_pw.grid(row=1, column=1)

Button(window, text=&quot;로그인&quot;, command=login, width=15).grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()</code></pre>
<pre><code>화면 구조 (grid):
         column=0    column=1
row=0  [ 아이디:  ][ 입력칸    ]
row=1  [ 비밀번호:][ ****      ]
row=2  [    로그인 버튼 (2칸 차지)    ]</code></pre><blockquote>
<p><code>grid()</code>를 쓰면 <code>pack()</code>보다 정렬이 훨씬 깔끔하게 잡힌다.
<code>columnspan=2</code> 옵션으로 버튼이 두 칸을 차지하게 만들 수 있었다.</p>
</blockquote>
<hr />
<h2 id="9-핵심-정리-📋">9. 핵심 정리 📋</h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td><code>from tkinter import *</code></td>
<td>tkinter 전체 불러오기</td>
</tr>
<tr>
<td><code>messagebox</code></td>
<td>팝업창. <code>*</code>와 별개로 따로 import 필요</td>
</tr>
<tr>
<td><code>Tk()</code></td>
<td>메인 창 객체 생성</td>
</tr>
<tr>
<td><code>mainloop()</code></td>
<td>창 유지 (이벤트 대기 루프)</td>
</tr>
<tr>
<td><code>Label</code></td>
<td>텍스트/이미지 표시</td>
</tr>
<tr>
<td><code>Button</code></td>
<td>클릭 버튼. <code>command</code>로 함수 연결</td>
</tr>
<tr>
<td><code>Entry</code></td>
<td>텍스트 입력창. <code>.get()</code>으로 값 가져옴</td>
</tr>
<tr>
<td><code>Checkbutton</code></td>
<td>독립 체크박스</td>
</tr>
<tr>
<td><code>Radiobutton</code></td>
<td>단일 선택 버튼</td>
</tr>
<tr>
<td><code>IntVar()</code></td>
<td>위젯과 실시간 연동되는 tkinter 전용 변수</td>
</tr>
<tr>
<td><code>pack()</code></td>
<td>순서대로 쌓기</td>
</tr>
<tr>
<td><code>grid()</code></td>
<td>행/열 격자 배치</td>
</tr>
<tr>
<td><code>place()</code></td>
<td>x, y 좌표로 직접 배치</td>
</tr>
<tr>
<td><code>configure()</code></td>
<td>위젯 속성 실시간 변경</td>
</tr>
<tr>
<td><code>PhotoImage</code></td>
<td>gif 이미지 불러오기 (영문 경로 권장)</td>
</tr>
<tr>
<td><code>command=func</code></td>
<td>함수 연결 시 괄호 없이 이름만 전달</td>
</tr>
</tbody></table>
<hr />
<blockquote>
<p>터미널 출력에서 벗어나서 실제 창이 뜨는 프로그램을 만드니까 체감이 달랐다.
위젯 하나하나는 단순하지만, 이걸 조합하면 꽤 그럴듯한 프로그램이 나옴을 알 수 있었다.
다음엔 메뉴 + 파일 입출력을 연결해서 실용적인 툴을 만들어볼 예정이다. 
지금부터 배우는 내용이 프로젝트에서 사용될 기술들과 직접적으로 연동됨에 복습을 꾸준히 해야함을 느끼는중!</p>
</blockquote>