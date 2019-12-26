from collections import defaultdict
from os import system, name
import queue as q
import intcode as comp

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()

while True:
    out = outq.get()
    print(chr(out), end='')
    if chr(out) == '?' and outq.qsize() == 1:
        inp = input()
        for i in inp:
            inq.put(ord(i))
        inq.put(ord('\n'))
