#Muestra la fizhas de dominó en el formato [m.n] sin que se repitan
n = 0 #Contador de fichas
for i in range(7):
    for j in range(7):
        if j>=i:
            n+=1
            print('Ficha ',n,' : [',i,',',j,']')