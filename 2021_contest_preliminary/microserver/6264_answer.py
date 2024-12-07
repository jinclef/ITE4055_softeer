t = int(input())

for i in range(t):
    n = int(input())
    task = list(map(int, input().split())) # services
    task.sort()
    # print(task)
    
    start_idx = 0
    end_idx = n-1

    servers = 0 #cnt

    # 601~900: 단독 서버에 저장
    while (start_idx <= end_idx and task[end_idx] > 600): # end_idx > start_idx 는 out of range 에러 예방용
        servers +=1
        end_idx -=1
    
    # 600: 300과 쌍을 이룬다.
    while (start_idx < end_idx and task[start_idx] == 300 and task[end_idx] == 600): # 위와 같은 조건이 있으면 더 안전하겠지만 조건 상 일어날 수 없긴 함
        servers +=1
        end_idx -=1
        start_idx +=1
    
    # 위에서 쌍을 이루고 남은 300, 600을 정리한다
    # 300은 빨리 정리 못함. 남은 600만 정리하자
    num300 = 0
    while (start_idx <= end_idx and task[start_idx] == 300):
        num300 +=1
        start_idx +=1
    
    # 301~600: 양극단끼리 짝을 이루면 된다.
    while (start_idx < end_idx):
        if (task[start_idx] + task[end_idx] <= 900):
            servers +=1
            start_idx +=1
            end_idx -=1
        # end_idx 의 경우 자기랑 같이 짝을 이뤄줄 남은 300을 찾는다.
        elif (num300 > 0):
            servers +=1
            end_idx -=1
            num300 -=1
        # 300도 없으면 그냥 혼자 들어간다.
        else:
            servers +=1
            end_idx -=1
    
    # 짝을 맞춰주고 하나가 남은 경우 서버 하나 할당해주기.
    if (start_idx == end_idx):
        servers +=1

        # 300: 남은 300끼리 3개당 한 서버씩 넣어준다.
        #? 이거 왜 들여쓰기 해야 되지?
        if (num300 > 0):
            servers += (num300+2)//3
    
    print(servers)