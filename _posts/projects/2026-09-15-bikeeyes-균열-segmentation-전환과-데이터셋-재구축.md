---
layout: post
title: "[BikeEyes] 균열 Segmentation 전환과 데이터셋 재구축"
date: 2026-09-15 14:59:44 +0900
categories: [projects]
tags: []
velog_url: https://velog.io/@addung/BikeEyes-%EA%B7%A0%EC%97%B4-Segmentation-%EC%A0%84%ED%99%98%EA%B3%BC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B-%EC%9E%AC%EA%B5%AC%EC%B6%95
---

<p>이전까지의 기록에서는 pothole 라벨 오염을 잡았다. 그런데 crack은 라벨을 정리한 뒤에도 성능이 올라오지 않았다. 모델을 바꾸는 대신 문제 정의부터 다시 했고, 결국 Detection에서 Segmentation으로 분리했다. 그 판단과 데이터 재구축 과정을 정리해보려고 한다.</p>
<h2 id="1-crack만-계속-낮았던-상황">1. crack만 계속 낮았던 상황</h2>
<p>5클래스 detection 모델에서 crack은 처음부터 다른 클래스보다 낮았다.</p>
<table>
<thead>
<tr>
<th>모델</th>
<th>crack mAP50</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td>1번째</td>
<td>0.935</td>
<td>다른 클래스는 0.99대</td>
</tr>
<tr>
<td>2번째</td>
<td>0.211</td>
<td>pothole 라벨 오염</td>
</tr>
<tr>
<td>3번째</td>
<td>0.00315</td>
<td>only4 처리로 전 클래스 붕괴</td>
</tr>
</tbody></table>
<p>2·3번째의 원인은 앞 글에서 정리한 라벨 문제였다. 문제는 그걸 다 고쳐도 crack만 유독 안 오른다는 점이었다.</p>
<p>라벨을 더 고칠 게 아니라, <strong>crack이라는 대상 자체가 사각형 박스와 안 맞는 것 아닌가</strong>를 의심하기 시작했다.</p>
<h2 id="2-bbox의-구조적-한계">2. BBOX의 구조적 한계</h2>
<p>균열은 가늘고 길게, 대각선으로 불규칙하게 이어진다. 이걸 사각형으로 감싸면 박스 안 대부분이 정상 도로가 된다.</p>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/4e216a45-5622-4a32-9b84-2b36ef9d5ff5/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/8f5c8ff3-c1e2-4f1a-9b7c-c1985d8c91a7/image.png" /></p>
<p>: 대각선으로 뻗은 균열 하나를 감싸면, 박스 안에서 실제 균열이 차지하는 픽셀은 일부에 불과하다.</p>
<p>여기서 이전 기록에서와 같이 동일하게, pothole이 무너졌던 이유가 &quot;형태가 아니라 도로 질감을 배워서&quot;였다. crack도 같은 구조였다. 박스 안 대부분이 정상 도로면, 모델은 &quot;이 도로 표면 = crack&quot;을 배우게 된다. 라벨이 정확해도 박스 방식 자체가 그 학습을 유도하고 있다는 사실을 깨닫게 되었다.</p>
<h2 id="3-회전-증강을-뺀-이유">3. 회전 증강을 뺀 이유</h2>
<p>증강 조건을 정할 때 회전을 제외했었다. </p>
<pre><code>대각선 균열에 회전을 적용
→ bbox는 축에 정렬된 사각형이라 다시 커짐
→ 박스와 실제 균열 사이 빈 배경이 더 늘어남
→ 라벨 품질이 오히려 나빠짐</code></pre><p>그래서 증강은 좌우반전, 밝기·색상 변화, 약간의 스케일 조정까지만 허용했다.</p>
<p>당시엔 라벨 품질을 지키려는 선택이라고만 봤다. 돌아보면 증강을 제한한 이유가 곧 박스 방식의 한계였다. 이런 제약이 하나씩 쌓이면서 crack을 사각형으로 다루는 게 맞는지 다시 생각하게 되었다.</p>
<h2 id="4-데이터-누수를-만들-뻔한-순서오류">4. 데이터 누수를 만들 뻔한 순서오류</h2>
<p>crack 데이터를 새로 만들면서 처음 세운 계획은 이랬다.</p>
<pre><code>원본 1,200장 + 필터링분 모으기
→ 증강해서 2만 장 만들기
→ 7:2:1로 분할</code></pre><p>이 순서가 잘못됐다는 걸 뒤늦게 알았다.</p>
<p>원본 1장을 증강하면 좌우반전·밝기 변화된 &quot;형제 이미지&quot;가 여러 장 생긴다. 내용은 거의 같고 파일명만 다르다. 이걸 전부 섞은 다음 무작위로 나누면 같은 원본에서 나온 형제가 train·val·test에 제각각 흩어진다.</p>
<p>그러면 val/test는 마치, 처음 보는 데이터가 아니라 train에서 본 사진의 쌍둥이가 된다. 점수가 실제보다 높게 나온다는 것도 다시금 데이터를 분류하는 과정에서 깨닫게 되었다.</p>
<p>이러한 문제를 자각하고, 이후부터는 순서를 바꿨다.</p>
<table>
<thead>
<tr>
<th>단계</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>원본 중복 제거</td>
</tr>
<tr>
<td>2</td>
<td>파일명과 이미지 유사도로, 같은 원본에서 나온 사진끼리 한 묶음으로 만들기</td>
</tr>
<tr>
<td>3</td>
<td>그룹째로 train/val/test 배정 (형제가 갈라지지 않게)</td>
</tr>
<tr>
<td>4</td>
<td>train에만 증강 적용</td>
</tr>
<tr>
<td>5</td>
<td>val/test는 원본 그대로</td>
</tr>
</tbody></table>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/93f3ffd4-8ffe-473a-9bc3-cfffa140be66/image.png" />: &quot;2만 장을 채우자&quot;는 목표 자체도 재검토했다. Ultralytics 학습기는 매 epoch마다 mosaic·hsv·flip을 실시간으로 적용하기 때문에, 미리 정적인 2만 장을 만들어두는 것보다 정제된 원본을 그대로 넘기는 쪽이 낫다는 결론이었다. 숫자를 맞추려고 증강을 늘리는 사고방식이 애초에 crack이 오염됐던 원인과 같았다.</p>
</blockquote>
<h2 id="5-segmentation-전환과-클래스-재정의">5. Segmentation 전환과 클래스 재정의</h2>
<p>이따금 멘토님께 피드백을 받았다. 모델 분리 자체는 타당하지만 원천데이터의 점검을 다시금 제대로 해보라는 피드백을 주셨었다. 라벨 오류와 미라벨 데이터를 먼저 점검해야 하고, SAM 자동 변환 결과를 통해서 다시한번 확인을 거치게 되었다.</p>
<blockquote>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/53b11dbd-9795-47e8-be10-c4c3d26671b0/image.png" /></p>
<ul>
<li>BBOX 라벨링된 사진의 데이터를 SAM 기반으로 확인해본 사진들</li>
</ul>
<p>최종 결정은 두 가지였다.</p>
<p><strong>하나, crack을 별도 segmentation 모델로 분리.</strong></p>
<p><strong>둘, 클래스를 &quot;crack&quot; 단일이 아니라 노면파손 2클래스로 확장.</strong></p>
<pre><code>class 0: linear      (선형 균열)
class 1: alligator   (거북등 균열)</code></pre><p>선형과 거북등은 형태도 원인도 다르다. 두 클래스의 특징이 극명하게 다름에, 하나로 묶어두면 모델이 서로 다른 두 패턴을 같은 클래스로 배우게 된다고 판단했다. 때문에 과감하게 분리하여 운영하기로 결정!</p>
<h2 id="6-구조-결정">6. 구조 결정</h2>
<p>BikeEyes는 AI 추론을 스마트폰이 아니라 서버에서 판단한다. 앱은 수집과 전송을 담당하게 된다.</p>
<pre><code>Android 앱  →  이미지 수집·전송
서버        →  BBOX 모델(1차)  →  Segmentation 모델(2차)</code></pre><p>온디바이스였다면 모델 두 개를 돌리는 부담 때문에 시도가 어려울 수도 있었을 구조였지만, 서버 기반이라 여유가 있다고 판단하여 분리 운영을 선택하게 되었다.</p>
<table>
<thead>
<tr>
<th>모델</th>
<th>담당 클래스</th>
</tr>
</thead>
<tbody><tr>
<td>YOLOv8m Detection</td>
<td>manhole, pothole, flood_area, bollard</td>
</tr>
<tr>
<td>YOLOv8m-seg</td>
<td>linear, alligator</td>
</tr>
</tbody></table>
<p>두 모델 모두 크롭이나 가공 없이 <strong>동일한 원본 파일</strong>을 기준으로 순차 실행한다.</p>
<h2 id="7--기준선-확보와-모델-선택">7.  기준선 확보와 모델 선택</h2>
<p>본 모델을 학습하기 전에 segmentation이 실제로 이 데이터에서 통하는지부터 확인했다.</p>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/68c3b2a0-7c51-4b53-8b2c-c3e48695dd6b/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/fe4c0519-0bd6-4117-afbf-51200d33e240/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/645623b4-938d-4be0-a78d-d7872161d809/image.png" /></p>
</blockquote>
<pre><code>DeepLabv3+ / 50 epoch
Train Loss  0.1042
Val Loss    0.1178
Val IoU     epoch 48  0.6382
            epoch 49  0.6388
            epoch 50  0.6394</code></pre><p>Val IoU가 마지막 3에폭에서 계속 오르고 있었다. 한 epoch당 +0.0006 정도씩이지만 아직 수렴 전이라는 뜻이고, 이 데이터에 학습할 신호가 남아 있다는 확인이었다. 선형 객체 인식에 강한 알고리즘으로 검증한 결과이니, 균열을 픽셀 단위로 다루는 접근 자체는 성립한다고 봤다.</p>
<p>다만 본 모델은 DeepLabv3+가 아니라 YOLOv8m-seg로 갔다. 이유는 세 가지였다.</p>
<blockquote>
</blockquote>
<ol>
<li>인스턴스 단위 결과가 필요했다. DeepLabv3+는 semantic segmentation이라 &quot;이 픽셀이 균열이다&quot;까지만 알려준다. 균열 하나하나를 구분하지 않고, 객체별 confidence도 나오지 않는다. BikeEyes는 탐지 결과마다 confidence를 받아서 클래스별 임계값을 적용하고, 그 값으로 위험구간 확정 여부를 판단한다. 픽셀 맵만으로는 이 흐름에 넣을 수가 없었다.</li>
<li>Detection 모델과 같은 계열이어야 했다. 서버는 동일한 원본 이미지를 BBOX 모델(1차) → Segmentation 모델(2차) 순으로 통과시킨다. 이미 4클래스 detection이 YOLOv8m이었으니 seg도 Ultralytics 계열로 맞추면 전처리, 추론 코드, 결과 포맷을 하나로 관리할 수 있었다. 프레임워크가 둘로 갈리면 그만큼 서버에서 유지해야 할 코드가 늘어난다.</li>
<li>비교 실험의 결론이 그랬다. 5개 객체검출 모델을 비교했을 때 YOLOv8m이 정확도와 속도 모두에서 가장 균형 잡힌 결과였다(<a href="mailto:mAP@0.50">mAP@0.50</a> 0.963, 83.30 FPS). 교수님 피드백도 값이 제일 좋은 하나를 골라 충분히 학습시키고 과적합이 보이면 중단하라는 쪽이었다.</li>
</ol>
<p>DeepLabv3+의 0.6394는 그래서 본 모델이 아니라 기준선으로 남겼다. YOLOv8m-seg가 이보다 못 나오면 접근이 아니라 모델 선택을 다시 봐야 한다는 판단 근거였다.</p>
<h2 id="8-ab-데이터-분리">8. A/B 데이터 분리</h2>
<p>원본은 두 갈래였다. 파일명 규칙으로 구분했다.</p>
<pre><code>new_crack{N}.jpg   →  테스트베드 직접 촬영
raw_crack{N}.jpg   →  공공데이터
aug_crack4_{번호}_from_{원본명}.jpg  →  증강본</code></pre><p><img alt="" src="https://velog.velcdn.com/images/addung/post/f6d41f11-fe56-4c2c-bc91-ed1ea02c5f28/image.png" /></p>
<table>
<thead>
<tr>
<th>구분</th>
<th>내용</th>
<th>규모</th>
</tr>
</thead>
<tbody><tr>
<td>source_B</td>
<td>테스트베드 직접 촬영</td>
<td>3,786장 (원본 그룹 1,248개)</td>
</tr>
<tr>
<td>source_A</td>
<td>공공데이터</td>
<td>15,973장 (원본 그룹 9,556개)</td>
</tr>
</tbody></table>
<p>B는 원본 그룹 단위로 train 832그룹(2,507장) / val 208그룹(671장) / test_holdout 208그룹(608장)으로 나눴다. 4번에서 정한 원칙대로 <strong>그룹째 배정</strong>해서 증강 형제가 split을 넘나들지 않게 했다.</p>
<h2 id="9-촬영-관점-필터링">9. 촬영 관점 필터링</h2>
<p>공공데이터를 그대로 쓰면 안 된다고 판단했다. raw_crack 번호 구간별로 촬영 출처를 확인했다.</p>
<table>
<thead>
<tr>
<th>번호 구간</th>
<th>출처</th>
<th>개수</th>
<th>결정</th>
</tr>
</thead>
<tbody><tr>
<td>1~1171</td>
<td>노르웨이 자동차 블랙박스</td>
<td>1,953</td>
<td>제외</td>
</tr>
<tr>
<td>1172~1986</td>
<td>중국 오토바이</td>
<td>1,285</td>
<td><strong>유지</strong></td>
</tr>
<tr>
<td>1987~2769</td>
<td>중국 드론</td>
<td>1,290</td>
<td>제외</td>
</tr>
<tr>
<td>2770~4124</td>
<td>자동차 블랙박스</td>
<td>2,138</td>
<td>제외</td>
</tr>
<tr>
<td>4125~6460</td>
<td>도보 근접 촬영</td>
<td>3,838</td>
<td><strong>유지</strong></td>
</tr>
<tr>
<td>6461~9714</td>
<td>드론</td>
<td>5,469</td>
<td>제외</td>
</tr>
</tbody></table>
<p>결과: <strong>15,973장 → 5,123장 (32% 유지, 68% 제외)</strong></p>
<p>드론은 위에서 내려다보고, 자동차 블랙박스는 자전거보다 높고 빠르다. BikeEyes는 자전거에 거치된 스마트폰으로 찍는다. 같은 균열이라도 관점이 다르면 모델이 보는 형태가 달라진다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/79ddfd28-2274-4f38-99b9-3043d08cf722/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/3a16657a-a702-4acc-ba3b-8c1e0e8a2a47/image.png" /></p>
<p>데이터 1만 장을 버리는 결정이었다. 수량보다 실제 사용 환경과의 일치가 중요하다고 판단했다.</p>
<h2 id="10-sam으로-bbox-→-polygon-변환">10. SAM으로 bbox → polygon 변환</h2>
<p>기존 crack bbox 라벨을 폴리곤으로 바꿔 재사용하기로 했다. 처음부터 다시 라벨링하면 2만 장을 손으로 따야 했다.</p>
<p>Roboflow 웹 UI로 먼저 시도했는데 대량 일괄 변환 기능이 없었다. 로컬 Ultralytics SAM(<code>sam2_b.pt</code>)으로 전환해서 해결했다.</p>
<pre><code>대상: source_A 전체 15,973 + source_B 전체 3,786
결과: 각 split 폴더에 labels_polygon 하위 폴더 생성
      원본 labels(bbox)는 그대로 보존
class id: 5클래스 체계의 4(crack) → 단일 클래스 체계의 0으로 일괄 변환</code></pre><p>원본 bbox를 지우지 않고 남겨둔 건 의도적이었다. 변환 결과가 이상할 때 원본과 대조해야 했다.</p>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/4a46e445-71ed-452f-b161-7841f07d90dc/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/c8767c2f-a2df-41f6-ae70-999dc29aad8a/image.png" /><em>이미지에 표시된 파란색 bbox는 균열 주변을 포함하거나, 구불구불한 형태의 크랙의 형태를 전부다 담기에는 한계가 있을음 비교할 수 있다</em></p>
</blockquote>
<h2 id="11-변환-결과-검증">11. 변환 결과 검증</h2>
<p>SAM 변환 결과 일부가 &quot;뭉텅 채워진 영역&quot;으로 나왔다. 균열이 아니라 넓은 구역 전체를 감싼 것이다. 확인해보니 원본 bbox 자체가 구역 단위로 크게 그려진 경우가 많았다.</p>
<p>문제는 2만 장을 전부 눈으로 볼 수는 없다는 점이었다. 의심 후보를 자동으로 걸러낼 지표가 필요했다.</p>
<table>
<thead>
<tr>
<th>시도</th>
<th>방법</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td>1차</td>
<td>폴리곤 자기 자신의 bounding box 대비 채움 비율</td>
<td>방향에 따라 오탐 다수 — <strong>실패</strong></td>
</tr>
<tr>
<td>2차</td>
<td>회전 최소 바운딩박스(minAreaRect) 기준</td>
<td>여전히 오탐 다수 — <strong>실패</strong></td>
</tr>
<tr>
<td>3차</td>
<td><strong>원본 bbox 면적 대비</strong> 폴리곤 채움 비율</td>
<td><strong>확정</strong></td>
</tr>
</tbody></table>
<p>1차가 실패한 이유는 폴리곤 자신의 bbox를 기준으로 삼으면 대각선 균열과 수평 균열의 값이 전혀 다르게 나오기 때문이었다. 비교 기준이 대상에 따라 흔들리면 지표가 될 수 없다.</p>
<p>3차로 확정한 뒤 자동 분류 로직을 만들었다.</p>
<pre><code>blob_suspect      뭉툭한 bbox인데 많이 채워짐   → 의심
order_mismatch    ratio &gt; 1.05, 매칭 의심       → 의심
elongated_normal  원래 가는 bbox라 정상 추정    → 정상 추정</code></pre><blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/3f3d58f2-b585-461f-af53-92082badc1bd/image.png" /></p>
</blockquote>
<h2 id="12-검수-기준이-뒤집힌-지점">12. 검수 기준이 뒤집힌 지점</h2>
<p>여기서 판단이 한 번 뒤집혔다.</p>
<p>클래스를 &quot;노면파손(선형 + 거북등)&quot;으로 넓히면서 <strong>&quot;넓게 채워진 것 = 오류&quot;라는 전제 자체가 무효가 됐다.</strong> 거북등 균열은 원래 넓은 영역 형태가 정상이다. 채움 비율이 높다는 게 문제가 아니게 된 것이다.</p>
<p>검수 기준을 바꿨다.</p>
<pre><code>(변경 전) 이 폴리곤이 얼마나 채워졌나
(변경 후) 이 영역이 실제 노면손상인가 아닌가</code></pre><p>클래스 정의가 바뀌면 검수 기준도 같이 바뀌어야 한다는 걸 이때 알았다. 자동 지표를 세 번 고쳐 만들어놓고, 정작 그 지표가 의미를 갖는 전제가 사라진 상황이었다.</p>
<h2 id="13-검수-도구-직접-제작">13. 검수 도구 직접 제작</h2>
<p>수기 검수용 GUI를 Python tkinter와 Pillow로 만들었다.</p>
<pre><code>review_gui.py
- 8열 × 4행 = 32장 격자 표시
- 클릭으로 다중 선택 후 [선형] / [거북등] / [제외] 일괄 태그
- 진행 상황 CSV 실시간 저장 (중단해도 이어서 가능)</code></pre><blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/0080a563-d7ff-4e4c-8e06-46bedc6d3432/image.png" /></p>
</blockquote>
<p>3,123개를 한 장씩 열어보는 방식으로는 끝낼 수 없어서 만든 도구였다.</p>
<h2 id="14-검수-결과">14. 검수 결과</h2>
<table>
<thead>
<tr>
<th>대상</th>
<th>규모</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td>blob_suspect + order_mismatch</td>
<td>3,123개</td>
<td>345개 직접 분류, 나머지 2,778개 <strong>전부 제외</strong></td>
</tr>
<tr>
<td>elongated_normal (spot-check)</td>
<td>1,147개</td>
<td>71개 직접 분류(그중 36개 제외), 1,076개 기존 라벨 유지</td>
</tr>
</tbody></table>
<p>최종 제외: 2,126장 + 36장 = <strong>2,156장</strong></p>
<p>2,778개를 전부 제외한 건 의도적인 선택이었다. 애매하거나 라벨링 오차가 있어 보이는 건 남기지 않았다.</p>
<p>앞 글에서 오염된 라벨 1,724개 때문에 모델이 통째로 무너지는 걸 겪었다. 확신 없는 라벨을 데이터셋에 남기는 비용이 데이터를 버리는 비용보다 크다는 게 그때 얻은 기준이었다.</p>
<p>elongated_normal 쪽은 반대로 처리했다. 원래 정상 추정이던 항목이라 전수 검수 대신 71개만 표본으로 봤고, 그중 36개만 제외했다. 의심 구간은 보수적으로, 정상 구간은 표본으로 — 검수 비용을 어디에 쓸지 나눈 것이다.</p>
<h2 id="15-최종-데이터셋">15. 최종 데이터셋</h2>
<p>두 제외 목록을 반영해 clean 폴더를 만들었다.</p>
<pre><code>source_A_only4_base_viewpoint_filtered_clean/
├── train/  images, labels(=폴리곤), labels_bbox_backup(원본 bbox)   2,914장
├── val/    405장
└── test/   225장</code></pre><p>15,973장에서 시작해 최종 3,544장이 됐다. 관점 필터링에서 68%, 검수에서 추가로 걸러낸 결과다.</p>
<h2 id="16-학습-전략--base-→-fine-tuning-→-holdout">16. 학습 전략 — base → fine-tuning → holdout</h2>
<pre><code>1단계  source_A(공공데이터 clean)로 base 학습
2단계  source_B(테스트베드 실주행)로 fine-tuning
3단계  test_holdout의 raw only 183장으로 최종 평가</code></pre><blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/614a1cd9-fd50-4b87-9c08-e9de7a2af60c/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/e913d68e-fe56-415d-969a-7d1a3211b30a/image.png" /></p>
</blockquote>
<ul>
<li>최종 YOLOv8m-Seg 모델의 성능을 평가한 결과, 전체 클래스 기준 F1-score는 confidence 0.283에서 최대 0.60을 기록하였다. 클래스별 F1-confidence curve에서는 linear 클래스가 약 0.63, alligator 클래스가 약 0.59 수준의 최대 F1-score를 나타냈으며, 두 클래스 모두 약 0.3 부근의 confidence에서 가장 높은 성능을 보였다.</li>
<li>정규화 Confusion Matrix를 분석한 결과, 실제 linear 중 69%가 linear로 정상 예측되었으며, 약 30%는 background로 미탐되었다. 실제 alligator의 경우 45%가 정상 예측되었고, 24%가 linear로 오분류, 31%가 background로 미탐되었다. 따라서 linear에 비해 alligator 클래스의 분류 난도가 상대적으로 높은 것으로 나타났다.</li>
<li>또한 실제 background 영역이 linear로 예측된 비율이 0.93, alligator로 예측된 비율이 0.07로 나타나, 균열이 존재하지 않는 영역에 대한 False Positive 억제가 주요 개선 과제임을 확인하였다. 이를 통해 학습 데이터에서의 정량 성능뿐 아니라 실제 환경에서는 배경의 노면 패턴, 이음선 및 균열과 유사한 질감에 대한 추가적인 검증과 데이터 보강이 필요함을 확인하였다.<h2 id="17-실제-주행-환경-추론-결과">17. 실제 주행 환경 추론 결과</h2>
</li>
</ul>
<blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/addung/post/ab8618b7-e6bf-4c31-a51b-4a88b0d38362/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/2f88fee6-92eb-468d-9aaf-c2772d3d06eb/image.png" />
<img alt="" src="https://velog.velcdn.com/images/addung/post/f6407823-aa76-4e98-ad58-78bf4c38b448/image.png" /></p>
</blockquote>
<ul>
<li><p>BBOX였다면 이 균열을 감싸는 사각형이 도로 폭 상당 부분을 차지했을 것이다.</p>
</li>
<li><p>서비스에 적용된 최종 구조는 다음과 같다.</p>
</li>
</ul>
<pre><code>BBOX 모델      pothole 0.50 / manhole 0.55 / flood_area 0.50 / bollard 0.55
Segmentation   linear 0.40 / alligator 0.40</code></pre><p><img alt="" src="https://velog.velcdn.com/images/addung/post/361ceba1-7fb2-4e03-91f1-38a196573932/image.png" /></p>
<p>클래스별로 confidence 임계값을 다르게 뒀다. 균열 계열을 0.40으로 낮춘 건 형태가 불규칙해서 확신도가 구조적으로 낮게 나오기 때문이다. 같은 기준을 일괄 적용하면 균열만 계속 미탐된다.</p>
<h2 id="18-마무리">18. 마무리</h2>
<p><strong>모델을 바꾼 게 아니라 문제를 다시 정의했다.</strong> crack의 성능이 안 나올 때 백본을 바꾸거나 에폭을 늘리는 선택지도 있었다. 그런데 원인은 &quot;이 대상을 사각형으로 표현하는 게 맞는가&quot;에 있었다. 알고리즘 선택보다 문제를 어떤 형태로 놓느냐가 먼저였다.</p>
<p><strong>데이터를 버리는 판단도 설계다.</strong> 공공데이터 68%를 관점 불일치로 제외했고, 검수에서 애매한 2,778개를 추가로 뺐다. 15,973장이 3,544장이 됐다. 수량이 성능을 만드는 게 아니라는 걸 앞 글에서 한 번 크게 겪은 뒤의 판단이었다.</p>
<p><strong>기준은 클래스 정의가 바뀌면 같이 바뀐다.</strong> 채움 비율 지표를 세 번 고쳐 만들었는데, 클래스를 거북등까지 넓히는 순간 그 지표의 전제가 사라졌다. 도구를 만들기 전에 무엇을 판정하려는지부터 고정돼 있어야 했다.</p>
<p><strong>평가 데이터는 실제 환경과 같아야 한다.</strong> 증강 후 분할은 형제 이미지를 흩어 놓아 점수를 부풀린다. 최종 평가는 증강 없는 실촬영 holdout으로만 했다.</p>