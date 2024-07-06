#Juan Carlos Vargas Castro
#Actividad 2 de Gráfica de funciones

from sympy import symbols, sin, pi
from sympy.plotting import plot

def f(x):
  y = 0
  for k in (1,101):
    n1 = sin(2*pi*(k**2)*x)
    d1 = 4*(pi**2)*(k**5)
    n2 = x**2
    d2 = 2*k
    div1 = n1/d1
    div2 = n2/d2
    y = y + div1 + div2
  return y

x = symbols('x')

g1 = plot(f(x), (x, -5, 5), line_color='red', show=False)
g1.show()
