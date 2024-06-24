from random import randint

k = int(input('Indica la suma de los 2 dados: '))

if k > 1 and k < 13:
    m = 0
    for i in range(1000):
        suma = randint(1,12) + randint(1,12)
        m+=suma==k
    print('La probabilidad de que la suma sea ',k,' en 1000 tiradas es de ',m/1000)
else:
    print('No es una suma válida')