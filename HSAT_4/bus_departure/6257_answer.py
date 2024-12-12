n = int(input())
a = list(map(int, input().split()))

more = [[0 for _ in range(n)] for _ in range(n)] # i~k 사이의 값 개수
total = 0
for i in range(n):
    for k in range(i+1, n): # 사실 i+2 부터 됨 중간에 j 있어서..
        if a[i] < a[k]: # 문제 조건 상 같을 수는 없음.
            more[i][k] = more[i][k-1]+1
        else:
            more[i][k] = more[i][k-1]
            total += more[i][k]

print(total)