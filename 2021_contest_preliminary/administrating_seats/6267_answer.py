import sys

n,m,q = map(int, input().split())
ID = [0] * (10**4+1) # 0: notIn, 1: Out, [x,y]
table = [[0]*(m+2) for _ in range(n+2)] # 0: out, 1: in # out of range 유의하기 위해 m+1 대신 m+2
# print(table)

def nearest(x,y):
    # 1 <= N,M <= 20
    minD = 1000
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (table[i][j] == 1):
                d = ((x-i)**2 + (y-j)**2) # 비교용이니까 굳이 루트 안해줘도 됨
                if d< minD:
                    minD = d
    return minD

def assign(pid):
    maxD = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (table[i][j] == 0) and \
                table[i-1][j] == 0 and table[i+1][j] == 0 \
                and table[i][j-1]==0 and table[i][j+1]==0 : # 1이면 이미 배정 끝난거임 + 상하좌우에 사람이 없어야 함
                d = nearest(i,j) # 가장 가까운 사람과의 거리가 가장 먼 것
                if d > maxD:
                    maxD = d
                    ID[pid] = [i,j]
    
    if maxD == 0:
        return False
    else:
        table[ID[pid][0]][ID[pid][1]] = 1
        return True, [i,j]

for i in range(q):
    inOut, pid = input().split()
    pid = int(pid)
    if (inOut == "In"):
        if ID[pid] == 0:
            res = assign(pid)
            if res:
                print(f"{pid} gets the seat ({ID[pid][0]}, {ID[pid][1]}).")
            else:
                print("There are no more seats.")
        elif ID[pid] == 1:
            print(f"{pid} already ate lunch.")
        else: # if 문으로 작성하기 어렵기 때문에 이걸 else 에 쓴다.
            print(f"{pid} already seated.")
    else: # out
        if ID[pid] == 0: # 아직 못먹음
            print(f"{pid} didn't eat lunch.")
        elif ID[pid] == 1: # 이미 먹음
            print(f"{pid} already left seat.")
        else: # 먹는 중
            print(f"{pid} leaves from the seat ({ID[pid][0]}, {ID[pid][1]}).")
            table[ID[pid][0]][ID[pid][1]] = 0
            ID[pid] = 1


