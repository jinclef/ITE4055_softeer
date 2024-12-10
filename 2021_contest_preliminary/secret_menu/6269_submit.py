M, N, K = map(int, input().split())

# 비밀메뉴 조작법 (length = M)
secret = list(map(int, input().split()))

# 사용자의 버튼 조작 (length = N)
user = list(map(int, input().split()))

result = False
for i in range (len(user)):
    if result==True:
        break

    if (user[i] == secret[0]):
        temp = True
        idx = 0
        while (temp and i+idx < len(user) and idx < len(secret)):
            if (user[i+idx] != secret[idx]):
                temp=False
            if (temp and idx == len(secret)-1):
                result=True
                break
            idx+=1

if (result):
    print("secret")
else:
    print("normal")