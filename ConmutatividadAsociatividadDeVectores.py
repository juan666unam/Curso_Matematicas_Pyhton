#Juan Carlos Vargas Castro
#Propiedades Conmutativa y Asociativa de la Suma de Vectores

def suma_2_vectores(vector1, vector2):
  # Validamos que los vectores sean del mismo tamaño
  if len(vector1) != len(vector2):
    raise ValueError("Los vectores NO son del mismo tamaño")

  # Creamos una lista vacía
  suma = []

  # Agregamos a la lista la suma cada cada uno de los elementos de cada vector 
  for i in range(len(vector1)):
    suma.append(vector1[i] + vector2[i])

  return suma

# Pruebas de la función suma_2_vectores
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
suma1 = suma_2_vectores(vector1, vector2)
print(f'La suma de {vector1} + {vector2} es {suma1}')

# Prueba de la Conmutatividad
suma2 = suma_2_vectores(vector2, vector1)
print(f'La suma de {vector2} + {vector1} es {suma2}')

if suma1 == suma2:
  print(f'La suma de {vector1} + {vector2} ES IGUAL a La suma de {vector2} + {vector1} ({suma2})')
  print('Por lo tanto, la suma de vectores ES Conmutativa')
else:
  print('La suma de vectores NO es Conmutativa')

# Prueba de la Asociatividad
vector3 = [7, 8, 9]

#(v1 + v2) + v3
suma_v12 = suma_2_vectores(vector1, vector2)
suma_v12_3 = suma_2_vectores(suma_v12, vector3)

#v1 + (v2 + v3)
suma_v23 = suma_2_vectores(vector2, vector3)
suma_v1_23 = suma_2_vectores(vector1, suma_v23)

#(v1 + v3) + v2
suma_v13 = suma_2_vectores(vector1, vector3)
suma_v13_2 = suma_2_vectores(suma_v13, vector2)

if (suma_v12_3 == suma_v1_23) and (suma_v12_3 == suma_v13_2) and (suma_v1_23 == suma_v13_2):
  print(f'La suma de ({vector1} + {vector2}) + {vector3}) es {suma_v12_3}')
  print(f'La suma de {vector1} + ({vector2} + {vector3}) es {suma_v1_23}')
  print(f'La suma de ({vector1} + {vector3}) + {vector2}) es {suma_v13_2}')
  print('Por lo tanto, la suma de vectores ES Asociativa')
else:
    print('La suma de vectores NO ES Asociativa')
