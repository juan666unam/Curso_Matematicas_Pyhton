from math import *

vo = float(input('Indica la velocidad inicial (en m/s):'))
a = radians(float(input('Indica el ángulo de lanzamiento (en grados):')))
dt = float(input('Indica el intervalo de tiempo (en segundos):'))

x = 0
y = 1
t = 0

while y > 0:
    t+=dt
    x = vo * cos(a) * t
    y = vo * sin(a) * t - 9.81 * t**2 / 2
    if y > 0:
        print('La posición (x,y) del objeto en el segundo',t,'es (',x,',',y,')')
    