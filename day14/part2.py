import math

recipes = {}

with open('input.txt') as f:
    for l in f:
        allinp, outp = l.rstrip().split(' => ')
        inplist = []
        for inp in allinp.split(', '):
            inpamount = int(inp.split(' ')[0])
            inpchem = inp.split(' ')[1]
            inplist.append((inpamount, inpchem))
        
        outpamount = int(outp.split(' ')[0])
        outpchem = outp.split(' ')[1]
        if outp in recipes:
            print('Shouldnt happen')
        else:
            recipes[outpchem] = (outpamount, inplist)
#print(recipes)

start = 6215000
print(start)
need = {'FUEL': start}
have = {}
ore = 0
while ore < 1000000000000:
    if len(need) == 0:
        print(1000000000000 - ore)
        need['FUEL'] = 1
        start += 1
    chem, amount = need.popitem()
    if chem == 'ORE':
        ore += amount
        continue
    outamount = recipes[chem][0]
    times = math.ceil(amount / outamount)
    inps = recipes[chem][1]
    #print('Creating', amount, chem, 'need', times, inps)
    for inp in inps:
        inamount = inp[0] * times
        inchem = inp[1]
        if inchem in have:
            haveamount = have[inchem]
            #print('Have', inchem, haveamount)
            if haveamount > inamount:
                have[inchem] -= inamount
            elif haveamount == inamount:
                have.pop(inchem)
            else:
                have.pop(inchem)
                need[inchem] = inamount - haveamount
                #print('Need another', need[inchem])
        else:
            #print('Need', inamount, inchem)
            if inchem in need:
                need[inchem] += inamount
            else:
                need[inchem] = inamount
    leftover = outamount * times - amount
    if leftover > 0 and chem in have:
        have[chem] += leftover
    elif leftover > 0:
        have[chem] = leftover

print(start - 1)