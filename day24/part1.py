maxx = 4
maxy = 4
grid = ""
with open('input.txt') as f:
    for l in f.readlines():
        grid += l.strip()

prevs = set()
prevs.add(grid)
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
while True:
    line = ''
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            count = 0
            for d in dirs:
                newx = x + d[0]
                newy = y + d[1]
                index = newy * 5 + newx
                if newx in range(maxx + 1) and newy in range(maxy+1):
                    count += grid[index] == '#'
            if grid[y * 5 + x] == '#' and count == 1:
                line += '#'
            elif grid[y * 5 + x] == '.' and (count == 2 or count == 1):
                line += '#'
            else:
                line += '.'
    newgrid = line

    grid = newgrid
    if newgrid in prevs:
        break
    prevs.add(newgrid)

count = 0
biodiv = 0
for y in range(maxy + 1):
    for x in range(maxx + 1):
        if newgrid[y * 5 + x] == '#':
            biodiv += pow(2,count)
        count += 1

print(biodiv)

