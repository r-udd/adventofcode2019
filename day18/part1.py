from collections import defaultdict
from os import system, name
from heapq import *

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
            pos = (x, y)
            if pos == player:
                print('@', end='')
            elif pos in keys:
                print(keys[pos], end='')
            elif pos in doors:
                print(doors[pos], end='')
            else:
                print(cave[(x, y)], end='')
        print()

def calcdist(cave, start, target, doors):
    todo = [(start, 0, [])]
    visited = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while todo:
        pos, steps, keysneeded = todo.pop(0)
        visited.add(pos)
        for d in dirs:
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if cave[newpos] == '#':
                continue
            elif newpos in visited:
                continue
            elif newpos == target:
                return steps + 1, keysneeded
            elif newpos in keys:
                keysneeded.append(keys[newpos])
                todo.append((newpos, steps + 1, keysneeded.copy()))
            elif newpos in doors:
                keysneeded.append(doors[newpos].lower())
                todo.append((newpos, steps + 1, keysneeded.copy()))
            elif cave[newpos] == '.':
                todo.append((newpos, steps + 1, keysneeded.copy()))
    print('WHY')

forced = {'m': 'd', 'c': 'k', 's': 'w', 'w': 'a', 'l': 'y', 'j': 'q', 'q': 'b', 'g': 'v', 'v': 'h', 'i': 'x', 'x': 'u'}

def getallpossibilities(mem, start, keys, currkeys, step, minstep, keyposs):
    possible = {}
    startletter = ''
    if start in keys:
        startletter = keys[start]
    if startletter in forced:
        targetletter = forced[startletter]
        possible[keyposs[targetletter]] = targetletter
    for pos, letter in keys.items():
        if letter not in currkeys:
            neededstep, neededkeys = mem[(start, pos)]
            for nk in neededkeys:
                if nk not in currkeys:
                    break
            else:
                if neededstep + step < minstep:
                    possible[pos] = letter
                # else:
                #     print('Too large')
    return possible
    


cave = defaultdict(lambda: '#')
keys = {}
keyposs = {}
doors = {}
player = ()
with open('processedman2.txt') as f:
    maxx = 0
    maxy = 0
    for y, l in enumerate(f):
        for x, char in enumerate(l.rstrip()):
            maxx = max(x, maxx)
            if char == '#':
                cave[(x, y)] = '#'
                continue
            elif char == '@':
                player = (x, y)
                keyposs[char] = (x,y)
            elif char.isupper():
                doors[(x, y)] = char
            elif char.islower():
                keys[(x, y)] = char
                keyposs[char] = (x,y)
            cave[(x, y)] = '.'
        maxy = max(y, maxy)

printcave(cave, player, keys, doors, maxx, maxy)
precalc = {}
mem = {}
for pos in keys.keys():
    steps, keysneeded = calcdist(cave, player, pos, doors)
    mem[(player,pos)] = [steps, keysneeded]
    mem[(player,pos)] = [steps, keysneeded]

keylist = list(keys.keys())
for i in range(len(keylist)):
    for j in range(i+1, len(keylist)):
        steps, keysneeded = calcdist(cave, keylist[i], keylist[j], doors)
        mem[(keylist[i], keylist[j])] = [steps, keysneeded]
        mem[(keylist[j], keylist[i])] = [steps, keysneeded]
        
currkeys = set()
workq = []
heappush(workq, [[0], 0, player, currkeys])
minstep = 10000
print('Start going through the possible paths')
while workq:
    _, step, start, currkeys = heappop(workq)
    # print(len(currkeys), len(keys))
    # input('STOP')
    if step >= minstep:
        continue
    if len(keys) == len(currkeys):
        if step < minstep:
            minstep = step
            print('Antalet steg', step, 'remaining heap', len(workq))
        else:
            print('steg', step)
    possibilities = getallpossibilities(mem, start, keys, currkeys, step, minstep, keyposs)
    for p,letter in possibilities.items():
        c = currkeys.copy()
        c.add(letter)
        nextstep = step + mem[(start, p)][0]
        if nextstep < minstep:
            heappush(workq, [[-nextstep], nextstep, p, c])
print(minstep)

#lägre än 4034