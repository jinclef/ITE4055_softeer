import sys
sys.setrecursionlimit(10**6)

N = int(input())

def dfs1(current, parent):
    subtreeSize[current] = 1
    for i in range(len(node[current])):
        child = node[current][i][0]
        weight = node[current][i][1]
        if child != parent:
            dfs1(child, current) # bottom-up
            distSum[current] += distSum[child] + subtreeSize[child]*weight # 아직 최상위 노드 말고는 올바르지 않은 값임. 
            subtreeSize[current] += subtreeSize[child]
    return

def dfs2(current, parent):
    for i in range(len(node[current])):
        child = node[current][i][0]
        weight = node[current][i][1]
        if child != parent:
            # distSum[child] = distSum[current] - weight*(subtreeSize[child]) + weight*(N-subtreeSize[child])
            distSum[child] = distSum[current] + weight*(N-2*subtreeSize[child])
            dfs2(child, current) # top-down

node = [[] for _ in range(N+1)] # 3중 노드
subtreeSize = [0]*(N+1)
distSum = [0]*(N+1)

for i in range(N-1):
    x,y,t = map(int, input().split())
    # 양방향으로 노드 간선 저장
    node[x].append([y,t])
    node[y].append([x,t])

# print(node)
dfs1(1,1)

print(distSum)
dfs2(1,1)

# for i in range(1, N+1):
#     print(distSum[i])