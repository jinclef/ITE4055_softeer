N,M,K = map(int, input().split())
A = list(input().split())
B = list(input().split())
C = [[0]*M for _ in range(N)]

longest = 0
for a in range(N):
    for b in range(M):
        if A[a] ==B[b]:
            if a-1<0 or b-1<0:
                C[a][b] = 1
            else:
                C[a][b] = C[a-1][b-1]+1
            longest = max(longest, C[a][b])

print(longest)