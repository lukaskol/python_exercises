#!/usr/bin/env python3

# to run this script type ./rownanie_kwadratowe.py -a 2 -b 3 -c 1

import getopt
import sys
import math

a, b, c = 0, 0, 0


try:
    opts, args = getopt.getopt(sys.argv[1:], 'a:b:c:')

    for opt, arg in opts:
        if opt == '-a':
            a = int(arg)
        elif opt == '-b':
            b = int(arg)
        elif opt == '-c':
            c = int(arg)
except getopt.GetoptError:
    print('rownanie_kwadratowe -a <a> -b <b> -c <c>')
    exit(2)

print('Równanie: %dx^2 + %dx + %d = 0' % (a, b, c))

delta = b * b - 4 * a * c

if delta >= 0:
    xa = (-b-math.sqrt(delta))/(2*a)
    xb = (-b+math.sqrt(delta))/(2*a)
    print('x1 = %d\nx2 = %d' % (xa, xb))

else:
    print('Cannot solve this problem')
