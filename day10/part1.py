class obj ():

    def __init__(self, inp):
        self.blocked = False
        self.isast = inp == '#'

def printmap (m):
    for yline in m:
        for x in yline:
            if x.isast:
                print('#', end='')
            else:
                print('.', end='')
        print()

with open('input') as f:
    astmap = [[obj(x) for x in line.rstrip()] for line in f.readlines()]
    xmax = len(astmap[0])
    ymax = len(astmap)
maxfound = -1
printmap(astmap)
print('xmax', xmax)
print('ymax', ymax)
for y in range(ymax):
    for x in range(xmax):
        if not astmap[y][x].isast:
            continue
        # print(x, y)

        for ydiff in range(0-y, ymax-y+1):
            # print(ydiff)
            for xdiff in range(0-x, xmax-x+1):
                if xdiff == 0 and ydiff == 0:
                    continue
                xcurr = x
                ycurr = y
                found = False
                while xcurr + xdiff in range(xmax) and ycurr+ydiff in range(ymax):
                    xcurr += xdiff
                    ycurr += ydiff
                    if found and astmap[ycurr][xcurr].isast:
                        astmap[ycurr][xcurr].blocked = True
                    elif astmap[ycurr][xcurr].isast:
                        found = True

        count = 0
        for line in astmap:
            for ast in line:
                if ast.isast and not ast.blocked:
                    count += 1
                if ast.isast:
                    ast.blocked = False
        # print('count', count, x, y)
        # if count > maxfound:
        #     print('new max', x, y)
        maxfound = max(count, maxfound)

print(maxfound-1)
