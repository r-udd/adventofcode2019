from collections import defaultdict

def printcave(cave, portals, maxx, maxy):
    with open('test2processed.txt', mode='w') as f:
        for y in range(maxy+1):
            for x in range(maxx+1):
                pos = (x, y)
                if pos in portals:
                    f.write(portals[pos])
                else:
                    f.write(cave[(x, y)])
            f.write('\n')

cave = defaultdict(lambda: '.')
portals = {}
with open('test2.txt') as f:
    maxx = 0
    maxy = 0
    for y, l in enumerate(f):
        for x, char in enumerate(l[:-1]):
            maxx = max(x, maxx)
            if char == '#':
                cave[(x, y)] = '#'
                continue
            if char == ' ':
                cave[(x, y)] = '#'
                continue
            elif char.isupper():
                portals[(x, y)] = char
            cave[(x, y)] = '.'
        maxy = max(y, maxy)

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
changed = True
while changed:
    changed = False
    for pos, tile in cave.items():
        if pos not in portals and tile == '.':
            count = 0
            for d in dirs:
                count += cave[(pos[0] + d[0], pos[1] + d[1])] == '#'
                # count += cave[(pos[0] + d[0], pos[1] + d[1])] == '*'
            if count == 3:
                cave[pos] = '#'
                changed = True


printcave(cave, portals, maxx, maxy)
