import Complex

cplx1 = Complex.Complex(2, 2)
cplx2 = Complex.Complex(3, 3)

print('STAGE 1')
print('ABS cplx1: %g' % (abs(cplx1)))
print('Conjugate cplx1: %s' % str(cplx1.conjugate()))
print('Neg cplx1: -(%s) = %s' % (str(cplx1), str(-cplx1)))
print('Add cplx1 + cplx2: %s + %s = %s' % (str(cplx1), str(cplx2), str(cplx1 + cplx2)))
print('Sub cplx1 - cplx2: %s - %s = %s' % (str(cplx1), str(cplx2), str(cplx1 - cplx2)))
print('Mul cplx1 * cplx2: %s * %s = %s' % (str(cplx1), str(cplx2), str(cplx1 * cplx2)))

print('\nStage 2')
print('Add cplx1 + const: %s + %s = %s' % (str(cplx1), 4, str(cplx1 + 4)))
print('Sub cplx1 - const: %s - %s = %s' % (str(cplx1), 4, str(cplx1 - 4)))
print('Mul cplx1 * const: %s * %s = %s' % (str(cplx1), 4, str(cplx1 * 4)))

print('\nStage 3')
print('Add const + cplx2: %s + %s = %s' % (4, str(cplx2), str(4 + cplx2)))
print('Sub const - cplx2: %s - %s = %s' % (4, str(cplx2), str(4 - cplx2)))
print('Mul const * cplx2: %s * %s = %s' % (4, str(cplx2), str(4 * cplx2)))