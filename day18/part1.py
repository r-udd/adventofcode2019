from collections import defaultdict
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def printcave(cave, player, keys, doors, maxx, maxy):
    for y in range(maxy+1):
        for x in range(maxx+1):
            pos = (x,y)
            if pos == player:
                print('@', end='')
            elif pos in keys:
                print(keys[pos], end='')
            elif pos in doors:
                print(doors[pos], end='')
            else:
                print(cave[(x,y)], end='')
        print()

def findnextkey(cave, player, keys, doors):
    todo = [(player, 0)]
    visited = set()
    dirs = [(0,-1), (0,1), (-1,0), (1,0)]
    possiblekeys = []
    while todo:
        pos, steps = todo.pop(0)
        visited.add(pos)
        for d in dirs:
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if cave[newpos] == '#':
                continue
            elif newpos in doors:
                continue
            elif newpos in visited:
                continue
            elif newpos in keys:
                possiblekeys.append((newpos, steps + 1))
            elif cave[newpos] == '.':
                todo.append((newpos, steps + 1))
    return possiblekeys


cave = defaultdict(lambda : '#')
keys = {}
doors = {}
player = ()
with open('test2.txt') as f:
    maxx = 0
    maxy = 0
    for y, l in enumerate(f):
        for x, char in enumerate(l.rstrip()):
            maxx = max(x, maxx)
            if char == '#':
                cave[(x,y)] = '#'
                continue
            elif char == '@':
                player = (x,y)
            elif char.isupper():
                doors[(x,y)] = char
            elif char.islower():
                keys[(x,y)] = char
            cave[(x,y)] = '.'
        maxy = max(y, maxy)            

printcave(cave, player, keys, doors, maxx, maxy)

steps = 0
while keys:
    possiblekeys = findnextkey(cave, player, keys, doors)
    if len(possiblekeys) == 1:
        steps += possiblekeys[0][1]
        player = possiblekeys[0][0]
        key = keys.pop(player)
        for pos, val in doors.items():
            if val.lower() == key:
                doors.pop(pos)
                break
    else:
        print('PRINT')
        printcave(cave, player, keys, doors, maxx,maxy)
        pass
        
print(steps)