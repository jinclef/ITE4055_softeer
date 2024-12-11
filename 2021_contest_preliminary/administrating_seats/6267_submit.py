N,M,Q = map(int, input().split()) # N행 M열 좌석

## 좌석별로, 앉은 자리와의 거리 최솟값을 담은 배열
seat = [[((N-1)**2 + (M-1)**2)**(1/2) for j in range(M)] for i in range(N)]
# print(seat)

## 사람별 식사 여부 pair <id, status>
YET = 0
ING = 1
LEFT = 2

eaten = {0 : {YET, 0, 0}} # { id : (status, x, y) }

def distance(fromX, fromY, toX, toY):
    return ((toX - fromX)**2 + (toY-fromY)**2) ** (1/2)

def update_minD(i, j):
    for x in range(1, M+1):
        for y in range(1, N+1):
            if (seat[x][y] == 0):
                d = distance(i,j,x,y)
                if (d < seat[i][j]):
                    seat[i][j] = d
                    break

def caculate_minD_per_seat():
    for i in range(M):
        for j in range(N):
            update_minD(i, j)

def find_seat():
    max = 1
    n = N
    m = M
    get = False
    for i in range(M):
        for j in range(N):
            if max < seat[i][j]:
                max = seat[i][j]
                n=i
                m=j
            if max == seat[i][j]:
                if (i<n or (i==n and j<m)): n=i, m=j
    if (max == 1):
        get = False
    else:
        get = True


def treat_in(id):
    if id in eaten.keys() and eaten[id][0] == LEFT:
        print(f"{id} already ate lunch.")
    else:
        get, x, y = find_seat()
        if get == False:
            print("There are no more seats.")
        else: # success
            eaten[id][0] = ING
            print(f"{id} gets the seat({x}, {y}).")

def treat_out(id):
    if id in eaten.keys() and eaten[id][0] == LEFT:
        print(f"{id} already left seat.")
    elif id in eaten.keys() and eaten[id][0] == ING:
        x = eaten[id][1]
        y = eaten[id][2]
        print(f"{id} leaves from the seat ({x}, {y}).")
        eaten[id][0] = LEFT
    else:
        print("Error!")


for q in range(Q):
    inout, id = input().split()
    id = int(id)
    if inout == "In":
        treat_in(id)
    else:
        treat_out(id)
