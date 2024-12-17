class Program:
    def __init__(self, reg_a, reg_b, reg_c, code):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.code = code
        self.pointer = 0

    def run(self):
        output = []

        while self.pointer < len(self.code):
            instruction = self.code[self.pointer]

            instruction_output = self.execute_instruction(instruction, self.code[self.pointer + 1])

            if instruction == 5:
                output.append(instruction_output)

            self.pointer += 2

        return output

    def execute_instruction(self, instruction, operand):
        match instruction:
            case 0:
                return self.adv(operand)
            case 1:
                return self.bxl(operand)
            case 2:
                return self.bst(operand)
            case 3:
                return self.jnz(operand)
            case 4:
                return self.bxc(operand)
            case 5:
                return self.out(operand)
            case 6:
                return self.bdv(operand)
            case 7:
                return self.cdv(operand)

    def adv(self, operand):
        self.reg_a = self.perform_division(operand)

    def bxl(self, operand):
        self.reg_b = self.reg_b ^ operand

    def bst(self, operand):
        self.reg_b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.reg_a != 0:
            self.pointer = operand - 2

    def bxc(self, operand):
        self.reg_b = self.reg_b ^ self.reg_c

    def out(self, operand):
        return self.combo(operand) % 8

    def bdv(self, operand):
        self.reg_b = self.perform_division(operand)

    def cdv(self, operand):
        self.reg_c = self.perform_division(operand)

    def perform_division(self, operand):
        return self.reg_a // (2 ** self.combo(operand))

    def combo(self, operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.reg_a
        elif operand == 5:
            return self.reg_b
        elif operand == 6:
            return self.reg_c


