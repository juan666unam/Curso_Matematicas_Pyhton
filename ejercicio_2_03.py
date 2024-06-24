from random import randint

n = 10
ac = 0
for i in range(1,n+1):
    a = randint(1,10)
    b = randint(1,10)
    c = int(input(str(i) + '. ¿Cuánto es ' + str(a) + ' x ' + str(b) + '? '))
    if a*b == c:
        print('Correcto')
        ac+=1
    else:
        print('Incorrecto')
print('Tu calificación es: ',ac)
     