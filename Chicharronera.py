import math
import cmath

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

def raiz(a,b,c):
    d = (b**2-4*a*c)/2*a
    
    if d < 0:
        r = cmath.sqrt(d)
    else:
        r = math.sqrt(d)

    return r

r = raiz(a,b,c)

x1 = -b + r
x2 = -b - r

print("x1 = ",x1)
print("x2 = ",x2)