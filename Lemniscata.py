#Juan Carlos Vargas Castro
#Gráficas polares: lemniscata

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(1, 4 * np.pi, 4000)
r = np.sqrt(3    * np.cos(2 * theta))

plt.polar(theta, r, marker='+',color=(.2,.4,.5,.3) )
plt.title("Lemniscata")
plt.show()