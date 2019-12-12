import itertools
import fractions

def lcm(a, b):
    return abs(a*b) // fractions.gcd(a, b)

def get_vel(m1, m2, v1, v2):
    if m1 < m2:
        return v1+1, v2-1
    elif m2 < m1:
        return v1-1, v2+1
    return v1, v2

x = []
y = []
z = []
prevenergy = 0
with open('input.txt') as f:
    for line in f:
        inp = line.split('=')
        xpos = int(inp[1].split(',')[0])
        ypos = int(inp[2].split(',')[0])
        zpos = int(inp[3].split('>')[0])
        x.append(xpos)
        y.append(ypos)
        z.append(zpos)
x += [0,0,0,0]#+4 for velocity
y += [0,0,0,0]#+4 for velocity
z += [0,0,0,0]#+4 for velocity

pairs = itertools.combinations([0,1,2,3],2)
p = list(pairs)
inp = 5
prevstatesx={}
prevstatesy={}
prevstatesz={}
found = [0, 0, 0]
count = 0
while True:
    xstate = tuple(x)
    ystate = tuple(y)
    zstate = tuple(z)
    if not found[0] and xstate in prevstatesx:
        print('FOUND PREV STATE X', count, 'prev count', prevstatesx[xstate])
        found[0] = count
    if not found[1] and ystate in prevstatesy:
        print('FOUND PREV STATE Y', count, 'prev count', prevstatesy[ystate])
        found[1] = count
    if not found[2] and zstate in prevstatesz:
        print('FOUND PREV STATE Z', count, 'prev count', prevstatesz[zstate])
        found[2] = count
    if all(found):
        break

    prevstatesx[xstate] = count
    prevstatesy[ystate] = count
    prevstatesz[zstate] = count
    for pair in p:
        moon1 = pair[0]
        moon2 = pair[1]
        x[moon1+4], x[moon2+4] = get_vel(x[moon1], x[moon2], x[moon1+4], x[moon2+4])
        y[moon1+4], y[moon2+4] = get_vel(y[moon1], y[moon2], y[moon1+4], y[moon2+4])
        z[moon1+4], z[moon2+4] = get_vel(z[moon1], z[moon2], z[moon1+4], z[moon2+4])
    for moon in range(4):
        x[moon] += x[moon+4]
        y[moon] += y[moon+4]
        z[moon] += z[moon+4]
    count += 1
    
    if count % 10000 == 0:
        print(count, x)
    # if count == 100:
    #     break

print('x', x)
print('y', y)
print('z', z)
print(lcm(lcm(found[0], found[1]), found[2]))
#Only input once