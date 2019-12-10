import math

class obj ():

    def __init__(self, char, x, y):
        self.blocked = False
        self.isast = char == '#'
        self.x = x
        self.y = y

def printmap (m):
    for yline in m:
        for x in yline:
            if x.isast:
                print('#', end='')
            else:
                print('.', end='')
        print()

with open('input') as f:
    astmap = []
    for y, line in enumerate(f.readlines()):
        linemap = []
        for x, char in enumerate(line):
            linemap.append(obj(char, x, y))
        astmap.append(linemap)
    xmax = len(astmap[0])
    ymax = len(astmap)

maxfound = -1
printmap(astmap)
print('xmax', xmax)
print('ymax', ymax)


stationx = 26
stationy = 29

#test5
# stationx = 11
# stationy = 13
#test6
# stationx = 8
# stationy = 3
astmap[stationy][stationx].blocked = True

for ydiff in range(0-stationy, ymax-stationy+1):
    # print(ydiff)
    for xdiff in range(0-stationx, xmax-stationx+1):
        if xdiff == 0 and ydiff == 0:
            continue
        xcurr = stationx
        ycurr = stationy
        found = False
        while xcurr + xdiff in range(xmax) and ycurr+ydiff in range(ymax):
            xcurr += xdiff
            ycurr += ydiff
            if found and astmap[ycurr][xcurr].isast:
                astmap[ycurr][xcurr].blocked = True
            elif astmap[ycurr][xcurr].isast:
                found = True

flat = []
for line in astmap:
    for ast in line:
        if ast.isast and not ast.blocked:
            flat.append(ast)

def angle (ast):
    degrees = math.degrees(math.atan2(
        ast.x - stationx, -(ast.y - stationy))) % 360.0
    return degrees

print(angle(obj('#', stationx-1, stationy+1)))

s = sorted(flat, key=angle)

print(s[199].x*100 + s[199].y)
