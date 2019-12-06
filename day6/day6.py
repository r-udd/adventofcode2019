def count (orbits, obj, current):
    if obj not in orbits:
        return current
    summa = current
    orbs = orbits[obj]
    for o in orbits[obj]:
        summa += count(orbits, o, current+1)
    return summa


def jumpcount(orbits, obj):
    if obj == 'SAN':
        return 0, False, True
    if obj == 'YOU':
        return 0, True, False
    if obj not in orbits:
        return 0, False, False
    summa = 0
    orbs = orbits[obj]
    foundsan = False
    foundyou = False
    for o in orbits[obj]:
        count, san, you = jumpcount(orbits, o)
        foundsan = foundsan or san
        foundyou = foundyou or you
        if san and you:
            return count, you, san
        if san or you:
            summa = summa + count + 1
    return summa, foundyou, foundsan


orbits = {}

with open('input') as f:
    for l in f:
        obj1, obj2 = l.rstrip().split(')')
        if obj1 not in orbits:
            orbits[obj1] = [obj2]
        else:
            orbits[obj1].append(obj2)
print(orbits)

print('Total direct and indirect orbits:', count(orbits, 'COM', 0))

#Subtract for the edges between YOU/SAN and the closest orbit
print('Total jumps:', jumpcount(orbits, 'COM')[0] - 2)
