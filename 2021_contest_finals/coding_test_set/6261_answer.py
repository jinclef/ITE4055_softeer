def test(testSets): # 중간값 검사
    S = [0]*N # S_i: c_i 에, d_{i-1}은 다 썼고 d_i 는 아직 덜 넣은 것.
    S[0] = C[0]
    for i in range(N-1):
        if S[i] >= testSets: # 넉넉한 경우
            S[i+1] = C[i+1] + D[i]
        elif S[i]+D[i] >= testSets: 
            S[i+1] = C[i+1] + (S[i] + D[i] - testSets)
        else:
            return False

    if S[N-1] >= testSets:
        return True
    else:
        return False
    
# cf. 변수 재사용
'''
def testVer2(testSets):
    now = C[0]
    for i in range(N-1):
        if now >= testSets:
            now = C[i+1] + D[i]
        elif now + D[i] >= testSets:
            now = C[i+1] + (now + D[i] - testSets)
        else:
            return False
    
    if now >= testSets:
        return True
    else:
        return False
'''

def bSearch(start, end): # binary search
    if (start==end):
        return start # 그게 답이야~
    
    mid = (start+end+1)//2 # mid 를 포함해서 서치를 하게 되면 start=mid 가 되는 경우가 있는데, 그거 피하기 위해서 +1 해준다.
    if test(mid):
        return bSearch(mid, end)
    else:
        return bSearch(start, mid-1)

N,T = map(int, input().split())
for i in range(T):
    C = [0]*N
    D = [0]*N # N-1
    temp = list(map(int, input().split()))
    for i in range(N-1): # d 가 1~N-1까지만 있어서.
        C[i] = temp[2*i]
        D[i] = temp[2*i+1]
    C[N-1] = temp[2*(N-1)]
    bSearch(0, 2*(10**12))