#Suma Vectores
import matplotlib.pyplot as plt

def sumaVectores(z1,z2):
        return (z1[0] + z2[0], z1[1]+z2[1])

def restaVectores(z1,z2):
        return (z1[0] - z2[0], z1[1]-z2[1])


z1 = (2,1)
z2 = (3,4)

suma = sumaVectores(z1,z2)
resta = restaVectores(z1,z2)

plt.quiver(0, 0, z1[0], z1[1], color='g', units='xy', scale=1)
plt.quiver(z1[0],z1[1],z2[0],z2[1], color='b',units='xy', scale=1)

#Grafica de la suma
#plt.quiver(0, 0, suma[0], suma[1], color='r',units='xy', scale=1)

#Grafica de la resta
plt.quiver(z2[0],z2[1], resta[0], resta[1], color='r',units='xy', scale=1)
plt.axis('scaled')
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()