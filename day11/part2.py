import queue as q
import intcode as comp

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

currdir = 0

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()

miny = 9999
minx = 9999
maxx = -9999
maxy = -9999

pos = (0,0)
paint = {}

while 1:
    try:
        if len(paint) == 0:
            inq.put(1)
        elif pos not in paint:
            inq.put(0)
        else:
            inq.put(paint[pos])
        color = outq.get(timeout=5)
        paint[pos] = color
        newdir = outq.get(timeout=5)
        if newdir == 1:
            currdir = (currdir + 1) % 4
        elif newdir == 0:
            currdir = (currdir - 1) % 4
        else:
            print('SHIT')

        pos = (pos[0] + dirs[currdir][0],pos[1] + dirs[currdir][1])
        minx = min(pos[0], minx)
        miny = min(pos[1], miny)
        maxx = max(pos[0], maxx)
        maxy = max(pos[1], maxy)
    except q.Empty as err:
        break

for y in range(miny,maxy+1):
    for x in range(minx, maxx+1):
        pos = (x,y)
        if pos in paint and paint[pos] == 1:
            print('X', end='')
        else:
            print(' ', end='')
    print()
