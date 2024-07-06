#Juan Carlos Vargas Castro
#Problema Interprepas Matemáticas VI área 1, gráficas de f o g, g o f y f*g

from sympy import sqrt, symbols, ln
from sympy.plotting import plot

def f(x):
  return sqrt(-x)

def g(x):
  return ln(x)

x = symbols('x')

g1 = plot(f(x), (x, -5, 5), line_color='red', show=False)
g2 = plot(g(x), (x, -5, 5), line_color='blue', show=False)
g3 = plot(f(g(x)), (x, -5, 5), line_color='green', show=False)
g4 = plot(g(f(x)), (x, -5, 5), line_color='brown', show=False)
g5 = plot(f(x)*g(x), (x, -5, 5), line_color='orange', show=False)
g1.append(g2[0])
g1.append(g3[0])
g1.append(g4[0])
g1.append(g5[0])
g1.show()
