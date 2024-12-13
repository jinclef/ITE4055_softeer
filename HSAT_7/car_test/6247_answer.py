import bisect

n, q = map(int, input().split())
mileage = list(map(int, input().split()))
mileage.sort()

for _ in range(q):
    m = int(input())
    if m not in mileage:
        print(0)
    else:
        idx = bisect.bisect_left(mileage, m)
        print(idx*(n-idx-1)) # 자기보다 작은거 x 자기보다 큰거 개수