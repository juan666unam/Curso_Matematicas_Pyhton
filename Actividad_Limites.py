#Juan Carlos Vargas Castro
#Actividad del tema de límites

from sympy import symbols, limit, sqrt
x  = symbols('x')
fx = (x**2 - 4)/((sqrt(x + 7)) - ((3/2) * sqrt(x + 2)))
limf = limit(fx, x, 2)
print("El límite es: ", limf)