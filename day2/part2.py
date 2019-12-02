def runprogram (noun,verb):
    with open('adventofcode2019/day2/input') as f:
        program = [int(x) for x in f.readline().split(',')]
    program[1] = noun
    program[2] = verb

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
    return program[0]

for noun in range(0,100):
    for verb in range(0,100):
        if runprogram(noun,verb) == 19690720:
            print(noun, verb)
            print(100 * noun + verb)
