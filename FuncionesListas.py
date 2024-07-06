#Juan Carlos Vargas Castro
#Para qué sirven las funciones index, count y remove en las Listas

a = []
for x in range(10):
  if x%2 == 0:
    a.append(x)
print(a)

print(a.index(8))       #index(elemento): retorna el índice que tiene el elemento indicado dentro de la Lista
#print(a.index(10))       #Devuleve errror si el elemento no se encuentra

a.append(6)
print(a)
print(a.count(6))       #count(elemento): retorna la cantidad de veces que el elemento indicado se encuentra dentro de la Lista
print(a.count(10))      #Devuelve 0 si el elemento no se encuentra

a.remove(2)             #remove(elemento): remueve de la Lista el elemento indicado
print(a)
a.remove(6)             #si el elemento esta repetido, remueve la primera ocurrencia
print(a)
#a.remove(10)            #Devuleve errror si el elemento no se encuentra dentro de la Lista
