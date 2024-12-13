import bisect

n, q = map(int, input().split())
mileage = list(map(int, input().split()))
mileage.sort()
setMileage = set(mileage) # hash -> 상수시간에 탐색

for _ in range(q):
    m = int(input())
    if m not in setMileage: # list 에서 있는지 확인하려면 리스트 전체를 다 뒤져야 하는데 너무 길어요 (5만*20만..> 10억)
        print(0)
    else:
        idx = bisect.bisect_left(mileage, m)
        print(idx*(n-idx-1)) # 자기보다 작은거 x 자기보다 큰거 개수