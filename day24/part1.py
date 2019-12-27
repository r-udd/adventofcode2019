maxx = 4
maxy = 4
grid = []
with open('input.txt') as f:
    for l in f.readlines():
        line = []
        for char in l.strip():
            line.append(char)
        grid.append(line)

dirs = [(0,-1), (1,0), (0,1), (-1,0)]
prevs = set()
prevs.add(str(grid))
print (str(grid))
while True:
    newgrid = [['.' for x in range(maxx+1)] for y in range(maxy+1)]
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            count = 0
            for d in dirs:
                newx = x + d[0]
                newy = y + d[1]
                if newx in range(maxx + 1) and newy in range(maxy+1):
                    count += grid[newy][newx] == '#'
            if grid[y][x] == '#' and count == 1:
                newgrid[y][x] = '#'
            elif grid[y][x] == '.' and (count == 2 or count == 1):
                newgrid[y][x] = '#'
            else:
                newgrid[y][x] = '.'

    grid = newgrid
    snewgrid = str(newgrid)
    if snewgrid in prevs:
        break
    prevs.add(snewgrid)
count = 0
biodiv = 0
for y in range(maxy + 1):
    for x in range(maxx + 1):
        if newgrid[y][x] == '#':
            biodiv += pow(2,count)
        count += 1

print(biodiv)

