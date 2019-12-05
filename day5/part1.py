import opcodes as o


with open('input') as f:
#with open('testneg') as f:
    program = [int(x) for x in f.readline().split(',')]

inp = 1

#Can we assume that input is only once???
if program[0] == 3:
    index = o.op03(program, program[1], inp)
else:
    index = 0
# program[1] = 12
# program[2] = 2
while program[index] != 99:
    instruction = str(program[index]).zfill(5)

    opcode = instruction [-2:]
    if opcode == '03':
        print('Didnt work')
        break
    mode1 = int(instruction[-3])
    mode2 = int(instruction[-4])
    mode3 = int(instruction[-5])
    #position mode 0 address at index X
    #immediate mode 1 value at index X
    if mode1:
        param1 = program[index+1]
    else:
        param1 = program[program[index+1]]
    if mode2:
        param2 = program[index+2]
    else:
        param2 = program[program[index+2] % len(program)]
    param3 = program[index+3]



    index += getattr(o, 'op' + opcode)(program, param1, param2, param3)


print('position 0', program[0])
