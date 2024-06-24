def es_divisible(pnNumA, pnNumB):
    return pnNumA%pnNumB == 0

def es_primo(pnNum):
    for i in range(2, pnNum):
        if es_divisible(pnNum,i):
            return 0
    return 1

primos = int(input('Indica la cantidad de números primos: '))
c = 0
n = 0
while c < primos:
    n+=1
    if es_primo(n):
        c+=1
        print('El número primo ',c,' es: ',n)
