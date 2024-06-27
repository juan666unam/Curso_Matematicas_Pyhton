from sympy import linsolve, symbols

p, a, o = symbols('p a o')
aficionado = {p : 'pumas', a: 'américa', o : 'otro equipo'}

var =[p, a, o]
sol = linsolve([p + a + o - 72000, p - a + 0*o - 8500, 3*p + 3*a - 13*o + 0],
         var)

#print(type(sol))

i=0
for v in sol:
    for y in v:
        print(f'Los aficionados de {aficionado[var[i]]} son {y}')
        i+=1