ClaseEquiv0 = set()    #Conjunto vacíoa
ClaseEquiv1 = set()    #Conjunto vacíoa
ClaseEquiv2 = set()    #Conjunto vacíoa
ClaseEquiv3 = set()    #Conjunto vacíoa
ClaseEquiv4 = set()    #Conjunto vacíoa


for i in range(100):
    if i % 5 == 0:
        ClaseEquiv0.add(i)
        ClaseEquiv0.add(-i)
    elif i % 5 == 1:
        ClaseEquiv1.add(i)
        ClaseEquiv1.add(-i)
    elif i % 5 == 2:
        ClaseEquiv2.add(i)
        ClaseEquiv2.add(-i)
    elif i % 5 == 3:
        ClaseEquiv3.add(i)
        ClaseEquiv3.add(-i)
    else:
        ClaseEquiv4.add(i)
        ClaseEquiv4.add(-i)

print("Clase [0] = ", sorted(ClaseEquiv0))
print("Clase [1] = ", sorted(ClaseEquiv1))
print("Clase [2] = ", sorted(ClaseEquiv2))
print("Clase [3] = ", sorted(ClaseEquiv3))
print("Clase [4] = ", sorted(ClaseEquiv4))

print("La intersección de los t5 conjuntos es: ",
      ClaseEquiv0 & ClaseEquiv1 & ClaseEquiv2 & ClaseEquiv3 & ClaseEquiv4)

print("La unión de los 5 conjuntos es: ",
      sorted(ClaseEquiv0 | ClaseEquiv1 | ClaseEquiv2 | ClaseEquiv3 | ClaseEquiv4))