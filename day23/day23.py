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

input()

