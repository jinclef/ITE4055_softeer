n = int(input())
a = list(map(int, input().split()))

# i 는 안바뀌기 때문에 굳이 more 이 2차원 배열일 필요 없음.
more = [0 for _ in range(n)]
total = 0
for i in range(n):
    more[i] = 0 # 재활용하니까 초기화 해줘야 함.
    for k in range(i+1, n): # 사실 i+2 부터 됨 중간에 j 있어서..
        more[k] = more[k-1] # if, else에서 같은 동작
        if a[i] < a[k]: # 문제 조건 상 같을 수는 없음.
            more[k] +=1
        else:
            more[k] = more[k-1]
            total += more[k]

print(total)