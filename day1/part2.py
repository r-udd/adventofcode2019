def fuel (i):
    if i <= 0:
        return 0
    else:
        return i + fuel(i //3 - 2)

print(sum([fuel(int(i))-int(i) for i in open ('input.txt').readlines()]))

