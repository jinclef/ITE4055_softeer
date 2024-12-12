def dfs(rnd, count, x, y, visit, left, right, bottom, top, neighbor):
    count +=1
    color = garage[rnd][x][y]
    neighbor.append([x,y])
    visit[x][y] = True
    left, right = min(left,x), max(right, x)
    bottom, top = min(bottom,y), max(top, y)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <=nx<n and 0<=ny<n and garage[rnd][nx][ny] == color and visit[nx][ny] == False:
            count,left,right,bottom,top, neighbor = dfs(rnd, count, nx, ny, visit, left, right, bottom, top, neighbor)
    
    return count, left, right, bottom, top, neighbor

def remove(rnd, neighbor):
    garage[rnd+1] = [item[:] for item in garage[rnd]] # rnd 1의 것을 복사
    for cell in neighbor:
        x,y = cell[0], cell[1]
        garage[rnd+1][x][y] = 0

def calculateNeighbor(rnd): # neighbor 가 없으면 dfs 돌 필요 없으니까.
    hasNeighbor = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x<n-1 and garage[rnd][x][y] == garage[rnd][x+1][y]:
                hasNeighbor[x][y] = hasNeighbor[x+1][y] = 1
            if y<n-1 and garage[rnd][x][y] == garage[rnd][x][y+1]:
                hasNeighbor[x][y] = hasNeighbor[x][y+1] = 1
    return hasNeighbor

def refill(rnd):
    for x in range(n):
        temp = []
        for y in range(len(garage[rnd+1][x])):
            value = garage[rnd+1][x][y]
            if value != 0:
                temp.append(value)
            # else: pass
        garage[rnd+1][x] = temp

def simulate(rnd, total):
    global largest
    visit =[[False for _ in range(n)] for _ in range(n)]
    hasNeighbor = calculateNeighbor(rnd)

    for x in range(n):
        for y in range(n):
            if visit[x][y] == True:
                continue
            left = right = x
            bottom = top = y
            count = 0 # 같은 인접한 값

            if rnd == 2 and hasNeighbor[x][y] == 0:
                count, area = 1,1
                visit[x][y] = True
            else:
                neighbor = []
                count,left,right,bottom,top, neighbor = dfs(rnd, count, x, y, visit, left, right, bottom, top, neighbor)
                area = (right-left+1)*(top-bottom+1)
            
            newTotal = total + area + count

            if (rnd == 2):
                if largest < newTotal:
                    largest = newTotal
            else:
                remove(rnd, neighbor)
                refill(rnd)
                simulate(rnd+1, newTotal)
n = int(input())

garage =[[[] for _ in range(n)] for _ in range(3)] # garage[0] = 1회차 [1] 2회차 [2] 3회차 게임
for _ in range(3*n):
    temp = list(map(int, input().split()))
    for i in range(n):
        garage[0][i].append(temp[i])

for i in range(n): # 0 이 밑인게 나아서..
    garage[0][i].reverse()

dx = [0,1,0,-1]
dy = [1,0,-1,0]
largest = 0 # 3번 했을 때 얻을 수 있는 가장 큰 점수
simulate(0,0)
print(largest)