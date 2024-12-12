n,t = map(int, input().split())
signal = []

for row in range(n):
    temp = []
    for col in range(n):
        temp.append(list(map(int, input().split())))
    signal.append(temp)

# 신호 1~12 저장
# 들어오는 방향, 나가는 방향 4x4 조합
# 즉 4x4x12 짜리 -> 0번포함해서 13개
# signalInfo[i][j][k] : i 는 신호 번호, j 는 들어오는 방향, k 는 나가는 방향
signalInfo = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(13)]
# 0: ->
# 1: -/
# 2: <-
# 3: -\
# signalInfo[1][0][1] = signal[1][0][2] = signal[1][0][3] = 1
# signalInfo[2][1][2] = signal[2][1][3] = signal[2][1][0] = 1
# signalInfo[3][2][3] = signal[3][2][0] = signal[3][2][1] = 1
# signalInfo[4][3][0] = signal[4][3][1] = signal[4][3][2] = 1
for i in range(4):
    # 신호 1-4
    signalInfo[i+1][i][(i+1)%4] = 1 # 위에 주석에서 젤 왼쪽에 해당하는 것들
    signalInfo[i+1][i][(i+2)%4] = 1 # 중간
    signalInfo[i+1][i][(i+3)%4] = 1 # 젤 오른쪽
    # 신호 5-8
    signalInfo[i+5][i][(i+2)%4] = 1
    signalInfo[i+5][i][(i+3)%4] = 1
    # 신호 9-12
    signalInfo[i+9][i][(i+1)%4] = 1
    signalInfo[i+9][i][(i+2)%4] = 1

junction = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)] # 0 ~ n-1
junction[0][0][1] = 1 # 자동차 위치
junction2 = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)] # 초기화 편의
visit = [[0 for _ in range(n)] for _ in range(n)]
visit[0][0] = 1

def update(time, row, col, inDir, outDir, junction, junction2):
    signalNow = signal[row][col][time%4]
    if signalInfo[signalNow][inDir][outDir]:
        if (outDir == 0) and col != 0:
            junction2[row][col-1][2] = 1
            visit[row][col-1] = 1
        elif outDir == 1 and row != n-1:
            junction2[row+1][col][3] = 1
            visit[row+1][col] = 1
        elif outDir == 2 and col != n-1:
            junction2[row][col+1][0] = 1
            visit[row][col+1] = 1
        elif outDir == 3 and row != 0:
            junction2[row-1][col][1] = 1
            visit[row-1][col] = 1
    return

for time in range(t):
    for row in range(n):
        for col in range(n):
            for inDir in range(4):
                if (junction[row][col][inDir]): # 거기 차가 있을 때만
                    for outDir in range(4):
                        update(time, row, col, inDir, outDir, junction, junction2)
                    junction[row][col][inDir] = 0 # 차가 지나갔으니 없음.
    junction, junction2 = junction2, junction
