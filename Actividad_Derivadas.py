#Juan Carlos Vargas Castro
#Actividad del tema de Derivadas

from sympy import symbols, diff, exp, sin, tan, sqrt

x  = symbols('x')
fx = (tan(exp(2*sin(x))/(4*x)))**sqrt(x)
dx = diff(fx, x)
print("La derivada es: \n {0}  \n= {1} ".format(dx, dx.simplify()))

