#Juan Carlos Vargas Castro
#Gráficas de funciones parametrizadas

from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')

def x(t):
  return cos(t) + ((1/2) * cos(7*t)) + ((1/3) * sin(17*t))

def y(t):
  return sin(t) + ((1/2) * sin(7*t)) + ((1/3) * cos(17*t))

plot_parametric(x(t), y(t), (t, 0, 14*pi));
