class Console:

    def __init__(self, instr):
        self.instr = instr
        self.__visited = []
        self.__ptr = 0
        self.__accumulator = 0
        self.__success = 0

    def exec(self, ptr):
        if ptr in self.__visited:
            return self.__success, self.__accumulator
        elif ptr == len(self.instr):
            self.__success = 1
            return self.__success, self.__accumulator
        else:
            self.__visited.append(ptr)
            command, arg = self.instr[ptr]
            switch = {
                "acc": lambda: self.acc(arg),
                "jmp": lambda: self.jmp(arg),
                "nop": lambda: self.nop()
            }
            func = switch.get(command, lambda: 'Invalid Op')
            return func()

    def acc(self, arg):
        self.__accumulator += arg
        self.__ptr += 1
        return self.exec(self.__ptr)

    def jmp(self, arg):
        self.__ptr += arg
        return self.exec(self.__ptr)

    def nop(self):
        self.__ptr += 1
        return self.exec(self.__ptr)

    def reset(self):
        self.__visited = []
        self.__ptr = 0
        self.__accumulator = 0
        self.__success = 0
