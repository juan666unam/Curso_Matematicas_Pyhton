#Juan Carlos Vargas Castro
#Gráficas de funciones implícitas

from sympy import symbols, Eq
from sympy import plot_implicit

x, y, p, v = symbols('x y p v')

g1 = plot_implicit(Eq(x**2 + y**3 - 2*y, 3), (x, -10, 10), (y, -10, 10), line_color='red', show=False)
g2 = plot_implicit(Eq((p + (5/v**2))*(v - 0.03), 9.7), (p, 1, 10), (v, 1, 10), line_color='blue', show=False)
g1.append(g2[0])
g1.show()