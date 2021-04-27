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

    def get_user_input(self):
        a0 = int(input('Set the first number to 0 or 1: '))
        b0 = int(input('Set the second number to 0 or 1: '))
        c0 = int(input('Set the carry bit to 0 or 1: '))

        return a0, b0, c0

    def logic_gates(self, a0, b0):
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
        #print('-' * len(and_gate))

    def calculate_result(self, a0, b0, c0, a0_xor_b0):
        sum_a0_b0 = self.xor_gate(a0_xor_b0, c0)
        c1 = self.and_gate(a0_xor_b0, c0)
        c2 = self.and_gate(a0, b0)
        carry_bit = self.or_gate(c1, c2)
        result = str(carry_bit) + str(sum_a0_b0)

        return sum_a0_b0, c1, c2, carry_bit, result

    def show_result(self, a0, b0, c0, c1, c2, a0_xor_b0, sum_a0_b0, carry_bit, result):
        print('\n' + 'Initial state of adder circuit:')
        print('A: ' + str(a0))
        print('B: ' + str(b0))
        print('C (CARRY): ' + str(c0))

        print('\n' + 'The addition calculation is: ')
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

    def quit(self):
        input('Press ENTER to quit: ')
        raise SystemExit()

def main():
    adder = BinaryAdder()
    adder.show_intro()
    a0, b0, c0 = adder.get_user_input()
    a0_and_b0, a0_or_b0, a0_xor_b0 = adder.logic_gates(a0, b0)
    adder.show_logic_gates(a0, b0, a0_and_b0, a0_or_b0, a0_xor_b0)
    sum_a0_b0, c1, c2, carry_bit, result = adder.calculate_result(a0, b0, c0, a0_xor_b0)
    adder.show_result(a0, b0, c0, c1, c2, a0_xor_b0, sum_a0_b0, carry_bit, result)
    adder.quit()

if __name__ == '__main__':
    main()
