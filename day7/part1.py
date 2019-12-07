import opcodes as o
import itertools as it

def runamp (phase, invalue):
    with open('input.txt') as f:
        program = [int(x) for x in f.readline().split(',')]
    index = 0
    index = o.op03(program, index, program[index+1], phase)
    #index = o.op03(program, index, program[index+1], invalue)

    while program[index] != 99:
        instruction = str(program[index]).zfill(5)

        opcode = instruction [-2:]
        mode1 = int(instruction[-3])
        mode2 = int(instruction[-4])
        if mode1:
            param1 = program[index+1]
        else:
            param1 = program[program[index+1]]
        if mode2:
            param2 = program[index+2]
        else:
            param2 = program[program[index+2] % len(program)]
        param3 = program[index+3]
        if opcode == '03':
            index = o.op03(program, index, program[index+1], invalue)
            continue
        elif opcode == '04':
            index = o.op04(program, index, param1)
            if program [index] != 99:
                print('Oh shit')
            return param1
        index = getattr(o, 'op' + opcode)(program, index, param1, param2, param3)

output = -9999999
perms = it.permutations(range(5))

for perm in perms:
    output = max(runamp(perm[4], runamp(perm[3], runamp(perm[2], runamp(perm[1], runamp(perm[0], 0))))), output)

print(output)

