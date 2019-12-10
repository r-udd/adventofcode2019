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
            addr1 = program[index+1]
        elif mode1 == 1:
            addr1 = index+1
        elif mode1 == 2:
            addr1 = program[index+1] + relbase
        if mode2 == 0:
            param2 = program[index+2]
        elif mode2 == 1:
            param2 = index+2
        elif mode2 == 2:
            param2 = program[index+2] + relbase
        if mode3 == 0:
            param3 = program[index+3]
        elif mode3 == 1:
            print('NOPE')
        elif mode3 == 2:
            param3 = program[index+3] + relbase

        index, relbase = getattr(o, 'op' + opcode)(program, index, invalue, addr1, param2, param3, relbase)

runcomp(1)
runcomp(2)
