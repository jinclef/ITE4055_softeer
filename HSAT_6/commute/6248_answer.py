n, m = map(int, input().split()) # 정점, 간선 수

adj = [[] for _ in range(n+1)] # 정점 번호 그대로 쓰기 위함
adjR = [[] for _ in range(n+1)] # reverse
for _ in range(m):
    x,y = map(int, input().split())
    adj[x].append(y)
    adjR[y].append(x)

s,t = map(int, input().split()) # 집, 회사

def dfs(nodeToVisit, adj, visit):
    if visit[nodeToVisit] == 1:
        return
    visit[nodeToVisit] = 1
    for neighbor in adj[nodeToVisit]:
        dfs(neighbor, adj, visit)

    return

# 기본 그래프
fromS_visit = [0] * (n+1)
dfs(s, adj, fromS_visit)
fromT_visit = [0] * (n+1)
dfs(t, adj, fromT_visit)

# 반전된 그래프
toS_visit = [0] * (n+1)
dfs(s, adjR, toS_visit)
toT_visit = [0] * (n+1)
dfs(t, adjR, toT_visit)

count = 0
for i in range(1, n+1):
    if fromS_visit[i] and fromT_visit[i] and toS_visit[i] and toT_visit[i]:
        count +=1
