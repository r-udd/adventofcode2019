from collections import defaultdict

def printcave(cave, player, keys, doors, maxx, maxy):
    with open('processed.txt', mode='w') as f:
        for y in range(maxy+1):
            for x in range(maxx+1):
                pos = (x, y)
                if pos == player:
                    f.write('@')
                elif pos in keys:
                    f.write(keys[pos])
                elif pos in doors:
                    f.write(doors[pos])
                else:
                    f.write(cave[(x, y)])
            f.write('\n')

cave = defaultdict(lambda: '.')
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

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
changed = True
while changed:
    changed = False
    for pos, tile in cave.items():
        if pos not in keys and tile == '.':
            count = 0
            for d in dirs:
                count += cave[(pos[0] + d[0], pos[1] + d[1])] == '#'
                # count += cave[(pos[0] + d[0], pos[1] + d[1])] == '*'
            if count == 3:
                cave[pos] = '#'
                changed = True
                if pos in doors:
                    doors.pop(pos)
printcave(cave, player, keys, doors, maxx, maxy)
