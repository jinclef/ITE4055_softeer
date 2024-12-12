def matchDirection(direction):
    if (direction == 0): # l
        return '<'
    elif (direction == 2): # r
        return '>'
    elif (direction == 1): # u
        return '^'
    else: # d
        return 'v'

def turnDirection(before, after):
    if (before < after):
        return "R"*(after-before)
    elif (before == 3 and after == 0):
        return "R"
    elif (before > after):
        return "L" * (before-after)
    elif (before ==0 and after == 3):
        return "L"

def calNextNode(next_dir, current, current_x, current_y):
    if next_dir == 0: # l
        return [current_x-2, current_y]
    elif next_dir == 1: # u
        return [current_x, current_y+2]
    elif next_dir == 2: # r
        return [current_x+2, current_y]
    elif next_dir == 3: # d
        return [current_x, current_y-2]

def getNextNode(current, current_dir, current_x, current_y):
    if len(current) == 1:
        direction = current[0]
        return calNextNode(direction, current, current_x, current_y)
    
    elif len(current) == 2:
        first = current[0]
        second = current[1]
        if current_dir == first:
            return calNextNode(direction, second, current_x, current_y)
        else:
            return calNextNode(direction, first, current_x, current_y)
    else:
        print("Error!")
        return

def checkLRUD(arr):
    first_cand = []
    for i in range(H):
        for j in range(W):
            temp = []
            if arr[i-1][j] == '#':
                temp.append(0) # l
            if arr[i+1][j] == '#':
                temp.append(2) # r
            if arr[i][j-1] == '#':
                temp.append(3) # d
            if arr[i][j+1] == '#':
                temp.append(1) # u
            relation[i][j] = [temp]
            if len(temp) == 1:
                first_cand.append([i,j])
    return first_cand

H, W = map(int, input().split())

arr = [[[] for _ in range(W+2)] for _ in range(H+2)]
relation = [[[] for _ in range(W+2)] for _ in range(H+2)]
# print(arr)

for i in range (H):
    row = list(input())
    arr[i] = row

# print(arr)
first_cand = checkLRUD(arr)

first_i, first_j = first_cand[0]
end_i, end_j = first_cand[1]

direction = []
command = []
first_direction = matchDirection(relation[first_i][first_j][0])
direction.append(first_direction)

cnt = 0
x = first_i
y = first_j

while x != end_i and y != end_j:
    current_direction = relation[x][y]
    next_node = getNextNode(relation[first_i][first_j], current_direction, x, y)
    next_node_direction = relation[next_node[0]][next_node[1]]
    if next_node_direction != current_direction:
        command.append(turnDirection(current_direction, next_node_direction))
    
    next_node_direction = current_direction
    x = next_node[0]
    y = next_node[1]
    command.append("A")

print(first_i, first_j)
print(first_direction)
print(command)