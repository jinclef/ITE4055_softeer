N,M,Q = map(int, input().split())

left_people = []
eating_people = []
is_eating = [[[0] * i for i in range (N)] * j for j in range(M)]
seat = [[[((N-1)**2 + (M-1)**2)**(1/2)] * i for i in range (N)] * j for j in range(M)]

def find_most_safe_seat(row, col):
    max = 1
    max_x = 0
    max_y = 0
    end_x = row
    end_y = col
    for x in range(row):
        for y in range(col):
            if (is_eating[end_x][end_y] == 1):
                distance = ((end_x-x)**2 + (end_y-y)**2) ** (1/2)
                if distance > max:
                    max = distance
                    max_x = x
                    max_y = y
            else:
                end_x -=1
                end_y -=1 
    if max == 1:
        return False, -1, -1
    else:
        for x in range(row):
            for y in range(col):
                distance = ((end_x-x)**2 + (end_y-y)**2) ** (1/2)
        return True, max_x, max_y


for i in range(Q):
    input_line = input().split()
    inout = input_line[0]
    id = int(input_line[1])
    if (inout == "In"):
        if id in left_people or id in eating_people:
            print(f"{id} already ate lunch.")
        else:
            is_fulled, x, y = find_most_safe_seat(M, N)
            if is_fulled:
                print("There are no more seats.")
            else: # success
                eating_people.append(id)
                update_seat(id, x, y)
                print(f"{id} gets the seat ({x}, {y}).")
    else: #inout == "Out"
        if id in left_people:
            print(f"{id} already left seat.")
        elif id in eating_people:
            flush_seat(id)
            eating_people.remove(id)
            left_people.append(id)
            print(f"{id} leaves from the seat ({x}, {y}).")