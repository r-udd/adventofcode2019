
import intcode as comp
import itertools as it
import collections
import queue as q
from os import system, name 
from time import sleep 
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

def printmap (m):
    for y in range(24):
        for x in range(37+1):
            tile = m[(x,y)]
            if tile == 0:
                print(' ', end='')
            elif tile == 1:
                print('#', end='')
            elif tile == 2:
                print('B', end='')
            elif tile == 3:
                print('=', end='')
            elif tile == 4:
                print('O', end='')
            else:
                print('S', end='')
        print()

inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()

clear()
count = 0
i = 0
m = collections.defaultdict(int)
ballx = 0
paddlex = 0
while True:
    try:
        x = outq.get(timeout=0.001)
    except q.Empty as err:
        #clear()
        #printmap(m)
        if ballx < paddlex:
            inq.put(-1)
        elif ballx == paddlex:
            inq.put(0)
        else:
            inq.put(1)
        # m = collections.defaultdict(int)
        continue

    y = outq.get()
    tile = outq.get()
    m[(x,y)] = tile
    if tile == 3:
        paddlex = x
    if tile == 4:
        ballx = x
    
    if x == -1 and y == 0:
        tiles = 0
        for t in m.values():
            if t == 2:
                tiles += 1
        print('score', tile, 'tiles left', tiles)
        if tiles == 0:
            break
    i+= 1

