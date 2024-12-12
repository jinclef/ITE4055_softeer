def findDirection(x,y):
    count = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < H and 0 <= ny < W) and matrix[nx][ny] == '#':
            direction = i
            count +=1
    return direction if count == 1 else -1

def findStart(matrix):
    # 모든 자리에 대해서 자기 옆이 하나여야 함.
    # 자기도 있어야 함.
    for x in range(H):
        for y in range(W):
            if matrix[x][y] == '#':
                direction = findDirection(x,y)
                if direction != -1:
                    return x,y,direction

def navigate(x,y,direction):
    newDir = prevDir = direction
    matrix[x][y] = '.'
    while True:
        while newDir == prevDir:
            print('A', end='')
            # 2칸 직진
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = '.'
            x,y = x+dx[newDir], y+dy[newDir]
            matrix[x][y] = '.'

            prevDir = newDir
            newDir = findDirection(x,y)
        if newDir == -1:
            return
        elif (newDir-prevDir)%4 == 1: # turn L, R
            print('L', end='')
        elif (newDir-prevDir)%4 == 3:
            print('R', end='')
        prevDir = newDir

H, W = map(int, input().split())
matrix = [list(input()) for _ in range(H)]

x,y,dir = findStart(matrix)
directionMark = ['^', '<', 'v', '>']
dx = [-1,0,1,0]
dy = [0,-1,0,1]

print(x+1, y+1)
print(directionMark[dir])
navigate(x,y,dir)