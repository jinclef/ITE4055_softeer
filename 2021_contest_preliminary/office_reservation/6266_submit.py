N,M = map(int, input().split()) # 회의실 수, 예약된 회의 수

office_name = []
for i in range(N):
    office = input()
    office_name.append(office)

reserved = {}
for i in range(M):
    office_reservation = list(input().split())
    r = office_reservation[0] # office 
    s = int(office_reservation[1]) # start time
    t = int(office_reservation[2]) # end time

    if r not in reserved.keys():
        reserved[r] = [0 * j for j in range(9)]
    
    reserved_time = reserved[r]
    time = s
    result = True
    while (s <= time < t):
        if reserved_time[time-9] == 1:
            result = False
            break
        else:
            reserved_time[time-9] = 1
        time +=1

office_name.sort()

# debug
# for key in reserved.keys():
#     print(key)
#     print(reserved[key])

for office in office_name:
    available = []
    print(f"Room {office}:")
    if (office not in reserved.keys()):
        print("1 available:")
        print("09-18")
    else:
        temp = []
        for idx in range(len(reserved[office])):
            if (reserved[office][idx] == 0):
                temp.append(idx+9)
            else:
                if len(temp)>0:
                    available.append(temp)
                temp = []
        if len(temp)>0:
            available.append(temp)
        if len(available) == 0:
            print("Not available")
        else:
            print(f"{len(available)} available:")
            for i in range(len(available)):
                start = available[i][0]
                end = available[i][len(available[i])-1]+1

                if start<10:
                    start = "0" + str(start)
                if end<10:
                    end = "0" + str(end)
                print(f"{start}-{end}")
    if (office != office_name[-1]):
        print("-----")