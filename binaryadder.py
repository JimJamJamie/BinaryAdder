#!/usr/bin/env python3

'''
binaryadder.py
'''

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
        print(title)
        print('-' * len(title) + '\n')

    def get_user_input(self):
        a0 = int(input('Set the first number to 0 or 1: '))
        b0 = int(input('Set the second number to 0 or 1: '))
        c0 = int(input('Set the carry bit to 0 or 1: '))

        return a0, b0, c0

    def logic_gates(self, a0, b0):
        a0andb0 = self.and_gate(a0, b0)
        a0orb0 = self.or_gate(a0, b0)
        a0xorb0 = self.xor_gate(a0, b0)

        return a0andb0, a0orb0, a0xorb0

    def show_logic_gates(self, a0, b0, a0andb0, a0orb0, a0xorb0):
        print('\n' + '-' * 38)
        print('Logic gate ' + str(a0) + ' AND ' + str(b0) + ': ' + str(a0andb0))
        print('Logic gate ' + str(a0) + ' OR  ' + str(b0) + ': ' + str(a0orb0))
        print('Logic gate ' + str(a0) + ' XOR ' + str(b0) + ': ' + str(a0xorb0))
        print('-' * 38)

    def calculate_result(self, a0, b0, c0, a0xorb0):
        suma0b0 = self.xor_gate(a0xorb0, c0)
        c1 = self.and_gate(a0xorb0, c0)
        c2 = self.and_gate(a0, b0)
        carry_bit = self.or_gate(c1, c2)
        result = str(carry_bit) + str(suma0b0)

        return suma0b0, c1, c2, carry_bit, result

    def show_result(self, a0, b0, c0, c1, c2, a0xorb0, suma0b0, carry_bit, result):
        print('\nThe addition calculation is: '+ str(a0) + ' PLUS ' + str(b0) +  ', CARRY ' + str(c0) + '\n')

        print('Initial state of adder circuit:')
        print('A: ' + str(a0))
        print('B: ' + str(b0))
        print('C (CARRY): ' + str(c0))

        print('\nCalculate the sum of A and B:')
        print('A XOR B [' + str(a0) + ' + ' + str(b0) + ']: ' + str(a0xorb0))
        print('\nFactor in the previous carry bit:')
        print('SUM = (A XOR B) XOR C [' + str(a0xorb0) +  ' + ' + str(c0) + ']: ' + str(suma0b0))

        print('\nGenerate the input values for carry bit calculation:')
        print('C1 = (A XOR B) AND C [' + str(a0xorb0) + ' + ' + str(c0) + ']: ' + str(c1))
        print('C2 = A AND B [' + str(a0) + ' + ' + str(b0) + ']: ' + str(c2))

        print('\nCalculate the carry bit')
        print('CARRY = C1 OR C2 [' + str(c2) + ' + ' + str(c1) + ']: ' + str(carry_bit))

        print('\nConcatenate the carry bit and sum bit for the final 2-bit result:')
        print('RESULT (CARRY|SUM): ' + result + '\n')

    def quit(self):
        input('Press ENTER to quit: ')
        raise SystemExit()

def main():
    adder = SimpleAdder()
    adder.show_intro()
    a0, b0, c0 = adder.get_user_input()
    a0andb0, a0orb0, a0xorb0 = adder.logic_gates(a0, b0)
    adder.show_logic_gates(a0, b0, a0andb0, a0orb0, a0xorb0)
    suma0b0, c1, c2, carry_bit, result = adder.calculate_result(a0, b0, c0, a0xorb0)
    adder.show_result(a0, b0, c0, c1, c2, a0xorb0, suma0b0, carry_bit, result)
    adder.quit()

if __name__ == '__main__':
    main()
