#!/usr/bin/env python3

class BinaryAdder():

    def and_gate(self, a0, b0):
        if (a0 == 1 and b0 == 1):
            return 1
        else:
            return 0

    def or_gate(self, a0, b0):
        if (a0 == 1 or b0 == 1):
            return 1
        else:
            return 0

    def xor_gate(self, a0, b0):
        if (a0 == 1 and b0 != 1) or (a0 != 1 and b0 == 1):
            return 1
        else:
            return 0

    def show_intro(self):
        title = '2-bit Binary Adder'
        print('\n' + title)
        print('-' * len(title) + '\n')
        print('Choose three binary numbers for the adder to compute.' + '\n')

    def validate_input(self, prompt_text):
        user_input = int()
        while user_input != 0 or user_input != 1:
            try:
                user_input = int(input(prompt_text))
            except:
                print('Input a valid number.')
            else:
                if user_input > 1 or user_input < 0:
                    print('Input 0 or 1.')
                else:
                    return user_input

    def get_user_input(self):
        a0 = self.validate_input('Set the first bit to 0 or 1: ')
        b0 = self.validate_input('Set the second bit to 0 or 1: ')
        c0 = self.validate_input('Set the carry bit to 0 or 1: ')

        return a0, b0, c0

    def create_logic_gates(self, a0, b0):
        a0_and_b0 = self.and_gate(a0, b0)
        a0_or_b0 = self.or_gate(a0, b0)
        a0_xor_b0 = self.xor_gate(a0, b0)

        return a0_and_b0, a0_or_b0, a0_xor_b0

    def show_logic_gates(self, a0, b0, a0_and_b0, a0_or_b0, a0_xor_b0):
        and_gate = 'AND gate [' + str(a0) + ' AND ' + str(b0) + ']: ' + str(a0_and_b0)
        or_gate = 'OR  gate [' + str(a0) + ' OR  ' + str(b0) + ']: ' + str(a0_or_b0)
        xor_gate = 'XOR gate [' + str(a0) + ' XOR ' + str(b0) + ']: ' + str(a0_xor_b0)

        print('\n' + 'LOGIC GATES')
        print('-' * len(and_gate))
        print(and_gate)
        print(or_gate)
        print(xor_gate)

    def calculate_result(self, a0, b0, c0, a0_xor_b0):
        sum_a0_b0 = self.xor_gate(a0_xor_b0, c0)
        c1 = self.and_gate(a0_xor_b0, c0)
        c2 = self.and_gate(a0, b0)
        carry_bit = self.or_gate(c1, c2)
        result = str(carry_bit) + str(sum_a0_b0)

        return sum_a0_b0, c1, c2, carry_bit, result

    def show_result(self, a0, b0, c0, c1, c2, a0_xor_b0, sum_a0_b0, carry_bit, result):
        print('\n' + 'Initial state of the adder circuit:')
        print('Input A:   ' + str(a0))
        print('Input B:   ' + str(b0))
        print('Carry Bit: ' + str(c0))

        print('\n' + 'The sum calculation is: ')
        print(str(a0) + ' PLUS ' + str(b0) +  ', CARRY ' + str(c0))

        print('\n' + 'Calculate the sum of A and B:')
        print('A XOR B [' + str(a0) + ' + ' + str(b0) + ']: ' + str(a0_xor_b0))
        print('\n' + 'Factor in the carry bit:')
        print('SUM = (A XOR B) XOR C [' + str(a0_xor_b0) +  ' + ' + str(c0) + ']: ' + str(sum_a0_b0))

        print('\n' + 'Generate the input values for new carry bit calculation:')
        print('C1 = (A XOR B) AND C [' + str(a0_xor_b0) + ' + ' + str(c0) + ']: ' + str(c1))
        print('C2 = A AND B [' + str(a0) + ' + ' + str(b0) + ']: ' + str(c2))

        print('\n' + 'Calculate the new carry bit')
        print('CARRY = C1 OR C2 [' + str(c2) + ' + ' + str(c1) + ']: ' + str(carry_bit))

        print('\n' + 'Concatenate the new carry bit and sum bit for the final 2-bit result:')
        print('RESULT (CARRY|SUM): ' + result + '\n')

        print('Calculation complete!' + '\n')

    def exit(self):
        input('Press the RETURN key to exit: ')
        raise SystemExit()

def main():
    adder = BinaryAdder()
    adder.show_intro()
    a0, b0, c0 = adder.get_user_input()
    a0_and_b0, a0_or_b0, a0_xor_b0 = adder.create_logic_gates(a0, b0)
    adder.show_logic_gates(a0, b0, a0_and_b0, a0_or_b0, a0_xor_b0)
    sum_a0_b0, c1, c2, carry_bit, result = adder.calculate_result(a0, b0, c0, a0_xor_b0)
    adder.show_result(a0, b0, c0, c1, c2, a0_xor_b0, sum_a0_b0, carry_bit, result)
    adder.exit()

if __name__ == '__main__':
    main()
