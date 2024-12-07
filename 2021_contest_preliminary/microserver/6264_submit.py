def count_servers(arr):
    # 작은 것부터 크기순 정렬: 300 ~> 900
    arr.sort()

    cnt = 0
    # 300 먼저 빼주기
    cnt300 = 0
    for i in arr:
        if (i==300): cnt300+=1
    
    idx_excpt_300 = cnt300

    # 제한 조건에 따라 처리
    # for문은 300 끼리 연산 제외하고 처리하는 것.
    for idx in range(len(arr)-1, cnt300-1, -1):
        if (600 < arr[idx] <= 900):
            cnt +=1
        elif (arr[idx] == 600):
            if (cnt300 > 0):
                cnt300 -=1
            cnt +=1
        elif (300 < arr[idx] < 600):
            if (cnt300 == 0 and idx_excpt_300 == idx): #!
                cnt+=1
                break
            elif (idx_excpt_300 != idx and arr[idx_excpt_300] + arr[idx] <= 900):
                cnt +=1
                idx_excpt_300 += 1
            elif (300 + arr[idx] <= 900):
                cnt300-=1
                cnt +=1
            else:
                cnt +=1
        # else: # arr[idx] == 300
        #     # 3개가 1묶음
        #     cnt += (cnt300+2) // 3
        
        if (idx_excpt_300 > idx-1):
            break
    
    if (cnt300 > 0):
        cnt += (cnt300+2) // 3
    
    return cnt

T = int(input()) # test case count

# input
print_arr = []
for i in range (T):
    N = int(input())
    memarr = list(map(int, input().split())) # 300 300 300
    print_arr.append(count_servers(memarr))

print("\n")

for cnt in print_arr:
    print(cnt)