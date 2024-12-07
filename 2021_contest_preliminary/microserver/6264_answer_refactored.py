t = int(input())
for i in range(t):
    n = int(input())
    task = list(map(int, input().split()))
    task.sort()

    num300 = 0
    for j in range(n):
        if task[j] <=300:
            num300 +=1
    
    servers = 0
    start = num300
    end = n-1

    while (start <= end):
        servers +=1
        if task[end] > 600:
            pass
        elif start != end and task[start] + task[end] <= 900:
            start +=1
        elif num300 > 0:
            num300 -=1
        end -=1

    servers += (num300+2) // 3
    print(servers)