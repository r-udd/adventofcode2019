maxx = 4
maxy = 4
grid = ""
with open('input.txt') as f:
    for l in f.readlines():
        grid += l.strip()

grid = grid[:12] + '?' + grid[13:]
dirs = [(0,-1), (1,0), (0,1), (-1,0)]
pattern = '............?............'
levels = 500
allgrids = [pattern for y in range(levels)]
allgrids.insert(levels //2, grid)
levels += 1
for i in range(200):
    newgrids = [pattern]
    for level in range(1, levels-1):
        newgrid = ''
        for y in range(maxy + 1):
            for x in range(maxx + 1):
                if x == 2 and y == 2:
                    newgrid += '?'
                    continue
                count = 0
                for d in dirs:
                    newx = x + d[0]
                    newy = y + d[1]
                    index = newy * 5 + newx
                    if newx > maxx:
                        count += allgrids[level+1][13] == '#'
                    elif newy > maxy:
                        count += allgrids[level+1][17] == '#'
                    elif newy < 0:
                        count += allgrids[level+1][7] == '#'
                    elif newx < 0:
                        count += allgrids[level+1][11] == '#'
                    elif index == 12:
                        if d == (0,-1):
                            count += allgrids[level-1][20] == '#'
                            count += allgrids[level-1][21] == '#'
                            count += allgrids[level-1][22] == '#'
                            count += allgrids[level-1][23] == '#'
                            count += allgrids[level-1][24] == '#'
                        elif d == (1,0):
                            count += allgrids[level-1][0] == '#'
                            count += allgrids[level-1][5] == '#'
                            count += allgrids[level-1][10] == '#'
                            count += allgrids[level-1][15] == '#'
                            count += allgrids[level-1][20] == '#'
                        elif d == (0,1):
                            count += allgrids[level-1][0] == '#'
                            count += allgrids[level-1][1] == '#'
                            count += allgrids[level-1][2] == '#'
                            count += allgrids[level-1][3] == '#'
                            count += allgrids[level-1][4] == '#'
                        elif d == (-1,0):
                            count += allgrids[level-1][4] == '#'
                            count += allgrids[level-1][9] == '#'
                            count += allgrids[level-1][14] == '#'
                            count += allgrids[level-1][19] == '#'
                            count += allgrids[level-1][24] == '#'
                    else:
                        count += allgrids[level][index] == '#'
                if allgrids[level][y * 5 + x] == '#' and count == 1:
                    newgrid += '#'
                elif allgrids[level][y * 5 + x] == '.' and (count == 2 or count == 1):
                    newgrid += '#'
                else:
                    newgrid += '.'
        newgrids.append(newgrid)
    newgrids.append(pattern)
    allgrids = newgrids.copy()
    
    # for level in range(levels):
    #     for y in range(maxy + 1):
    #         for x in range(maxx + 1):
    #             print(newgrids[level][y * 5 + x], end='')
    #         print()
    #     print(level)


count = 0
for level in range(levels):
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if newgrids[level][y * 5 + x] == '#':
                count += 1
    #         print(newgrids[level][y * 5 + x], end='')
    #     print()
    # print(level)

print(count)

