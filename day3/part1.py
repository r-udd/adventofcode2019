def manhattan(position):
    return abs(position[0]) + abs(position[1])

with open('input') as f:
    line1 = f.readline().split(',')
    line2 = f.readline().split(',')

dirs = {'U': [0,-1], 'D': [0,1], 'R': [1,0], 'L': [-1,0]}

path = set()
position = [0,0]
for instruction in line1:
    direction = instruction[0]
    amount = int(instruction[1:])
    #print(direction, amount)
    for i in range(1, amount+1):
        position[0] += dirs[direction][0]
        position[1] += dirs[direction][1]
        path.add(tuple(position))
    # print(path)

position = [0, 0]
dist = 9999999999
for instruction in line2:
    direction = instruction[0]
    amount = int(instruction[1:])
    for i in range(1, amount+1):
        position[0] += dirs[direction][0]
        position[1] += dirs[direction][1]
        if tuple(position) in path:
            man = manhattan(position)
            dist = min(man, dist)
print(dist)
