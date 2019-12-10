import opcodes as o
import itertools as it
import collections

def runcomp (invalue):
    program = collections.defaultdict(int)
    with open('input') as f:
        for i, x in enumerate(f.readline().split(',')):
            program[i] = int(x)
    index = 0
    relbase = 0

    while program[index] != 99:
        instruction = str(program[index]).zfill(5)

        opcode = instruction [-2:]
        mode1 = int(instruction[-3])
        mode2 = int(instruction[-4])
        mode3 = int(instruction[-5])
        if mode1 == 0:
            param1 = program[program[index+1]]
        elif mode1 == 1:
            param1 = program[index+1]
        elif mode1 == 2:
            param1 = program[program[index+1] + relbase]

        if opcode == '03':
            index = o.op03(program, index, program[index+1], mode1, relbase, invalue)
        elif opcode == '04':
            index = o.op04(program, index, param1)
        elif opcode == '09':
            index, relbase = o.op09(program, index, param1, relbase)
        else:
            if mode2 == 0:
                param2 = program[program[index+2]]
            elif mode2 == 1:
                param2 = program[index+2]
            elif mode2 == 2:
                param2 = program[program[index+2] + relbase]
            if mode3 == 0:
                param3 = program[index+3]
            elif mode3 == 1:
                print('NOPE')
            elif mode3 == 2:
                param3 = program[index+3] + relbase

            index = getattr(o, 'op' + opcode)(program, index, param1, param2, param3)

runcomp(1)
runcomp(2)
