import queue as q

def op01(program, index, inq, outq, addrs, relbase, count):
    'Add'
    program[addrs[2]] = program[addrs[0]] + program[addrs[1]]
    return index + 4, relbase, count


def op02(program, index, inq, outq, addrs, relbase, count):
    'Multiply'
    program[addrs[2]] = program[addrs[0]] * program[addrs[1]]
    return index + 4, relbase, count


def op03(program, index, inq, outq, addrs, relbase, count):
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
    return index + 2, relbase, count


def op04(program, index, inq, outq, addrs, relbase, count):
    'Put output'
    o = program[addrs[0]]
    ''
    if count or o == 255:
        count += 1
    if count == 1 or count == 2 or count == 3:
        print(inq, count, o)
    print(end='')
    for i, o in enumerate(outq):
        if i != inq:
            o.put(program[addrs[0]])
    return index + 2, relbase, count


def op05(program, index, inq, outq, addrs, relbase, count):
    'Jump if true'
    if program[addrs[0]] != 0:
        return program[addrs[1]], relbase, count
    return index + 3, relbase, count


def op06(program, index, inq, outq, addrs, relbase, count):
    'Jump if false'
    if program[addrs[0]] == 0:
        return program[addrs[1]], relbase, count
    return index + 3, relbase, count


def op07(program, index, inq, outq, addrs, relbase, count):
    'Less than'
    program[addrs[2]] = int(program[addrs[0]] < program[addrs[1]])
    return index + 4, relbase, count


def op08(program, index, inq, outq, addrs, relbase, count):
    'Equals'
    program[addrs[2]] = int(program[addrs[0]] == program[addrs[1]])
    return index + 4, relbase, count


def op09(program, index, inq, outq, addrs, relbase, count):
    'Adjust relative base'
    return index + 2, relbase + program[addrs[0]], count
