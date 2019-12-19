from collections import defaultdict
import queue as q
import intcode as comp

def printmap(lowermap, uppermap, maxx, maxy):
    print(' ', end='')
    for x in range(maxy):
        print(x % 10, end='')
    print()
    for y in range(maxy):
        print(y % 10, end='')
        for x in range(maxx):
            pos = (x,y)
            if pos in lowermap and lowermap[pos] == '#':
                print('#', end='')
            elif pos in uppermap and uppermap[pos] == '#':
                print('#', end='')
            else:
                print('.', end='')
                
        print()

inq = q.Queue()
outq = q.Queue()

uppermap = defaultdict(lambda : '.')
lowermap = defaultdict(lambda : '.')
upper = [15,12]
lower = [15,13]
c = comp.Intcode(inq, outq)
c.start()
# upperdirs= [(1,0), (0,1)]
upperdir = 0
while True:
    inq.put(upper[0])
    inq.put(upper[1])
    tile = outq.get()
    if tile == 1:
        uppermap[(upper[0],upper[1])] = '#'
        upper[0] += 1
    elif tile == 0:
        upper[1] += 1
        upper[0] -= 1
    if upper[0] > 1500:
        break


while True:
    inq.put(lower[0])
    inq.put(lower[1])
    tile = outq.get()
    if tile == 1:
        lowermap[(lower[0],lower[1])] = '#'
        lower[1] += 1
    elif tile == 0:
        lower[0] += 1
        lower[1] -= 1
    if lower[0] > 1500:
        break
size = 99
for pos in uppermap.keys():
    if pos[0] > 8:
        for i in range(size):
            if (pos[0]-i, pos[1]) in lowermap:
                break
        else:
            if (pos[0]-size, pos[1]+size) in lowermap:
                print(pos[0]-size, pos[1], sep='')
                break
                
        

#printmap(lowermap, uppermap, 100, 100)
