from collections import defaultdict
from os import system, name
import queue as q
import intcode as comp

nics = []
no = 50
for i in range(no):
    nics.append(q.Queue())
    
for i, n in enumerate(nics):
    n.put(i)

nics.append(q.Queue())

comps = []
for i in range(no):
    comps.append(comp.Intcode(i, nics))

for c in comps:
    c.start()

prevx = -1
prevy = -1
while True:
    for qi in range(no):
        if not nics[qi].empty():
            break
    else:
        while not nics[50].empty():
            x = nics[50].get()
            y = nics[50].get()
            new = True
        if new:
            nics[0].put(x)
            nics[0].put(y)
            if prevx == x and prevy == y:
                print(y)
                break
            prevx = x
            prevy = y
            new = False