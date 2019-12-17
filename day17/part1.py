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

def printmap(map, robotpos, maxx, maxy):
    for y in range(maxy+1):
        for x in range(maxx+1):
            if x == robotpos[0] and y == robotpos[1]:
                print('R', end='')
            else:
                print(map[(x,y)], end='')
        print()

def createmap (shipmap, outq):
    x = 0
    y = 0
    maxx = 0
    robotpos = 0
    while outq.not_empty:
        o = outq.get()
        if o == 'q':
            return maxx, y, robotpos, (0,-1)
        o = chr(o)
        if o == '\n':
            y += 1
            maxx = max(x,maxx)
            x = 0
            continue
        elif o == '^':
            robotpos = (x,y)
            shipmap[(x,y)] = '#'
        else:
            shipmap[(x,y)] = o
        x += 1
    return -1, -1, -1, -1

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()
c.join()

shipmap = defaultdict(lambda : '.')
x = 0
y = 0

maxx, maxy, robot, dir = createmap(shipmap, outq)
clear()
printmap(shipmap, robot, maxx, maxy)
summa = 0
dirs = [(0,-1), (0,1), (-1,0), (1,0)]
it = list(shipmap.items())
for pos, tile in it:
    if tile == '#':
        for dir in dirs:
            t = shipmap[(pos[0]+dir[0], pos[1], dir[1])]
            newp = (pos[0]+dir[0], pos[1]+ dir[1])
            if shipmap[newp] != '#':
                break
        else:
            summa += pos[0] * pos[1]
print(summa)
