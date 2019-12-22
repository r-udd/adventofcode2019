instructions = []
with open('input.txt') as f:
    for line in f:
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

decksize = 10007
deck = [x for x in range(decksize)]
while instructions:
    i = instructions.pop(0)
    if i == 'r':
        deck.reverse()
    elif i == 'c':
        incr = instructions.pop(0)
        deck = deck[incr:] + deck[:incr]
    elif i == 'di':
        incr = instructions.pop(0)
        deck2 = deck.copy()
        deck2.reverse()
        for index in range(decksize):
            deck[index * incr % decksize] = deck2.pop()
    else:
        print('Something is wrong')

print(decksize == len(deck))
print(deck.index(2019))