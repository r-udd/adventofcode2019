def op01 (program, index, inq, outq, addrs, relbase):
    program[addrs[2]] = program[addrs[0]] + program[addrs[1]]
    return index + 4, relbase


def op02(program, index, inq, outq, addrs, relbase):
    program[addrs[2]] = program[addrs[0]] * program[addrs[1]]
    return index + 4, relbase

def op03(program, index, inq, outq, addrs, relbase):
    program[addrs[0]] = inq.get()
    return index + 2, relbase


def op04(program, index, inq, outq, addrs, relbase):
    outq.put(program[addrs[0]])
    return index + 2, relbase


def op05(program, index, inq, outq, addrs, relbase):
    'Jump if true'
    if program[addrs[0]] != 0:
        return program[addrs[1]], relbase
    return index + 3, relbase


def op06(program, index, inq, outq, addrs, relbase):
    'Jump if false'
    if program[addrs[0]] == 0:
        return program[addrs[1]], relbase
    return index + 3, relbase


def op07(program, index, inq, outq, addrs, relbase):
    'Less than'
    program[addrs[2]] = int(program[addrs[0]] < program[addrs[1]])
    return index + 4, relbase


def op08(program, index, inq, outq, addrs, relbase):
    'Equals'
    program[addrs[2]] = int(program[addrs[0]] == program[addrs[1]])
    return index + 4, relbase


def op09(program, index, inq, outq, addrs, relbase):
    'Adjust relative base'
    return index + 2, relbase + program[addrs[0]]
