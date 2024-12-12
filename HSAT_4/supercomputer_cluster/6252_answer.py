n, b = map(int, input().split())
a = list(map(int, input().split()))


def test(x):
    cost = 0
    for i in range(n):
        if (a[i] < x):
            cost += (x-a[i])*(x-a[i])
    return cost <= b

low, high = 1, 2*10**9
while low < high:
    mid = (low+high+1)//2
    if (test(mid)):
        low=mid
    else:
        high = mid-1

print(low) # low == high 겠지.