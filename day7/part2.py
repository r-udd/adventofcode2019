import opcodes as o
import itertools as it
import threading
from queue import Queue

class Amp(threading.Thread):
 
    def __init__(self, inq, outq, phase, args=(), kwargs=None):      
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.inq = inq
        self.outq = outq
        self.daemon = True
        self.phase = phase
 
    def run (self):
        with open('input.txt') as f:
            program = [int(x) for x in f.readline().split(',')]
        index = 0
        index = o.op03(program, index, program[index+1], self.phase)
        #index = o.op03(program, index, program[index+1], invalue)

        while program[index] != 99:
            instruction = str(program[index]).zfill(5)

            opcode = instruction [-2:]
            mode1 = int(instruction[-3])
            mode2 = int(instruction[-4])
            if mode1:
                param1 = program[index+1]
            else:
                param1 = program[program[index+1] % len(program)]
            if opcode == '03':
                index = o.op03(program, index, program[index+1], self.inq.get())
                continue
            elif opcode == '04':
                index = o.op04(program, index, param1)
                self.outq.put(param1)
                continue
            if mode2:
                param2 = program[index+2]
            else:
                param2 = program[program[index+2] % len(program)]
            param3 = program[index+3]
            index = getattr(o, 'op' + opcode)(program, index, param1, param2, param3)

output = -9999999
perms = it.permutations(range(5,10))

for perm in perms:
    queues = []
    for i in range(5):
        queues.append(Queue())
    amps = []
    for i in range(5):
        amps.append(Amp(queues[i],queues[(i+1) % 5],perm[i]))
    for amp in amps:
        amp.start()
    queues[0].put(0)
    
    amps[4].join()
    output = max(queues[0].get(), output)
print(output)
