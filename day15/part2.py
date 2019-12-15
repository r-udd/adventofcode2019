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

def lookahead (map, posx, posy, dir):
    visited = {(posx, posy)}
    todo = [(posx+dir[0], posy+dir[1])]
    dirs = [(0,-1), (0,1), (-1,0), (1,0)]
    while todo:
        pos = todo.pop(0)
        for d in dirs:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            testpos = (x,y)
            tile = map[testpos]
            t = pos in visited
            if tile == ' ':
                return True
            if tile == '#' or testpos in visited or testpos in todo:
                continue
            elif tile == '.':
                visited.add((x,y))
                todo.append(testpos)
                
    return False
            


def printmap(map, posx, posy, minx, maxx, miny, maxy):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if x == posx and y == posy:
                print('R', end='')
            else:
                print(map[(x,y)], end='')
        print()


inq = q.Queue()
outq = q.Queue()
c = comp.Intcode(inq, outq)
c.start()
minx = 0
miny = 0
maxx = 0
maxy = 0
shipmap = defaultdict(lambda : ' ')
x = 0
y = 0
shipmap[(x,y)] = '.'
inp = 'start'
count = 0
while inp != 'p':
    count += 1
    if count % 1000 == 0:
        clear()
        printmap(shipmap, x, y, minx, maxx, miny, maxy)
        print(x, y)
    #inp = readchar()
    if outq.get() != 'i':
        print('Something is wrong')
    
    dirs = [(0,-1), (0,1), (-1,0), (1,0)]
    for i, dir in enumerate(dirs, start=1):
        nextx = x + dir[0]
        nexty = y + dir[1]
        nextpos = (nextx, nexty)
        if shipmap[nextpos] == ' ':
            inq.put(i)
            break
    else:
        for i, dir in enumerate(dirs, start=1):
            nextx = x + dir[0]
            nexty = y + dir[1]
            nextpos = (nextx, nexty)
            if nextpos != prevpos and shipmap[nextpos] == '.' and lookahead(shipmap,x,y,dir):
                inq.put(i)
                break
        else:
            for i, dir in enumerate(dirs, start=1):
                nextx = x + dir[0]
                nexty = y + dir[1]
                nextpos = (nextx, nexty)
                if shipmap[nextpos] == '.' and lookahead(shipmap,x,y,dir):
                    inq.put(i)
                    break
            else:
                printmap(shipmap, x, y, minx, maxx, miny, maxy)
                print(x,y)
                lookahead(shipmap,x,y,(-1,0))
                break


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
    prevpos = (x,y)
    x = nextx
    y = nexty

#print(shipmap)

