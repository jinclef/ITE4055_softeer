h,k,r = map(int, input().split())

def merge(list1, list2):
    lst = []
    for i in range(len(list1)):
        lst.append(list1[i])
        lst.append(list2[i])
    return lst

tasks = [] # 2차원 배열
for _ in range(2**h):
    tasks.append(list(map(int, input().split())))

for i in range(1,h+1): # level
    tasks2 = [] # merge 결과 저장
    for j in range(2**(h-i)): # 두개씩 merge 한다. 레벨 i 에서 생기는 쌍의 수
        if (i%2): # level 이 홀수 - 오른쪽 먼저
            tasks2.append(merge(tasks[2*j+1], tasks[2*j]))
        else:
            tasks2.append(merge(tasks[2*j], tasks[2*j+1]))
    tasks = tasks2

# print(tasks2)
# 처음 h 날만큼은 완료된 게 없음
print(sum(tasks[0][:r-h]))
