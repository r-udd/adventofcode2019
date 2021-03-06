from collections import defaultdict
from os import system, name
import queue as q
import intcode as comp
from readchar import readchar

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq, mem0=2)
c.start()

with open('instructions.txt') as f:
    for l in f:
        for char in l:
            inq.put(ord(char))

while outq.not_empty:
    out = outq.get()
    if out == 'q':
        break
    elif out > 99:
        print(out)
    else:
        print(chr(out), end='')
