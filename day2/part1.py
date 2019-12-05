
with open('input') as f:
    program = [int(x) for x in f.readline().split(',')]

program[1] = 12
program[2] = 2

index = 0
while program[index] != 99:
    instruction = program[index]
    address1 = program[index+1]
    address2 = program[index+2]
    target = program[index+3]
    if instruction == 1:
        program[target] = program[address1] + program[address2]
    if instruction == 2:
        program[target] = program[address1] * program[address2]
    index = index + 4
print(program[0])
