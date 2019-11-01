#!/usr/bin/env python3

'''
simpleadder.py
'''

class SimpleAdder(object):

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
        user_input = str(input('Enter a 2-bit binary number: ')).zfill(2)
        print('You entered the number: '+ user_input)

        digits = []
        
        for x in user_input[0:2]:
            digits.append(x)

        a0 = int(digits[0])
        b0 = int(digits[1])

        print('The individual bits are: '+ str(a0) + ' and ' + str(b0))
        return a0, b0

    def display_output(self, a0, b0):
        self.a0, self.b0 = a0, b0

        a0andb0 = self.and_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' AND ' + str(b0) + ': ' + str(a0andb0))

        a0orb0 = self.or_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' OR  ' + str(b0) + ': ' + str(a0orb0))

        a0xorb0 = self.xor_gate(a0, b0)
        print('Logic gate ' + str(a0) + ' XOR ' + str(b0) + ': ' + str(a0xorb0))

        print('-'*78)

    def full_adder(self, a0, b0): 
        self.a0, self.b0 = a0, b0
        c0 = 0
        result = 0

        print('ADDER: A + B (' + str(a0) + ' + ' + str(b0) + ')')
        print('CARRY: 0')
        print('\n')
        
        print('Calculate the sum of A and B')
        a0xorb0 = self.xor_gate(a0, b0)
        print('A XOR B (' + str(a0) + ' + ' + str(b0) + '): ' + str(a0xorb0))
        print('\n')
        
        print('Factor in the previous carry bit')
        suma0b0 = self.xor_gate(a0xorb0, c0)
        print('SUM = (A XOR B) XOR C (' + str(a0xorb0) +  ' + ' + str(c0) + '): ' + str(suma0b0))
        print('\n')
        
        print('Generate the input values for carry bit calculation')
        c1 = self.and_gate(a0xorb0, c0)
        print('C1 = (A XOR B) AND C (' + str(a0xorb0) + ' + ' + str(c0) + '): ' + str(c1))
        c2 = self.and_gate(a0, b0)
        print('C2 = A AND B (' + str(a0) + ' + ' + str(b0) + '): ' + str(c2))
        print('\n')
        
        print('Calculate the carry bit')
        carry_bit = self.or_gate(c1, c2)
        print('CARRY = C1 OR C2 (' + str(c2) + ' + ' + str(c1) + '): ' + str(carry_bit))
        result = str(carry_bit) + str(suma0b0)
        print('\n')
        
        print('RESULT (CARRY|SUM): ' + result)

def main():
    adder = SimpleAdder()

    a0, b0 = adder.get_user_input()

    adder.display_output(a0, b0)
    
    adder.full_adder(a0, b0)
	
    # input('Press ENTER to quit: ')


if __name__ == '__main__':
    main()
