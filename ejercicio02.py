from math import *

r = float(input('Indica el radio de la esfera (en cm): '))
d = float(input('Indica la densidad de su material (en kg/cm3): '))

vol = 4/3*pi*r**3
masa = d * vol
peso = masa * 9.81

print('El peso de la esfera (en Kg) es: ', peso)