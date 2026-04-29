---
layout: post
title: "[Python] tkinter 파일 다루기, 이미지 처리, CSV 읽기"
date: 2026-04-29 14:55:42 +0900
categories: [etc]
tags: []
velog_url: https://velog.io/@addung/Python-tkinter-%ED%8C%8C%EC%9D%BC-%EB%8B%A4%EB%A3%A8%EA%B8%B0-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC-CSV-%EC%9D%BD%EA%B8%B0
---

<blockquote>
<p>260427 수업기록
저번 시간에 기본 위젯들을 배웠다면 이번엔 좀 더 실용적인 내용이었다.
파일을 직접 열고 저장하는 창을 띄우고, 이미지를 픽셀 단위로 처리하고, CSV 파일까지 읽어봤다.
코드가 점점 길어지는데 구조를 잘 나눠서 짜는 게 얼마나 중요한지를 훨씬더 크게 느끼게 되었다.</p>
</blockquote>
<hr />
<h2 id="목차">목차</h2>
<ol>
<li><a href="https://v2.velog.io/rss/@addung#%EB%A9%94%EB%89%B4-%EC%9D%B4%EB%B2%A4%ED%8A%B8">메뉴 + 이벤트 연결</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EB%8B%A4%EC%9D%B4%EC%96%BC%EB%A1%9C%EA%B7%B8">다이얼로그 창 종류</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B7%B0%EC%96%B4">이미지 뷰어 만들기</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%ED%9D%91%EB%B0%B1-%EB%B3%80%ED%99%98">흑백 변환 — 픽셀 처리</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%B4%EC%A7%84-%ED%8C%8C%EC%9D%BC">이진 파일과 RAW 이미지</a></li>
<li><a href="https://v2.velog.io/rss/@addung#csv">CSV 파일 읽기</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%EC%9D%91%EC%9A%A9-%EC%8B%A4%ED%97%98">응용 실험</a></li>
<li><a href="https://v2.velog.io/rss/@addung#%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC">핵심 정리</a></li>
</ol>
<hr />
<h2 id="1-메뉴--이벤트-연결">1. 메뉴 + 이벤트 연결</h2>
<p>저번에 메뉴 구조만 만들었다면, 이번엔 실제 기능을 붙였다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo(&quot;메뉴선택&quot;, &quot;열기 메뉴를 선택함&quot;)

def func_exit():
    window.quit()      # 메인 루프 종료
    window.destroy()   # 창 닫고 메모리 해제

window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label=&quot;파일&quot;, menu=fileMenu)
mainMenu.add_command(label=&quot;열기&quot;, command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label=&quot;종료&quot;, command=func_exit)

window.mainloop()</code></pre>
<blockquote>
<p><code>window.quit()</code> 과 <code>window.destroy()</code> 를 같이 써야 완전히 종료된다.
<code>quit()</code>만 쓰면 루프는 끝나도 창이 남아있는 경우가 생긴다.</p>
</blockquote>
<hr />
<h2 id="2-다이얼로그-창-종류">2. 다이얼로그 창 종류</h2>
<p><code>tkinter</code>에는 사용자 입력을 받거나 파일을 고르는 팝업 창이 내장돼있다.</p>
<h3 id="1-숫자-입력-다이얼로그">1) 숫자 입력 다이얼로그</h3>
<pre><code class="language-python">from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry(&quot;400x100&quot;)

Label1 = Label(window, text=&quot;입력된 값&quot;)
Label1.pack()

value = askinteger(&quot;확대배수&quot;, &quot;주사위 숫자(1~6)를 입력하세요&quot;, minvalue=1, maxvalue=6)

Label1.configure(text=str(value))  # 숫자 → 문자열 변환 후 라벨에 표시
window.mainloop()</code></pre>
<blockquote>
<p><code>askinteger()</code>는 숫자가 아닌 값을 입력하면 자동으로 걸러준다.
범위를 벗어난 값도 재입력을 유도한다.</p>
</blockquote>
<h3 id="2-파일-열기-다이얼로그">2) 파일 열기 다이얼로그</h3>
<pre><code class="language-python">from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry(&quot;400x100&quot;)

Label1 = Label(window, text=&quot;선택된 파일 이름&quot;)
Label1.pack()

filename = askopenfilename(
    parent=window,
    filetypes=(
        (&quot;GIF 파일&quot;, &quot;*.gif&quot;),
        (&quot;모든파일&quot;, &quot;*.*&quot;)
    )
)

Label1.configure(text=str(filename))
window.mainloop()</code></pre>
<h3 id="3-파일-저장-다이얼로그">3) 파일 저장 다이얼로그</h3>
<pre><code class="language-python">saveFp = asksaveasfile(
    parent=window,
    mode=&quot;w&quot;,                  # 쓰기(write) 모드
    defaultextension=&quot;.jpg&quot;,   # 확장자 미입력 시 자동으로 .jpg 붙여줌
    filetypes=((&quot;JPG파일&quot;, &quot;*.jpg;*.jpeg&quot;), (&quot;모든파일&quot;, &quot;*.*&quot;))
)

Label1.configure(text=saveFp)
saveFp.close()   # 파일 객체는 반드시 닫아줘야 함</code></pre>
<table>
<thead>
<tr>
<th>함수</th>
<th>역할</th>
</tr>
</thead>
<tbody><tr>
<td><code>askinteger()</code></td>
<td>정수 입력 팝업</td>
</tr>
<tr>
<td><code>askopenfilename()</code></td>
<td>파일 열기 창 → 경로 반환</td>
</tr>
<tr>
<td><code>asksaveasfile()</code></td>
<td>파일 저장 창 → 파일 객체 반환</td>
</tr>
</tbody></table>
<hr />
<h2 id="3-이미지-뷰어-만들기">3. 이미지 뷰어 만들기</h2>
<p>파일 열기 다이얼로그와 메뉴를 조합해서 GIF 이미지를 불러오는 뷰어를 만들었다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter.filedialog import *

def func_open():
    filename = askopenfilename(parent=window, filetypes=((&quot;GIF 파일&quot;, &quot;*.gif&quot;), (&quot;모든 파일&quot;, &quot;*.*&quot;)))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo   # 가비지 컬렉션 방지 — 이 줄 없으면 이미지가 사라짐

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry(&quot;500x500&quot;)
window.title(&quot;명화 감상하기&quot;)

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label=&quot;파일&quot;, menu=fileMenu)
fileMenu.add_command(label=&quot;파일열기&quot;, command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label=&quot;프로그램 종료&quot;, command=func_exit)

window.mainloop()</code></pre>
<blockquote>
<p><code>pLabel.image = photo</code> 이 줄이 없으면 함수가 끝나는 순간 이미지가 메모리에서 사라진다.
파이썬의 가비지 컬렉션이 참조가 없는 객체를 지워버리기 때문이다.</p>
</blockquote>
<hr />
<h2 id="4-흑백-변환--픽셀-처리">4. 흑백 변환 — 픽셀 처리</h2>
<p>이미지를 불러온 뒤 픽셀 하나하나를 직접 수정해서 흑백으로 만들었다.</p>
<pre><code class="language-python">def convert_to_grey(photo_obj):
    w = photo_obj.width()
    h = photo_obj.height()

    for y in range(h):
        for x in range(w):
            r, g, b = photo_obj.get(x, y)    # (x, y) 픽셀의 RGB 값 가져오기
            grey = (r + g + b) // 3           # 평균값으로 회색 계산
            hex_color = &quot;#%02x%02x%02x&quot; % (grey, grey, grey)
            photo_obj.put(hex_color, (x, y))  # 변환된 색상을 픽셀에 덮어씀</code></pre>
<pre><code class="language-python">def func_open():
    filename = askopenfilename(parent=window, filetypes=((&quot;GIF 파일&quot;, &quot;*.gif&quot;), (&quot;모든 파일&quot;, &quot;*.*&quot;)))
    photo = PhotoImage(file=filename)
    convert_to_grey(photo)   # 불러온 직후 흑백 변환
    pLabel.configure(image=photo)
    pLabel.image = photo</code></pre>
<p><strong>흑백 변환 원리:</strong></p>
<pre><code>RGB(255, 100, 50) → grey = (255 + 100 + 50) // 3 = 135
→ RGB(135, 135, 135) → 회색</code></pre><p>R, G, B 세 값을 평균 내서 셋 다 같은 값으로 만들면 회색이 된다.
이 방식을 <strong>평균법(Average method)</strong> 이라고 한다.</p>
<blockquote>
<p>이미지 크기가 클수록 처리할 픽셀 수가 늘어나서 속도가 느려진다.
영상처리의 기초 개념을 직접 구현해보는 경험이었다.</p>
</blockquote>
<hr />
<h2 id="5-이진-파일과-raw-이미지">5. 이진 파일과 RAW 이미지</h2>
<p>GIF 같은 포맷이 아니라 픽셀 밝기값 그 자체만 담긴 <strong>RAW 파일</strong>을 읽었다.
압축이나 헤더 없이 0~255 사이 숫자가 픽셀 순서대로 나열된 파일이다.</p>
<pre><code class="language-python">def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')           # 'rb' = 이진(binary) 읽기 모드

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))  # 1바이트씩 읽어서 숫자(0~255)로 변환
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()                        # 루프 밖에서 닫아야 함

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = &quot;&quot;
    for i in range(0, XSIZE):
        tmpString = &quot;&quot;
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += &quot;#%02x%02x%02x &quot; % (data, data, data)  # 흑백이라 R=G=B
        rgbString += &quot;{&quot; + tmpString + &quot;} &quot;
    paper.put(rgbString)              # 전체 RGB 문자열을 한 번에 입력

XSIZE, YSIZE = 256, 256
inImage = []

window = Tk()
window.title(&quot;흑백 사진 보기&quot;)

canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state=&quot;normal&quot;)

filename = 'C:/python/source/RAW/tree.raw'
loadImage(filename)
displayImage(inImage)

canvas.pack()
window.mainloop()</code></pre>
<pre><code>RAW 파일 구조:
[0행 0열 밝기] [0행 1열 밝기] ... [0행 255열 밝기]
[1행 0열 밝기] ...
총 256 × 256 = 65,536 바이트 (각 픽셀 = 1바이트)</code></pre><blockquote>
<p>나중에 배울 필터 적용, 엣지 검출 같은 기능도 이 구조에서 수학 연산을 더하는 방식이라고 한다.</p>
</blockquote>
<hr />
<h2 id="6-csv-파일-읽기">6. CSV 파일 읽기</h2>
<p>CSV는 콤마(<code>,</code>)로 값을 구분하는 텍스트 파일이다.
엑셀에서도 열리고 메모장으로도 열린다.</p>
<pre><code class="language-python">def printList(pList):
    for data in pList:
        print(data, end='\t')   # 탭 간격으로 가로 출력
    print()

with open(&quot;C:/python/source/CSV/singer1.csv&quot;, &quot;r&quot;) as inFp:
    header = inFp.readline()        # 첫 줄(헤더) 따로 읽기
    header = header.strip()         # 줄끝 \n 제거
    header_list = header.split(',') # 쉼표 기준으로 쪼개기
    printList(header_list)

    for inStr in inFp:              # 두 번째 줄부터 끝까지
        inStr = inStr.strip()
        row_list = inStr.split(',')
        printList(row_list)</code></pre>
<p><strong>핵심 함수 3개:</strong></p>
<table>
<thead>
<tr>
<th>함수</th>
<th>역할</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><code>strip()</code></td>
<td>양끝 공백/줄바꿈 제거</td>
<td><code>&quot;아이유\n&quot;</code> → <code>&quot;아이유&quot;</code></td>
</tr>
<tr>
<td><code>split(',')</code></td>
<td>구분자로 문자열 쪼개기</td>
<td><code>&quot;아이유,여자&quot;</code> → <code>['아이유', '여자']</code></td>
</tr>
<tr>
<td><code>readline()</code></td>
<td>파일에서 한 줄만 읽기</td>
<td>헤더 따로 처리할 때 사용</td>
</tr>
</tbody></table>
<pre><code>singer1.csv 내용:
이름,성별,활동유형
아이유,여자,솔로
BTS,남자,그룹

출력 결과:
이름    성별    활동유형
아이유  여자    솔로
BTS    남자    그룹</code></pre><hr />
<h2 id="7-응용-복습직접-만들어-보는-복습-문제들">7. 응용 복습(직접 만들어 보는 복습 문제들)</h2>
<h3 id="문제-1-컬러--흑백-선택해서-열기">문제 1. 컬러 / 흑백 선택해서 열기</h3>
<p>메뉴에 컬러와 흑백 두 가지 열기 옵션을 따로 만들었다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter.filedialog import *

def convert_to_grey(photo_obj):
    w, h = photo_obj.width(), photo_obj.height()
    for y in range(h):
        for x in range(w):
            r, g, b = photo_obj.get(x, y)
            grey = (r + g + b) // 3
            photo_obj.put(&quot;#%02x%02x%02x&quot; % (grey, grey, grey), (x, y))

def func_open_color():
    filename = askopenfilename(parent=window, filetypes=((&quot;GIF 파일&quot;, &quot;*.gif&quot;), (&quot;모든 파일&quot;, &quot;*.*&quot;)))
    if not filename:
        return
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo
    window.title(f&quot;이미지 뷰어 — 컬러: {filename.split('/')[-1]}&quot;)

def func_open_grey():
    filename = askopenfilename(parent=window, filetypes=((&quot;GIF 파일&quot;, &quot;*.gif&quot;), (&quot;모든 파일&quot;, &quot;*.*&quot;)))
    if not filename:
        return
    photo = PhotoImage(file=filename)
    convert_to_grey(photo)
    pLabel.configure(image=photo)
    pLabel.image = photo
    window.title(f&quot;이미지 뷰어 — 흑백: {filename.split('/')[-1]}&quot;)

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry(&quot;520x560&quot;)
window.title(&quot;이미지 뷰어&quot;)

photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

btnFrame = Frame(window)
btnFrame.pack()
Button(btnFrame, text=&quot;컬러로 열기&quot;, command=func_open_color, width=15).pack(side=LEFT, padx=5, pady=5)
Button(btnFrame, text=&quot;흑백으로 열기&quot;, command=func_open_grey, width=15).pack(side=LEFT, padx=5, pady=5)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label=&quot;파일&quot;, menu=fileMenu)
fileMenu.add_command(label=&quot;컬러로 열기&quot;, command=func_open_color)
fileMenu.add_command(label=&quot;흑백으로 열기&quot;, command=func_open_grey)
fileMenu.add_separator()
fileMenu.add_command(label=&quot;종료&quot;, command=func_exit)

window.mainloop()</code></pre>
<blockquote>
<p>파일 이름을 창 제목에 표시하게 했더니 어떤 파일이 열려있는지 한눈에 확인됐다.
기능을 함수로 분리했더니 메뉴와 버튼 양쪽에서 동일한 코드를 재사용할 수 있었다.</p>
</blockquote>
<hr />
<h3 id="문제-2-csv-파일을-gui-창에-테이블로-표시하기">문제 2. CSV 파일을 GUI 창에 테이블로 표시하기</h3>
<p>터미널 출력 대신 tkinter 창 안에 표 형태로 띄워봤다.</p>
<pre><code class="language-python">from tkinter import *
from tkinter.filedialog import *

def load_csv(filepath):
    rows = []
    with open(filepath, &quot;r&quot;, encoding=&quot;utf-8-sig&quot;) as f:
        for line in f:
            row = line.strip().split(',')
            rows.append(row)
    return rows

def show_csv():
    filename = askopenfilename(filetypes=((&quot;CSV 파일&quot;, &quot;*.csv&quot;), (&quot;모든파일&quot;, &quot;*.*&quot;)))
    if not filename:
        return
    rows = load_csv(filename)
    for widget in tableFrame.winfo_children():
        widget.destroy()   # 이전 내용 초기화
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            bg = &quot;#d0e8ff&quot; if r_idx == 0 else &quot;white&quot;
            Label(tableFrame, text=val, relief=&quot;solid&quot;, width=12,
                  bg=bg, font=(&quot;Arial&quot;, 9)).grid(row=r_idx, column=c_idx, padx=1, pady=1)

window = Tk()
window.title(&quot;CSV 뷰어&quot;)

Button(window, text=&quot;CSV 파일 열기&quot;, command=show_csv).pack(pady=5)

tableFrame = Frame(window)
tableFrame.pack(padx=10, pady=5)

window.mainloop()</code></pre>
<pre><code>실행 결과 (창에 격자 형태로 표시):
┌──────────┬──────┬──────────┐
│  이름    │ 성별 │ 활동유형 │  ← 파란 배경 (헤더)
├──────────┼──────┼──────────┤
│  아이유  │ 여자 │  솔로    │
│  BTS     │ 남자 │  그룹    │
└──────────┴──────┴──────────┘</code></pre><blockquote>
<p>헤더 행만 배경색을 다르게 주니까 가독성이 확 올라갔다.
<code>grid()</code> 레이아웃을 쓰니까 열 정렬도 자동으로 맞춰졌다.</p>
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
<td><code>messagebox.showinfo()</code></td>
<td>정보 팝업창</td>
</tr>
<tr>
<td><code>window.quit()</code> + <code>destroy()</code></td>
<td>완전 종료. 둘 다 써야 함</td>
</tr>
<tr>
<td><code>askinteger()</code></td>
<td>숫자 입력 다이얼로그</td>
</tr>
<tr>
<td><code>askopenfilename()</code></td>
<td>파일 열기 창 → 경로(str) 반환</td>
</tr>
<tr>
<td><code>asksaveasfile()</code></td>
<td>파일 저장 창 → 파일 객체 반환</td>
</tr>
<tr>
<td><code>pLabel.image = photo</code></td>
<td>가비지 컬렉션 방지 필수</td>
</tr>
<tr>
<td><code>photo.get(x, y)</code></td>
<td>픽셀 RGB 값 가져오기</td>
</tr>
<tr>
<td><code>photo.put(color, (x,y))</code></td>
<td>픽셀 색상 수정</td>
</tr>
<tr>
<td><code>open(fname, 'rb')</code></td>
<td>이진 파일 읽기 모드</td>
</tr>
<tr>
<td><code>fp.read(1)</code></td>
<td>1바이트씩 읽기</td>
</tr>
<tr>
<td><code>strip()</code></td>
<td>줄끝 공백/줄바꿈 제거</td>
</tr>
<tr>
<td><code>split(',')</code></td>
<td>쉼표 기준으로 쪼개기 → 리스트 반환</td>
</tr>
<tr>
<td><code>Canvas</code></td>
<td>도형/이미지를 그리는 위젯</td>
</tr>
<tr>
<td><code>paper.put(rgbString)</code></td>
<td>RGB 문자열을 이미지에 한 번에 적용</td>
</tr>
</tbody></table>
<hr />
<blockquote>
<p>위젯 하나 붙이는 것에서 시작해서 픽셀 단위 이미지 처리까지 왔다.
구조 짜는 게 제일 중요하다는 걸 점점 더 느끼고 있다.</p>
</blockquote>