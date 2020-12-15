import Complex
import re
import os
from termcolor import colored


def parse(s):
    if type(s) == str:
        s = s.replace("\s", "")
        cplx = re.compile("([-]?[0-9]+\\.?[0-9]?)([-|+]+[0-9]+\\.?[0-9]?)[j$]+")
        real = re.compile("([-]?[0-9]+\\.?[0-9]?)$")
        imag = re.compile("([-]?[0-9]+\\.?[0-9]?)[j$]")

        matcher1 = cplx.match(s)
        matcher2 = real.match(s)
        matcher3 = imag.match(s)

        if matcher1:
            RE = float(matcher1.group(1))
            IM = float(matcher1.group(2))
        elif matcher2:
            RE = float(matcher2.group(1))
            IM = 0
        elif matcher3:
            RE = 0
            IM = float(matcher3.group(1))
        else:
            raise TypeError('Wrong entry!')
        return RE, IM

    else:
        raise TypeError('Function should take string')


os.system('clear')
print("Welcome in complex calc. Insert normal/complex number, select activity and continue.....")
operation = ''
result = input('Number: ')
real, imag = parse(result)
result = Complex.Complex(real, imag)
new = 0

while True:
    print('Choose operation:\n+\n-\n*\nABS\nNOT\nConj\n=')
    choice = input('Choice: ')
    if choice == '=':
        os.system('clear')
        print(colored('RESULT: ', 'green') + str(result))
        print('Bye!')
        break
    new = input('Number: ')
    real, imag = parse(new)
    new = Complex.Complex(real, imag)
    if choice == '+':
        result += new
    elif choice == '-':
        result -= new
    elif choice == '*':
        result *= new
    elif choice == 'ABS':
        result = abs(result)
    elif choice == 'NOT':
        result = -result
    elif choice == 'Conj':
        result = result.conjugate()
    else:
        print('Unknown operation! Try again.')
        continue
    os.system('clear')
    print(colored('RESULT: ', 'green') + str(result))




