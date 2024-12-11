import sys
# sys.setrecursionlimit(30000)

H, W = map(int, input().split())

color_grid = []
for h in range(H):
    color = list(map(int, input().split()))
    color_grid.append(color)

# print(color_grid)

def change_color(i,j,c):
    # cf. color_grid[0] 은 첫번째 열을 가리킴. [세로][가로]

    my_color = color_grid[i][j]
    color_grid[i][j] = c
    # 좌
    if j-1>=0 and color_grid[i][j-1] == my_color:
        change_color(i, j-1, c)
    # 우
    if j+1<len(color_grid[i]) and color_grid[i][j+1] == my_color:
        change_color(i, j+1, c)
    # 상
    if i-1>=0 and color_grid[i-1][j] == my_color:
        change_color(i-1, j, c)
    # 하
    if i+1<len(color_grid) and color_grid[i+1][j] == my_color:
        change_color(i+1, j, c)

Q = int(input())

for q in range(Q):
    i, j, c = map(int, input().split())
    if color_grid[i-1][j-1] != c:
        change_color(i-1,j-1,c)


for h in range(H):
    for w in range(W):
        if w == W-1:
            print(color_grid[h][w])
        else:
            print(color_grid[h][w], end=' ')