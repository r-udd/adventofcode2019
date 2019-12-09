def op01 (program, index, param1, param2, param3):
    program[param3] = param1 + param2
    return index + 4


def op02(program, index, param1, param2, param3):
    program[param3] = param1 * param2
    return index + 4

def op03(program, index, param1, mode, relbase, input):
    if mode == 2:
        program[param1+relbase] = input
    else:
        program[param1] = input
    return index + 2


def op04(program, index, param1):
    print('OUTPUT:', param1)
    return index + 2


def op05(program, index, param1, param2, param3):
    'Jump if true'
    if param1 != 0:
        return param2
    return index + 3


def op06(program, index, param1, param2, param3):
    'Jump if false'
    if param1 == 0:
        return param2
    return index + 3


def op07(program, index, param1, param2, param3):
    'Less than'
    program[param3] = int(param1 < param2)
    return index + 4


def op08(program, index, param1, param2, param3):
    'Output'
    program[param3] = int(param1 == param2)
    return index + 4


def op09(program, index, param1, relbase):
    'Adjust relative base'
    return index + 2, relbase + param1
