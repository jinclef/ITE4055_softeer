def dfs(now, destIdx):
    global cnt
    if now == dest[destIdx]:
        if destIdx == m-1: # 마지막 지점 도착
            cnt +=1
            return
        else: # 중간 지점 도착
            destIdx += 1
    x, y = now # now = [x,y]
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny]==False and grid[x][y]==0: # 벽이 아닌 경우. grid 가 1이면 벽이어서 못감.
            dfs([nx,ny], destIdx)
    visit[x][y] = False # 해제 해야 모든 경우를 계산할 수 있다!


n,m = map(int, input().split()) # n x n, 방문 지점 수 m

grid = [list(map(int, input().split())) for _ in range(n)]
dest = []

for _ in range(m):
    x, y = map(int, input().split())
    dest.append([x-1,y-1]) # 0,0 부터 볼 수 있도록

visit = [[False for _ in range(n)] for _ in range(n)]
cnt = 0 # DFS 전체 경우의 수
dx = [0,0,1,-1]
dy = [1,-1,0,0]

dfs(dest[0], 1) # dest[1] : 도착지. 인데 인덱스로 관리하는게 더 편해서 인덱스만 넣어준다.
print(cnt)
