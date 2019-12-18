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


def findnextkey(cave, p, minsteps):
    todo = [(p['player'], 0)]
    visited = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    possiblekeys = []
    while todo:
        pos, steps = todo.pop(0)
        if steps > minsteps:
            continue
        visited.add(pos)
        for d in dirs:
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if cave[newpos] == '#':
                continue
            elif newpos in p['doors']:
                continue
            elif newpos in visited:
                continue
            elif newpos in p['keys']:
                possiblekeys.append((newpos, steps + 1))
            elif cave[newpos] == '.':
                todo.append((newpos, steps + 1))
    return possiblekeys


cave = defaultdict(lambda: '#')
keys = {}
doors = {}
player = ()
with open('input.txt') as f:
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
            elif char.isupper():
                doors[(x, y)] = char
            elif char.islower():
                keys[(x, y)] = char
            cave[(x, y)] = '.'
        maxy = max(y, maxy)

printcave(cave, player, keys, doors, maxx, maxy)

minsteps = 100000
possibilities = [{'player': player, 'keys': keys, 'doors': doors, 'steps': 0}]
possindex = 0
while possindex < len(possibilities):
    #print('possindex', possindex, possibilities[possindex]['steps'])

    # printcave(cave, possibilities[possindex]['player'],
    #           possibilities[possindex]['keys'], possibilities[possindex]['doors'], maxx, maxy)
    if possibilities[possindex]['steps'] > minsteps:
        possindex += 1
        continue
    possiblekeys = findnextkey(
        cave, possibilities[possindex], minsteps - possibilities[possindex]['steps'])
    if len(possiblekeys) == 0:
        possindex += 1
        continue
    if len(possiblekeys) != 1:
        for newi in range(1, len(possiblekeys)):
            newposs = {'player': possiblekeys[newi][0]}
            newposs['steps'] = possibilities[possindex]['steps'] + \
                possiblekeys[newi][1]
            newposs['keys'] = possibilities[possindex]['keys'].copy()
            key = newposs['keys'].pop(possiblekeys[newi][0])

            doors = possibilities[possindex]['doors'].copy()
            for pos, val in doors.items():
                if val.lower() == key:
                    doors.pop(pos)
                    break
            newposs['doors'] = doors
            possibilities.append(newposs)

    possibilities[possindex]['steps'] += possiblekeys[0][1]
    player = possiblekeys[0][0]
    possibilities[possindex]['player'] = player
    key = possibilities[possindex]['keys'].pop(player)
    # print('key', key)
    for pos, val in possibilities[possindex]['doors'].items():
        if val.lower() == key:
            possibilities[possindex]['doors'].pop(pos)
            break
    if len(possibilities[possindex]['keys']) == 0:
        # No keys left, done.
        prevmin = minsteps
        minsteps = min(minsteps, possibilities[possindex]['steps'])
        possindex += 1
        if prevmin != minsteps:
            print('minsteps', minsteps, 'index', possindex)

print(minsteps)
