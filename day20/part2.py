from collections import defaultdict

def isouter(portal, maxx, maxy):
    x = portal[0]
    y = portal[1]
    return x < 5 or y < 5 or y > maxy-5 or x > maxx -5

def printcave(cave, portals):
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            pos = (x, y)
            if pos in portals:
                if isouter(pos, len(cave[0]), len(cave)):
                    print('$', end='')
                else:
                    print('@', end='')
            else:
                print(cave[y][x], end='')
        print()


cave = []
portalpos = {}
portals = {}
with open('processed.txt') as f:
    maxx = 0
    maxy = 0
    for y, l in enumerate(f):
        cave.append([])
        for x, char in enumerate(l.rstrip()):
            maxx = max(x, maxx)
            cave[y].append(char)

        maxy = max(y, maxy)

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (-2,0)]
for y, l in enumerate(cave):
    startportal = False
    for x, char in enumerate(l):
        if char.isupper() and startportal:
            label = cave[y][x-1] + char
            for d in dirs:
                if cave[d[1]+y][d[0]+x] == '.':
                    pos = (d[0]+x, d[1]+y)
                    break
            portalpos[pos] = label
            startportal = False
            if label not in portals:
                portals[label] = [pos]
            else:
                portals[label].append(pos)
        elif char.isupper():
            startportal = True

def calcdist(cave, start, portalspos, portals, target, maxx, maxy):
    todo = [(start, 0, 0)]
    visited = set()
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while todo:
        pos, steps, level = todo.pop(0)
        visited.add(pos + (level,))
        for d in dirs:
            newx = pos[0] + d[0]
            newy = pos[1] + d[1]
            newpos = (newx,newy)
            if cave[newy][newx] == '#':
                continue
            if newpos == target and level == 0:
                return steps + 1
            elif newpos + (level,) in visited:
                continue
            elif newpos in portalpos:
                label = portalpos[newpos]
                pair = portals[label].copy()
                pair.remove(newpos)
                if len(pair) == 0:#'AA' and 'ZZ'
                    continue
                isout = isouter(newpos, maxx, maxy)
                if isout and level > 0:
                    todo.append((pair[0], steps + 2, level - 1))
                elif not isout:
                    todo.append((pair[0], steps + 2, level + 1))
            elif cave[newy][newx] == '.':
                todo.append((newpos, steps + 1, level))

#printcave(cave, portalpos)
start = portals['AA'][0]
target = portals['ZZ'][0]
print(calcdist(cave, start, portalpos, portals, target, maxx, maxy))