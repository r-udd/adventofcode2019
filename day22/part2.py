instructions = []
with open('input.txt') as f:
    lines = f.readlines()
    lines.reverse()

def revshuffle(instructions, index, decksize):
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        i += 1
        if instruction == 'r':
            index = (-index - 1) % decksize
        elif instruction == 'c':
            incr = instructions[i]
            i += 1
            index = (index + incr) % decksize
        elif instruction == 'di':
            incr = instructions[i]
            i += 1
            y = pow(incr, -1, decksize)
            index = (index * y) % decksize
    return index

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
n = 101741582076661
X = 2020

#from https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnifwk/
Y = revshuffle(instructions, X, decksize)
Z = revshuffle(instructions, Y, decksize)
A = ((Y-Z) * pow(X-Y, -1, decksize)) % decksize
B = (Y - A * X) % decksize

print((pow(A, n, decksize)*X + (pow(A, n, decksize)-1) * pow(A-1, -1, decksize) * B) % decksize)