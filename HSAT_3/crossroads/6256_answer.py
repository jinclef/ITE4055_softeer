from collections import deque

n = int(input())
car = []
for i in range(1, n+1): # i: carIdx
    t,w = input().split()
    car.append([i, int(t), w])

car.append([n+1, 10**9+1, 'A']) # car 길이 확인 계속 해줘야 함. 생략을 위한 설정
carIdx = 0
ans = [-1]*(n+1)
deq = [deque() for _ in range(4)]

counter = 0

while counter <= 10**9:
    tempCar = car[carIdx]
    number, time, w = tempCar
    while time <= counter:
        if w=='A' : deq[0].append(tempCar)
        elif w=='B': deq[1].append(tempCar)
        elif w=='C' : deq[2].append(tempCar)
        else: deq[3].append(tempCar)
        carIdx +=1
        tempCar = car[carIdx]
        number, time, w = tempCar
    if deq[0] and deq[1] and deq[2] and deq[3]:
        # time > counter 인 경우 -> 종료
        break
    if not deq[0] and not deq[1] and not deq[2] and not deq[3]:
        # 다 비어있는 경우 -> 다음 자동차가 들어오는 시간으로 시간 땡긴다.
        counter = time
        continue

    for i in range(4):
        # 교차로 통과
        if deq[i] and not deq[(i+3)%4]: # deq[0] is of A, deq[0] is of B, ... # 사실은 i-1 인데.. 그냥 모듈로 결과가 -1이 나올 수 있어서 이를 방지함.
            x = deq[i].popleft()
            number,_,_ = x
            ans[number] = counter
            # A와 C, B와 D 는 동시에 진행 가능
            if deq[(i+2)%4] and not deq[(i+1)%4]:
                x = deq[(i+2)%4].popleft()
                number,_,_ = x
                ans[number] = counter
            break
    counter +=1

for i in range(1, n+1):
    print(ans[i])