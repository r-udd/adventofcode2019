def op01 (program, index, input, addr1, addr2, addr3, relbase):
    program[addr3] = program[addr1] + program[addr2]
    return index + 4, relbase


def op02(program, index, input, addr1, addr2, addr3, relbase):
    program[addr3] = program[addr1] * program[addr2]
    return index + 4, relbase

def op03(program, index, input, addr1, addr2, addr3, relbase):
    program[addr1] = input
    return index + 2, relbase


def op04(program, index, input, addr1, addr2, addr3, relbase):
    print('OUTPUT:', program[addr1])
    return index + 2, relbase


def op05(program, index, input, addr1, addr2, addr3, relbase):
    'Jump if true'
    if program[addr1] != 0:
        return program[addr2], relbase
    return index + 3, relbase


def op06(program, index, input, addr1, addr2, addr3, relbase):
    'Jump if false'
    if program[addr1] == 0:
        return program[addr2], relbase
    return index + 3, relbase


def op07(program, index, input, addr1, addr2, addr3, relbase):
    'Less than'
    program[addr3] = int(program[addr1] < program[addr2])
    return index + 4, relbase


def op08(program, index, input, addr1, addr2, addr3, relbase):
    'Equals'
    program[addr3] = int(program[addr1] == program[addr2])
    return index + 4, relbase


def op09(program, index, input, addr1, addr2, addr3, relbase):
    'Adjust relative base'
    return index + 2, relbase + program[addr1]
