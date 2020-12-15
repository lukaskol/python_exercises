import math


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __abs__(self):
        return math.sqrt((self.re ** 2) + (self.im ** 2))

    def __add__(self, other):
        if type(other) == Complex:
            return Complex((self.re + other.re), (self.im + other.im))
        else:
            return Complex(self.re + other, self.im)

    __radd__ = __add__

    def __sub__(self, other):
        if type(other) == Complex:
            return Complex((self.re - other.re), (self.im - other.im))
        else:
            return Complex(self.re - other, self.im)

    def __rsub__(self, other):
        return Complex(other - self.re, self.im)

    def conjugate(self):
        return Complex(self.re, - self.im)

    def __mul__(self, other):
        if type(other) == Complex:
            return Complex((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))
        else:
            return Complex(other * self.re, other * self.im)

    __rmul__ = __mul__

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __str__(self):
        if self.im > 0:
            return '(%g + %gj)' % (self.re, abs(self.im))
        elif self.im < 0:
            return '(%g - %gj)' % (self.re, abs(self.im))
        else:
            return '(%g)' % self.re



