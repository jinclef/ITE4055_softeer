NUMBER = {
    1 : [0,0,1,0,0,1,0],
    2 : [1,0,1,1,1,0,1],
    3 : [1,0,1,1,0,1,1],
    4 : [0,1,1,1,0,1,0],
    5 : [1,1,0,1,0,1,1],
    6 : [1,1,0,1,1,1,1],
    7 : [1,1,1,0,0,1,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,1,1,0,1,1],
    0 : [1,1,1,0,1,1,1]
}

T = int(input()) # 테스트 케이스 개수
ans = []

def get_1(number):
    count = 0
    for i in range(7):
        if NUMBER[number][i] == 1:
            count +=1
    # print("get 1 is ", count)
    return count

for i in range(T):
    test_case = list(map(int, input().split()))
    A = test_case[0]
    B = test_case[1]

    cnt = 0
    while (B > 0 or A > 0):
        # 일의 자리 수
        remainder_A = A%10
        remainder_B = B%10
        # print(f"\nA is {A} and remainder A is {remainder_A}")
        # print(f"B is {B} and remainder B is {remainder_B}")
        temp = 0
        if remainder_A == 0 and A == 0:
            temp += get_1(remainder_B)
        elif remainder_B == 0 and B == 0:
            temp += get_1(remainder_A)
        else:
            for i in range (7):
                if NUMBER[remainder_A][i] != NUMBER[remainder_B][i]:
                    temp +=1
        A = A//10
        B = B//10
        cnt += temp
        # print("temp sum is ",temp)
    ans.append(cnt)

for i in range (len(ans)):
    print(ans[i])