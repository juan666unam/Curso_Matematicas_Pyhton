#Juan Carlos Vargas Castro
#Actividad Méotodo Babilónico

import math

n = float(input("Dame el valor del cual quieres la raíz: "))
aprox = float(input("Da una aproximación: "))

max_dif = 0.000000000000001     #Máxima diferencia admisible
raiz_math = math.sqrt(n)
dif = abs(raiz_math - aprox)    #Diferencia entre entre el valor de math y el de la aproximación

c = 0
while dif > max_dif:
    c += 1
    aprox = (1/2)*(aprox +  n/aprox)
    dif = abs(raiz_math - aprox)

print("La raíz aproximada de  {0} es {1:.49} ".format(n,aprox))
print("La raíz con math de {0} es {1:.49}".format(n,math.sqrt(n)))
print("La diferencia entre la obtenida con math y la aproximada es de {0:.49}".format(dif))
print("La cantidad de iteraciones fueron : ", c)

'''
raíz de 11 con aproximación de 3: 4 iteraciones
raíz de 2 con aproximación de 1: 5 iteraciones
raíz de 11 con aproximación de 2: 8 repeticiones
'''