instructions = []
with open('input.txt') as f:
    lines = f.readlines()
    lines.reverse()

#with open('inputreverse.txt', 'w') as f:
#    f.writelines(lines)

for line in lines:
    if line.startswith('deal into new stack'):
        instructions.append('r')
    elif line.startswith('deal with increment'):
        instructions.append('di')
        instructions.append(int(line.split()[-1]))
    elif line.startswith('cut'):
        instructions.append('c')
        instructions.append(int(line.split()[-1]))
    else:
        print('Something is wrong')

decksize = 119315717514047
decksize = 10007
index = 2020
index = 7395

states = []
diffs = []
diff = 0
while True:
    states.append(index)
    if len(states) > 1:
        diff = (index-states[-2]) % decksize
        if diff in diffs:
            break

        diffs.append(diff)
        #print(diff)
    i = 0
    offset
    while i < len(instructions):
        instruction = instructions[i]
        i += 1
        if instruction == 'r':
            index3 = (-index - 1) % decksize
            pass
        elif instruction == 'c':
            incr = instructions[i] % decksize
            i += 1
            index = (index + incr) % decksize
        elif instruction == 'di':
            incr = instructions[i]
            i += 1
            # x = index
            y = pow(incr, -1, decksize)
            index = (index * y) % decksize


            # while x % incr != 0:
            #     x += decksize
            # index = x // incr
            pass
        else:
            print('Something is wrong 2')
    break
print(index)