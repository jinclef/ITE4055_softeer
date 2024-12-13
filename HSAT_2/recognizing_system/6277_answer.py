import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
N, K = map(int, input().split())

def newDfs(S, maxX, minX, maxY, minY):
  global minSize
  if S == K+1:
    nowSize = (maxX - minX) * (maxY - minY)
    if nowSize < minSize:
      minSize = nowSize
    return
  for nextX, nextY in stackK[S]:
    newMaxX = max(maxX, nextX)
    newMinX = min(minX, nextX)
    newMaxY = max(maxY, nextY)
    newMinY = min(minY, nextY)
    newSize = (newMaxX - newMinX) * (newMaxY - newMinY)
    if newSize < minSize:
      newDfs(S+1, newMaxX, newMinX, newMaxY, newMinY)
    
minSize = 4000000
stackK = [[] for _ in range(K+1)]
for _ in range(N):
  x, y, color = map(int, input().split())
  stackK[color].append((x, y))
for x, y in stackK[1]:
  newDfs(2, x, x, y, y)
print(minSize)
