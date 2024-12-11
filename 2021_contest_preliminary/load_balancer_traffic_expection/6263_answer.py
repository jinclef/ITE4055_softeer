def calIndegree(dag): # indegree 계산 함수
    indegree = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(1, dag[i][0]+1): # dag[i][0] : 뻗어나가는 간선의 개수
            indegree[dag[i][j]]+=1 # dag[i][j] : dest node 의 idx
    
    return indegree

def tsort(dag): # topological sort
    indegree = calIndegree(dag)
    # print(indegree)
    stack = []
    for nodeId in range(1, n+1):
        if indegree[nodeId] == 0:
            stack.append(nodeId)
    
    ordering = [] # topological sort 결과가 될 list
    while stack: # while stack is not empty
        node = stack.pop() # indegree = 0 인 노드
        ordering.append(node)
        for i in range(1, dag[node][0]+1): # node 에서 나가는 간선
            child = dag[node][i]
            indegree[child] -=1
            if indegree[child] == 0:
                stack.append(child)

    return ordering

n, k = map(int, input().split()) # n: node 수, k: traffic 수

dag = [[0]] # 노드 간선 정보 넣기 list of list. 노드 번호가 1번부터라서 초기화 넣어줌.

for i in range(n):
    temp = list(map(int, input().split()))
    dag.append(temp)

ordering = tsort(dag)
# print(ordering) # [1,8,7,6,5,3,4,2]

traffic = [0]*(n+1) # node 마다 트래픽 수
traffic[1] = k # 초기화. 0 은 place holder 니까 넘어간다.
for nodeId in range(n): # n == len(ordering)
    node = ordering[nodeId]
    # 이미 그 노드에 트래픽이 분배되었다고 가정하고 자식에게 나눠준다.
    request = traffic[node]
    if dag[node][0] == 0:
        continue # 노드에서 나가는 간선의 수가 없는 경우 무시
    q = request // dag[node][0]
    r = request % dag[node][0]
    for j in range(1, dag[node][0]+1):
        child = dag[node][j]
        traffic[child] += q
    for j in range(1, r+1):
        child = dag[node][j]
        traffic[child] +=1

for i in range(1, n):
    print(traffic[i], end=' ')
print(traffic[n])
