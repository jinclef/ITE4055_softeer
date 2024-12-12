### 21년 재직자 대회 예선
#### level 3. 로드밸런서 트래픽 예측

- 요청의 개수가 최대 10^18 개라서 직접 다 따라가면 시간초과됨.
- topological sort 를 사용한다.
- indegree 를 노드별로 계산하고, indegree=0인 노드의 dest node 의 indegree -=1 하면, 그 다음 indegree=0 인 노드가 생길 거임. 그럼 이제 걔에 대해서 반복. 모두 0 될때까지.
- 다 돌고 0 찾고, 다 돌고 0 찾고 하면 10^2 만큼 들게 됨 -> 시간 초과. 따라서 그떄그때 처리해준다: stack 활용해서 O(n) 시간 내에 해결하도록 함.
- 

##### Topological Sort
- 간선의 방향은 항상 한방향 (왼쪽 -> 오른쪽) 이어야 한다.
- 사이클이 없어야 한다. (DAG)
- 모든 노드의 indegree (노드로 들어오는 간선의 개수) 를 저장해야 한다 : indegree = 0 인 노드가 가장 왼쪽에 올 수 있다.

###### 예시
| node id   | 1 2 3 4 5 6 7 8 |
| --------- | --------------- |
| indegree  | 0 2 1 1 1 1 1 1 |
