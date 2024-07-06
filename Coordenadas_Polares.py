#Coordenadas polares
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 4000)
r = 3 * np.cos(6 * theta)
x = r * np.sin(theta)
y = r * np.cos(theta)

plt.axis('off')
plt.axis('equal')
plt.plot(x,y)
#plt.axis('scaled')
#plt.xlim(0,5)
#plt.ylim(0,5)
plt.show
plt.show


theta = np.linspace(1, 4 * np.pi, 4000)
r = np.sqrt(3 * np.cos(2 * theta))

plt.polar(theta, r, marker='+',color=(.2,.4,.5,.3) )
plt.title("Lemniscata")
plt.show()
