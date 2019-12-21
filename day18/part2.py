from collections import defaultdict
from heapq import *

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

def calcdist(cave, mem, start, keys, doors):
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
            elif newpos in doors:
                keysneeded.append(doors[newpos].lower())
                todo.append((newpos, steps + 1, keysneeded.copy()))
            elif newpos in keys:
                mem[(start,newpos)] = [steps + 1, keys[newpos], keysneeded]
                c = keysneeded.copy()
                c.append(keys[newpos])
                todo.append((newpos, steps + 1, c))
            elif cave[newpos] == '.':
                todo.append((newpos, steps + 1, keysneeded.copy()))

def getallpossibilities(mem, start, keys, currkeys, step, minstep, keyposs):
    possible = {}
    for pos, letter in keys.items():
        #if letter not in currkeys:
        if (start, pos) in mem:
            _, letter, neededkeys = mem[(start, pos)]
            for nk in neededkeys:
                if nk not in currkeys:
                    break
            else:
                possible[pos] = letter
    return possible

tot = 0
for fileletter in ['a', 'b', 'c', 'd']:
    cave = defaultdict(lambda: '#')
    keys = {}
    keyposs = {}
    doors = {}
    player = ()
    with open('input2' + fileletter + '.txt') as f:
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

    #printcave(cave, player, keys, doors, maxx, maxy)
    mem = {}
    calcdist(cave, mem, player, keys, doors)

    keylist = list(keys.keys())
    for i in range(len(keylist)):
        calcdist(cave, mem, keylist[i], keys, doors)
    print(len(mem))
    currkeys = ""
    bestkey = {}
    bestkey[('', player)] = 0
    workq = []
    heappush(workq, [[0], 0, player, currkeys, ''])
    minstep = 10000
    print('Start going through the possible paths')
    while workq:
        _, step, start, currkeys, o = heappop(workq)
        if start in keys:
            letter = keys[start]
        else:
            letter = '@'
        # print(len(currkeys), len(keys))
        # input('STOP')
        if step >= minstep:
            continue
        if len(keys) == len(currkeys):
            if step < minstep:
                minstep = step
                print('Antalet steg', step, 'remaining heap', len(workq))
                print(o)
            else:
                print('steg', step)
            continue
        elif len(keys) < len(currkeys):
            print('NOES')
        possibilities = getallpossibilities(mem, start, keys, currkeys, step, minstep, keyposs)
        for p, letter in possibilities.items():
            if letter not in currkeys:
                c = currkeys + letter
                c = ''.join(sorted(c))
            else:
                c = currkeys
            onext = o+letter
            nextstep = step + mem[(start, p)][0]
            if (c, p) not in bestkey:
                bestkey[(c, p)] = nextstep
                heappush(workq, [[nextstep], nextstep, p, c, onext])
            else:
                # if bestkey[ls] > nextstep:
                #     bestkey[ls] = nextstep
                if bestkey[(c, p)] > nextstep:
                    bestkey[(c, p)] = nextstep
                    heappush(workq, [[nextstep], nextstep, p, c, onext])
    tot += minstep
print(tot)
