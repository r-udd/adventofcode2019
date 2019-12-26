import opcodes as o
import collections
import threading

class Intcode(threading.Thread):

    def __init__(self, inq, outq, mem0=-1, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.inq = inq
        self.outq = outq
        self.mem0 = mem0
        self.daemon = True

    def run (self):
        program = collections.defaultdict(int)
        
        with open('input.txt') as f:
            for i, x in enumerate(f.readline().split(',')):
                program[i] = int(x)
        if self.mem0 != -1:
            program[0] = self.mem0
        index = 0
        relbase = 0
        count = 0
        while program[index] != 99:
            instruction = str(program[index]).zfill(5)

            opcode = instruction [-2:]
            addrs = []
            for i in range(1, 4):
                mode = int(instruction[-2-i])
                if mode == 0:
                    addr = program[index + i]
                elif mode == 1:
                    addr = index + i
                elif mode == 2:
                    addr = program[index + i] + relbase
                addrs.append(addr)

            index, relbase, count = getattr(o, 'op' + opcode)(program, index, self.inq, self.outq, addrs, relbase, count)
        #self.outq.put('q')
