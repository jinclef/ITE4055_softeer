### 21년 재직자 대회 본선
#### level 3. 코딩 테스트 세트

우리 사람 하는 대로 하면
O(N*T*2*10^12)
-> 2*10^12 부분을 LogN으로 바꾸자!
-> 전체 0 ~ 2*10^12에서 이분탐색. binary search

* 끌어쓴다는 생각. <br/>
    일단 C에서 다 가져오고, 그래도 모자르면 D에서 가져오고, 그래도 모자르면 false <br/>
    모자르다의 기준? testSets. <br/>
    testSets 값은 어떻게 설정되는가? <br/>

* parametric earch: 이진탐색 함수 하나, 중간값 테스트해서 되는지 여부 확인할때 테스트하는 함수 하나가 필요하다.
<br/>
아직 이해가 잘 안된다.

#### parametric search

"
실제로 파라메트릭 서치를 사용하면 최적화 문제를 결정 문제로 바꾸어 풀 수 있게 되어 문제 접근이 상당히 용이해집니다. 최적화 문제를 결정 문제로 바꾸어 푼다는 말은 주어진 상황에서 최솟값, 최댓값 등의 특정 값을 구하는 문제를 특정 값이 어떠한 조건을 만족하는지만 확인하면 되는 문제로 바뀐다는 의미입니다.
...
위 예시의 핵심은 배부르게 지내기 위해 하루 최소 몇 회의 식사를 먹어야 하는가? 에 대한 최적화 문제가
하루에 식사를 R번 했을 때 배부르게 지낼 수 있는가에 대한 결정 문제로 바뀌었다는 것입니다.
"

#### 다시 돌아오면...
아니 그래도 이해 안되는데. testSets 의 기능이 잘 이해가 안됨.