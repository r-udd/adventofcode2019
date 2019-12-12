import itertools

pos = []
vel = []
prevenergy = 0
with open('input.txt') as f:
    for line in f:
        inp = line.split('=')
        x = int(inp[1].split(',')[0])
        y = int(inp[2].split(',')[0])
        z = int(inp[3].split('>')[0])
        pos.append([x, y, z])
        vel.append([0,0,0])

pairs = itertools.combinations([0,1,2,3],2)
p = list(pairs)
inp = 5
prevstates=set()
count = 0
while True:
    #state = tuple((p[i] for p in pos for i in range(3)))
    state = tuple((v[i] for v in vel for i in range(3)))
    
    energy = 0
    for moon in range(4):
        kin = 0
        pot = 0
        for i in range(3):
            pot += abs(pos[moon][i])
            kin += abs(vel[moon][i])
        energy += pot * kin

    if state in prevstates:
        print(count)
    prevstates.add(state)
    for pair in p:
        moon1 = pair[0]
        moon2 = pair[1]
        for i in range(3):
            if pos[moon1][i] < pos[moon2][i]:
                vel[moon1][i] += 1
                vel[moon2][i] -= 1
            elif pos[moon2][i] < pos[moon1][i]:
                vel[moon1][i] -= 1
                vel[moon2][i] += 1
    for moon in range(4):
        for i in range(3):
            pos[moon][i] += vel[moon][i]
    count += 1
    
    if count % 1000 == 0:
        #print(energy, energy - prevenergy)
        prevenergy = energy

print(count)
#Only input once