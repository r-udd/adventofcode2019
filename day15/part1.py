from collections import defaultdict
from os import system, name
import queue as q
import intcode as comp
from readchar import readchar

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()

def printmap(map, posx, posy, minx, maxx, miny, maxy):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if x == posx and y == posy:
                print('R', end='')
            else:
                print(map[(x,y)], end='')
        print()

minx = 0
miny = 0
maxx = 0
maxy = 0
shipmap = defaultdict(lambda : ' ')
x = 0
y = 0
shipmap[(x,y)] = '.'
inp = 'start'
while inp != 'p':
    clear()
    printmap(shipmap, x, y, minx, maxx, miny, maxy)
    print(x, y)
    inp = readchar()
    nextx = x
    nexty = y
    if outq.get() != 'i':
        print('Something is wrong')
    if inp == b'p':
        break
    elif inp == b'w':
        inq.put(1)
        nexty += -1
    elif inp == b's':
        inq.put(2)
        nexty += 1
    elif inp == b'a':
        inq.put(3)
        nextx += -1
    elif inp == b'd':
        inq.put(4)
        nextx += 1
    else:
        continue

    minx = min(minx, nextx)
    miny = min(miny, nexty)
    maxx = max(maxx, nextx)
    maxy = max(maxy, nexty)
    ret = outq.get()
    if ret == 0:
        shipmap[(nextx, nexty)] = '#'
        continue
    elif ret == 1:
        shipmap[(nextx, nexty)] = '.'
    elif ret == 2:
        shipmap[(nextx, nexty)] = 'O'
    else:
        print('Something is wrong 2')
    x = nextx
    y = nexty

print(shipmap)

