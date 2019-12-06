def count (orbits, obj, current):
    if obj not in orbits:
        return current
    summa = current
    orbs = orbits[obj]
    for o in orbits[obj]:
        summa += count(orbits, o, current+1)
    return summa


orbits = {}

with open('input') as f:
    for l in f:
        obj1, obj2 = l.rstrip().split(')')
        if obj1 not in orbits:
            orbits[obj1] = [obj2]
        else:
            orbits[obj1].append(obj2)
print(orbits)

print(count(orbits, 'COM', 0))
