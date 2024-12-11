import sys
sys.setrecursionlimit(10**5)

def color(x,y,c):
    old_color = image[x][y]
    image[x][y] = c
    if image[x-1][y] == old_color:
        color(x-1,y,c)
    if image[x+1][y] == old_color:
        color(x+1,y,c)
    if image[x][y-1] == old_color:
        color(x,y-1,c)
    if image[x][y+1] == old_color:
        color(x,y+1,c)

h, w = map(int, input().split())

image = [[0]*(w+2)] # 0인 row 초기화, 인덱스 원하는거 쓰기. 확장해서, out of range 에러가 없게끔 함.
for i in range(h):
    temp = list(map(int, input().split()))
    image.append([0]+temp)
image.append([0]*(w+2))
# print(image)

q = int(input())
for i in range(q):
    x,y,c = map(int, input().split())
    if image[x][y] != c: # new_color 와 old_color 가 같은 경우를 생각해야 함.
        color(x,y,c)

for i in range(1, h+1):
    for j in range(1, w): # w+1이 아님 주의. 왜냐면 마지막은 end 가 없어서.
        print(image[i][j], end=' ')
    print(image[i][w])