import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# intervalo de visualização
a = -2.5
b = 2
f = np.poly1d([1, -1, -1])
#plota intervalo par visualização
pts = np.linspace(a, b, 100)
plt.plot(pts, f(pts))
plt.hlines(0,a,b,'g')

plt.show()