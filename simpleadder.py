#!/usr/bin/env python3

'''
simpleadder.py
'''

class SimpleAdder():

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

    def get_user_input(self):
        a0 = int(input('Set the first number to 0 or 1: '))
        b0 = int(input('Set the second number to 0 or 1: '))
        c0 = int(input('Set the carry bit to 0 or 1: '))
        return a0, b0, c0

    def display_output(self, a0, b0):
        print('-' * 38)
        self.a0, self.b0 = a0, b0
        a0andb0 = self.and_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' AND ' + str(b0) + ': ' + str(a0andb0))
        a0orb0 = self.or_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' OR  ' + str(b0) + ': ' + str(a0orb0))
        a0xorb0 = self.xor_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' XOR ' + str(b0) + ': ' + str(a0xorb0))
        print('-' * 38)

    def full_adder(self, a0, b0, c0):
        self.a0, self.b0, self.c0 = a0, b0, c0
        result = 00
        print('\nInitial state of adder circuit:')
        print('A: ' + str(a0))
        print('B: ' + str(b0))
        print('C (CARRY): ' + str(c0))
        print('\nCalculate the sum of A and B:')
        a0xorb0 = self.xor_gate(a0, b0)
        print('A XOR B (' + str(a0) + ' + ' + str(b0) + '): ' + str(a0xorb0))
        print('\nFactor in the previous carry bit:')
        suma0b0 = self.xor_gate(a0xorb0, c0)
        print('SUM = (A XOR B) XOR C (' + str(a0xorb0) +  ' + ' + str(c0) + '): ' + str(suma0b0))
        print('\nGenerate the input values for carry bit calculation:')
        c1 = self.and_gate(a0xorb0, c0)
        print('C1 = (A XOR B) AND C (' + str(a0xorb0) + ' + ' + str(c0) + '): ' + str(c1))
        c2 = self.and_gate(a0, b0)
        print('C2 = A AND B (' + str(a0) + ' + ' + str(b0) + '): ' + str(c2))
        print('\nCalculate the carry bit')
        carry_bit = self.or_gate(c1, c2)
        print('CARRY = C1 OR C2 (' + str(c2) + ' + ' + str(c1) + '): ' + str(carry_bit))
        print('\nConcatenate the carry bit and sum bit for the final 2-bit result:')
        result = str(carry_bit) + str(suma0b0)
        print('RESULT (CARRY|SUM): ' + result + '\n')

def main():
    adder = SimpleAdder()
    title = '2-bit Binary Adder'
    print(title)
    print('-' * len(title) + '\n')
    a0, b0, c0 = adder.get_user_input()
    print('\nThe addition calculation is: '+ str(a0) + ' plus ' + str(b0) +  ', carry ' + str(c0) + '\n')
    adder.display_output(a0, b0)
    adder.full_adder(a0, b0, c0)
    input('Press ENTER to quit: ')


if __name__ == '__main__':
    main()
