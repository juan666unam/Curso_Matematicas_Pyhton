#Juan Carlos Vargas Castro
#Actividad del tema de Integrales

from sympy import symbols, Integral, sqrt, integrate

x  = symbols('x')

res = Integral(sqrt(1 + x**2), (x,-1,1))

print("El resultado con Integral es: ", res.evalf())

res = integrate(sqrt(1 + x**2), (x,-1,1))

print("El resultado con integrate es: ", res.evalf())