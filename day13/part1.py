
import intcode as comp
import itertools as it
import collections
import queue as q


inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()

c.join()
count = 0
i = 0
minx = 9999
maxx = 0
miny = 9999
maxy = 0

while not outq.empty():
    
    x = outq.get()
    minx = min(minx, x)
    maxx = max(maxx, x)
    y = outq.get()
    miny = min(minx, x)
    maxy = max(maxx, x)
    tile = outq.get()
    if tile == 2:
        count +=1
    i+= 1
print(count)
print('x', minx, maxx)
print('y', miny, maxy)