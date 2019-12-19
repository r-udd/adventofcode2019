from collections import defaultdict
from os import system, name
import queue as q
import intcode as comp
from readchar import readchar

def printmap(map, maxx, maxy):
    for x in range(maxy):
        print(x % 10, end='')
    print()
    for y in range(maxy):
        print(y % 10, end='')
        for x in range(maxx):
                print(map[(x,y)], end='')
        print()

inq = q.Queue()
outq = q.Queue()

shipmap = defaultdict(lambda : '.')
count = 0
for y in range(50):
    for x in range(50):
        c = comp.Intcode(inq, outq)
        c.start()
        inq.put(x)
        inq.put(y)
        tile = outq.get()
        _ = outq.get()
        if tile == 1:
            shipmap[(x,y)] = '#'
            count += 1

printmap(shipmap, 50, 50)
print(count)
dirs = [(0,-1), (0,1), (-1,0), (1,0)]
