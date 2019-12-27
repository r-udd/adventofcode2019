import queue as q

def op01(program, index, inq, outq, addrs, relbase, address):
    'Add'
    program[addrs[2]] = program[addrs[0]] + program[addrs[1]]
    return index + 4, relbase, address


def op02(program, index, inq, outq, addrs, relbase, address):
    'Multiply'
    program[addrs[2]] = program[addrs[0]] * program[addrs[1]]
    return index + 4, relbase, address


def op03(program, index, inq, outq, addrs, relbase, address):
    'Get input'
    #outq.put('i')
    try:
        i = outq[inq].get_nowait()
    except q.Empty:
        i = -1
    # if i == 255:
    #     outq[inq].get()
    #     ans = outq[inq].get()
    #     print(ans)
    #     print(end='')

    program[addrs[0]] = i
    return index + 2, relbase, address


def op04(program, index, inq, outq, addrs, relbase, address):
    'Put output'
    o = program[addrs[0]]
    ''
    if address[0] == 0:
        address = (1, o)
    elif address[0] == 1:
        if address[1] == 255:
            outq[50].put(o)
        else:
            outq[address[1]].put(o)
        address = (2, address[1])
    elif address[0] == 2:
        if address[1] == 255:
            outq[50].put(o)
        else:
            outq[address[1]].put(o)
        address = (0,0)
    return index + 2, relbase, address


def op05(program, index, inq, outq, addrs, relbase, address):
    'Jump if true'
    if program[addrs[0]] != 0:
        return program[addrs[1]], relbase, address
    return index + 3, relbase, address


def op06(program, index, inq, outq, addrs, relbase, address):
    'Jump if false'
    if program[addrs[0]] == 0:
        return program[addrs[1]], relbase, address
    return index + 3, relbase, address


def op07(program, index, inq, outq, addrs, relbase, address):
    'Less than'
    program[addrs[2]] = int(program[addrs[0]] < program[addrs[1]])
    return index + 4, relbase, address


def op08(program, index, inq, outq, addrs, relbase, address):
    'Equals'
    program[addrs[2]] = int(program[addrs[0]] == program[addrs[1]])
    return index + 4, relbase, address


def op09(program, index, inq, outq, addrs, relbase, address):
    'Adjust relative base'
    return index + 2, relbase + program[addrs[0]], address
