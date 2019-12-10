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
        addrs = []
        for i in range(1, 4):
            mode = int(instruction[-2-i])
            if mode == 0:
                addr = program[index + i]
            elif mode == 1:
                addr = index + i
            elif mode == 2:
                addr = program[index + i] + relbase
            addrs.append(addr)

        index, relbase = getattr(o, 'op' + opcode)(program, index, invalue, addrs, relbase)

runcomp(1)
runcomp(2)
