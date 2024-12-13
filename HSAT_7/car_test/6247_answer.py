import bisect

n, q = map(int, input().split())
mileage = list(map(int, input().split()))
mileage.sort()
setMileage = set(mileage) # hash -> 상수시간에 탐색

for _ in range(q):
    m = int(input())
    idx = bisect.bisect_left(mileage, m) # 들어있으면 본인 위치, 들어있지 않으면 삽입될 위치를 나타내는 값이다.
    if idx != n and m == mileage[idx]:
        print(idx*(n-idx-1)) # 자기보다 작은거 x 자기보다 큰거 개수
    else: # 없는 값
        print(0)