
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
while not outq.empty():
    
    o = outq.get()
    print (i, o)
    if (i -2 )%3 == 0 and o == 2:
        count +=1
    i+= 1
print(count)