---
layout: post
title: "[BikeEyes] pothole mAP 붕괴 원인 추적"
date: 2026-09-14 21:40:35 +0900
categories: [projects]
tags: []
velog_url: https://velog.io/@addung/BikeEyes-pothole-mAP-%EB%B6%95%EA%B4%B4-%EC%9B%90%EC%9D%B8-%EC%B6%94%EC%A0%81
---

<p>crack 데이터를 교체하고 재학습했더니 pothole 성능이 무너졌다. 원인을 찾아 고쳤는데 이번엔 전 클래스가 무너졌다. 두 번의 붕괴를 추적한 기록.</p>
<h2 id="1-기준점--1번째-모델">1. 기준점 — 1번째 모델</h2>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/35a1002b-8afa-43ad-a171-e3aac422f32c/image.png" />1번째 모델 클래스별 성능
<em>yolov8m_5class_epoch150 결과</em></p>
<table>
<thead>
<tr>
<th>클래스</th>
<th>Box(P)</th>
<th>R</th>
<th>mAP50</th>
<th>mAP50-95</th>
</tr>
</thead>
<tbody><tr>
<td>all</td>
<td>0.971</td>
<td>0.956</td>
<td>0.98</td>
<td>0.808</td>
</tr>
<tr>
<td>manhole</td>
<td>0.992</td>
<td>0.995</td>
<td>0.995</td>
<td>0.914</td>
</tr>
<tr>
<td>pothole</td>
<td>0.982</td>
<td>0.967</td>
<td>0.991</td>
<td>0.765</td>
</tr>
<tr>
<td>flood_area</td>
<td>0.977</td>
<td>0.97</td>
<td>0.99</td>
<td>0.836</td>
</tr>
<tr>
<td>bollard</td>
<td>0.97</td>
<td>0.979</td>
<td>0.99</td>
<td>0.819</td>
</tr>
<tr>
<td>crack</td>
<td>0.936</td>
<td>0.87</td>
<td>0.935</td>
<td>0.708</td>
</tr>
</tbody></table>
<p>crack만 상대적으로 낮았다. 그래서 crack 원천 데이터를 품질 좋은 것으로 교체하고 재학습을 돌렸다.</p>
<h2 id="2-1차-붕괴--pothole만-무너짐">2. 1차 붕괴 — pothole만 무너짐</h2>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/ba3f0e06-116a-4330-955d-f5d84ee825b3/image.png" />
2번째 모델 클래스별 성능
<em>train_5class_testbed_yolov8m_640_e150_p30 결과</em></p>
<table>
<thead>
<tr>
<th>클래스</th>
<th>Box(P)</th>
<th>R</th>
<th>mAP50</th>
<th>mAP50-95</th>
</tr>
</thead>
<tbody><tr>
<td>all</td>
<td>0.642</td>
<td>0.861</td>
<td>0.638</td>
<td>0.524</td>
</tr>
<tr>
<td>manhole</td>
<td>0.992</td>
<td>0.993</td>
<td>0.994</td>
<td>0.91</td>
</tr>
<tr>
<td><strong>pothole</strong></td>
<td><strong>0.0219</strong></td>
<td>0.932</td>
<td><strong>0.0236</strong></td>
<td>0.0167</td>
</tr>
<tr>
<td>flood_area</td>
<td>0.965</td>
<td>0.975</td>
<td>0.99</td>
<td>0.824</td>
</tr>
<tr>
<td>bollard</td>
<td>0.933</td>
<td>0.982</td>
<td>0.97</td>
<td>0.793</td>
</tr>
<tr>
<td>crack</td>
<td>0.298</td>
<td>0.425</td>
<td>0.211</td>
<td>0.079</td>
</tr>
</tbody></table>
<p>건드린 건 crack 데이터뿐인데 pothole이 0.991 → 0.0236으로 떨어졌다.</p>
<p>manhole, flood_area, bollard는 그대로였다. 학습 설정 문제였다면 전체가 흔들렸어야 한다. 특정 클래스만 떨어졌으니 데이터 쪽을 봐야 했다.</p>
<p>Precision 0.0219 / Recall 0.932라는 조합도 눈에 띄었다. 재현율은 높은데 정밀도만 바닥이다. 못 찾는 게 아니라 아닌 걸 찍고 있다는 뜻이다. 혼동행렬에서도 background → pothole 오탐이 <strong>188,991건</strong>으로 나왔다.</p>
<h2 id="3-가설--형태가-아니라-질감을-학습">3. 가설 — 형태가 아니라 질감을 학습</h2>
<p>오탐 이미지들의 공통점은 도로 표면의 어두운 무늬였다.</p>
<pre><code>콘크리트 홈 패턴  → pothole
노면 질감 변화    → pothole
크랙성 도로 표면  → pothole</code></pre><p>포트홀의 형태가 아니라 질감을 배운 것으로 보였다. 그리고 이번에 바꾼 게 crack 데이터니까, 의심할 곳은 하나였다.</p>
<h2 id="4-라벨-분포-확인">4. 라벨 분포 확인</h2>
<p>class4_crack_20000_split 안의 class id를 전부 카운트했다.</p>
<blockquote>
<p>crack split과 final 데이터셋의 class id 분포
<img alt="" src="https://velog.velcdn.com/images/addung/post/ba103410-63a3-484f-b979-ad4eca6060b7/image.png" /></p>
</blockquote>
<pre><code>crack_split_train  txt 16709  {0: 122, 1: 1379, 3: 44, 4: 76159}
crack_split_val    txt 2192   {0: 17,  1: 243,  3: 4,  4: 10468}
crack_split_test   txt 1099   {0: 6,   1: 102,  3: 2,  4: 5364}

final_train  {0: 14117, 1: 15375, 2: 13999, 3: 40712, 4: 76470}</code></pre><p>crack 데이터셋인데 manhole(0), pothole(1), bollard(3)가 같이 들어 있었다. pothole은 합계 <strong>1,724개</strong>.</p>
<p>여기서 짚어둘 게 있다. YOLO에서 한 이미지에 여러 클래스가 라벨링되는 건 원칙적으로 오류가 아니다. 사진 한 장에 맨홀과 균열이 같이 있으면 둘 다 라벨링하는 게 맞다. 그래서 이 분포만으로 오류라고 단정할 수는 없었다.</p>
<p>다만 정황은 충분했다. train의 pothole은 클래스당 14,000장 기준으로 설계했는데 final_train은 15,375개. 차이가 crack split에서 딸려온 1,724개와 맞아떨어졌다.</p>
<p>확인할 건 그 1,724개가 실제 포트홀이냐였다.</p>
<h2 id="5-육안-검수">5. 육안 검수</h2>
<p>해당 라벨을 원본 이미지에 박스로 그려서 확인했다. 빨강이 pothole(1), 초록이 crack(4).</p>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/74ed8624-4999-4890-925c-8c3853c23c41/image.png" />
선형 균열이 pothole로 라벨링된 사례
 crack 원본에서 나온 이미지인데 선형 균열 하나가 통째로 pothole로 잡혀 있다.</p>
</blockquote>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/3bd062b4-cc27-49b4-9037-e91ed1032253/image.png" />
자갈 질감을 pothole로 잡은 사례
<em>왼쪽 물 고인 건 진짜 포트홀이 맞다. 문제는 오른쪽 —&gt; 거칠기만 한 자갈 질감 영역에 pothole 박스가 두 개 잡혔다. (파인 곳이 아님)</em></p>
</blockquote>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/fadde6cc-87e1-4375-bced-d72190b16be1/image.png" />
bbox가 도로 대부분을 덮은 사례
pothole 박스 세 개가 겹치면서 도로 대부분을 덮었다. <em>이 정도 크기면 모델이 &quot;도로 배경 전체&quot;를 포트홀 특징으로 배워버리는 사태 발생.</em></p>
</blockquote>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/c584ebb7-8ee5-4d22-a442-0a3fa9679dd8/image.png" />같은 질감인데 클래스가 갈린 사례
<em>거북등 균열 구간에 pothole 박스. 같은 이미지 안에서 비슷한 질감의 다른 영역은 crack으로 잡혀 있다. (기준이 일관되지 않음)</em></p>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/a5f0043d-1701-4d5c-8483-57a9c68329cc/image.png" />
 균열 영역에 pothole 하나가 섞인 사례
<em>상단 균열 영역에 pothole 하나. 나머지는 전부 crack.</em></p>
<p>오라벨이 다수 확인됐다. 특히 균열이 깊어 그늘이 생긴 부분이 포트홀로 들어간 경우가 많았다.</p>
<p>한 가지 인정할 부분은, 사람이 봐도 애매한 경계가 있다는 것이었으며 실제 우리 프로젝트 기준으로 필요한 '이미지의 정확도나 사진의 각도 측면'도 중요하다는 사실을 다시금 인지하게 되었다. 도로 보수 흔적이나 깊은 균열은 판단이 갈린다. 그래도 첫 번째 사진처럼 명백한 선형 균열까지 포트홀로 들어간 건 오라벨로 보는 게 맞다고 판단했다.</p>
<p>오탐 188,991건은 모델이 잘못 배운 게 아니라 가르친 대로 배운 결과였다는 것을 깨닫게 되었다. 데이터가 워낙 많았었고 공공데이터에 공유되었던 원천데이터였음에 이러한 오류를 크게 의심하지 못했던 것 같다.</p>
<h2 id="6-1차-조치--crack-split에서-class-4만-남기기">6. 1차 조치 — crack split에서 class 4만 남기기</h2>
<p>라벨 파일에서 class 0/1/3 줄을 지우고 class 4만 남기는 스크립트를 돌렸다.</p>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/edc61137-d411-4454-8509-128a3983bc2e/image.png" /></p>
</blockquote>
<p> -&gt;make_crack_split_only4.py 실행 결과</p>
<pre><code>[train] 유지 16521 / 제외 188
        원본  {0:122, 1:1379, 3:44, 4:76159}
        only4 {4: 76159}
[val]   유지 2158 / 제외 34
[test]  유지 1080 / 제외 19</code></pre><blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/4d5fb610-c2a7-4a9a-a1b4-a8ba8c224427/image.png" />
only4 + negative 반영 후 최종 데이터셋</p>
</blockquote>
<pre><code>[train] class bbox 분포: {0: 13995, 1: 13996, 2: 13999, 3: 40668, 4: 76470}</code></pre><p>pothole이 15,375 → 13,996으로 돌아왔다. 의도한 14,000장 기준에 맞았다. (여기까지는 계획대로 착수완료)</p>
<h2 id="7-2차-붕괴--이번엔-전부-무너짐">7. 2차 붕괴 — 이번엔 전부 무너짐</h2>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/8c7564e1-4ead-4e63-8637-00efb0d40d86/image.png" />
3번째 모델 클래스별 성능
<em>train_5class_testbed_yolov8m_640_e150_p30_crack_only4_v2 결과</em></p>
</blockquote>
<table>
<thead>
<tr>
<th>클래스</th>
<th>Box(P)</th>
<th>R</th>
<th>mAP50</th>
<th>mAP50-95</th>
</tr>
</thead>
<tbody><tr>
<td>all</td>
<td>0.11</td>
<td>0.574</td>
<td>0.0906</td>
<td>0.077</td>
</tr>
<tr>
<td>manhole</td>
<td>0.325</td>
<td>0.739</td>
<td>0.252</td>
<td>0.227</td>
</tr>
<tr>
<td>pothole</td>
<td>0.00145</td>
<td>0.352</td>
<td>0.000677</td>
<td>0.000469</td>
</tr>
<tr>
<td>flood_area</td>
<td>0.0783</td>
<td>0.862</td>
<td>0.0731</td>
<td>0.0586</td>
</tr>
<tr>
<td>bollard</td>
<td>0.145</td>
<td>0.799</td>
<td>0.124</td>
<td>0.0979</td>
</tr>
<tr>
<td>crack</td>
<td>0.000417</td>
<td>0.117</td>
<td>0.00315</td>
<td>0.001</td>
</tr>
</tbody></table>
<p>멀쩡했던 manhole 0.994 → 0.252, flood_area 0.99 → 0.0731, bollard 0.97 → 0.124.</p>
<p>고치려다 더 망가뜨렸다.</p>
<h2 id="8-2차-붕괴의-원인--라벨만-지우고-이미지는-남겼다">8. 2차 붕괴의 원인 — 라벨만 지우고 이미지는 남겼다</h2>
<p>원인은 only4 처리 방식 자체였다.</p>
<p>class 0/1/3 라벨을 지웠지만 <strong>이미지는 그대로 뒀다.</strong> 그런데 그 이미지 안에는 실제로 맨홀도 있고 볼라드도 있었다. 라벨이 없어진 상태로 학습에 들어가니 모델 입장에서는 이렇게 읽힌다.</p>
<pre><code>이 사진에 맨홀이 찍혀 있는데 라벨이 없다
→ 이 맨홀처럼 생긴 건 background다</code></pre><p>crack 이미지 16,521장에 걸쳐 이런 학습이 일어났다. pothole 오염을 지우려다 manhole·bollard·flood_area까지 &quot;찾으면 안 되는 것&quot;으로 가르친 셈이다.</p>
<p>정리하면 이렇다.</p>
<table>
<thead>
<tr>
<th></th>
<th>무슨 일</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td>문제 A</td>
<td>crack 소스에 오염된 pothole 라벨 1,724개 혼입</td>
<td>pothole 0.991 → 0.0236</td>
</tr>
<tr>
<td>문제 B</td>
<td>only4 처리에서 라벨만 삭제하고 이미지 유지</td>
<td>manhole·flood_area·bollard까지 추가 붕괴</td>
</tr>
</tbody></table>
<p>문제 A만 보고 성급하게 조치한 게 문제 B를 만들었다.</p>
<h2 id="9-올바른-조치-방향">9. 올바른 조치 방향</h2>
<p>라벨만 지우는 방식은 쓰면 안 된다는 게 확실해졌다. 대신 class 0/1/3 bbox가 포함된 이미지를 추출해서 하나씩 판정하기로 했다.</p>
<table>
<thead>
<tr>
<th>판정</th>
<th>처리</th>
</tr>
</thead>
<tbody><tr>
<td>실제 pothole·manhole·bollard가 맞다</td>
<td>라벨 유지</td>
</tr>
<tr>
<td>실제로는 crack·질감·보수 흔적이다</td>
<td><strong>이미지 자체를 제외</strong></td>
</tr>
</tbody></table>
<p>라벨만 지우고 이미지를 남기는 방식은 금지. 이게 문제 B의 원인이었다.</p>
<p>class 1이 bbox 1,724개, 이미지로는 1,000장 내외라 수기 검수가 가능한 규모였다.</p>
<h2 id="10-정리">10. 정리</h2>
<p>이번에 두 번 깨지면서 남은 것.</p>
<p><strong>성능이 떨어졌을 때 모델부터 만지지 않는다.</strong> 
: 전체가 아니라 특정 클래스만 떨어졌다면 원인은 학습 코드 바깥에 있을 가능성이 높다.</p>
<p><strong>mAP 하나만 보지 않는다.</strong> 
: Precision 0.02 / Recall 0.93이라는 조합이 &quot;못 찾는 문제&quot;가 아니라 &quot;아닌 걸 찍는 문제&quot;라는 걸 알려줬다. 혼동행렬의 background 오탐 건수도 같은 이야기를 했다.</p>
<p><strong>수치는 가설까지만 세워준다.</strong> 
: 1,724개라는 숫자는 의심의 근거일 뿐이고, 실제로 오라벨인지는 그려서 봐야 알 수 있었다.</p>
<p><strong>데이터 조치는 학습이 그걸 어떻게 읽을지까지 생각하고 해야 한다.</strong> 
: 이게 제일 크게 남았다. 라벨을 지우는 행위가 &quot;이 클래스를 학습에서 빼기&quot;가 아니라 &quot;이 객체를 background로 가르치기&quot;가 된다는 걸 처음엔 생각하지 못했다. YOLO에서 빈 라벨은 정보 없음이 아니라 negative 신호다.</p>
<p>crack은 이 문제들과 별개로 낮은 성능이 이어졌다. 길고 가늘게 이어지는 균열을 사각형 박스로 감싸는 방식 자체의 한계라고 판단했고, 이와 더불어 단순 1천여장 정도의 분리라고 여겨졌던 원천데이터의 문제또한 꽤나 심각했다.</p>