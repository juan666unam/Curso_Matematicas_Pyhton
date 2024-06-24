d = float(input('Indica la distancia entre las 2 ciudades en Km: '))
va = float(input('Indica la velocidad del vehículo A en Km/h: '))
vb = float(input('Indica la velocidad del vehículo B en Km/h: '))

xa = va * d / (va + vb)
xa = xa * 1000

print('La distancia (en metros) donde se dará el choque respecto al punto de partida de A es: ',xa)