def computeRanking(arr):
    ranking = [0] * n # len(arr)
    ans = [0] * n

    # 1. arr 확장
    for i in range(n):
        arr[i] = [arr[i], i]
    arr.sort(reverse=True)

    # 2. 일단 해놓고, 자기 앞이랑 점수 같으면 자기 앞과 같은 랭킹 부여
    cnt = 1
    ranking[0] = 1
    for i in range(1,n):
        if arr[i][0] != arr[i-1][0]:
            cnt = i+1
        ranking[i] = cnt
    
    # 3. ans 에 ranking 넣기
    for i in range(n):
        ans[arr[i][1]] = ranking[i]
    for i in range(n):
        print(ans[i], end=' ')
    print()


n = int(input())
total = [0]*n
for _ in range(3):
    scores = list(map(int, input().split()))
    for i in range(n):
        total[i] += scores[i]
    computeRanking(scores)

computeRanking(total)