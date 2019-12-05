def op01 (program, param1, param2, param3):
    program[param3] = program[param1] + program[param2]
    return 4


def op02(program, param1, param2, param3):
    program[param3] = program[param1] * program[param2]
    return 4


def op03(program, param1, input):
    program[param1] = input
    return 2


def op04(program, param1, param2, param3):
    print(program[param1])
    return 2
