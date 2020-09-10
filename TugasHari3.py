# soal no 1

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2*-np.pi, 2*np.pi, 200)
tan = np.tan(x)/10
cos = np.cos(x)
sin = np.sin(x)

fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (16, 8), sharey = True)

ax[0].plot(x, tan, color = 'b', label = 'tanx')
ax[0].set_title('Grafik tanx')

ax[1].plot(x, sin, color = 'r', label = 'sinx')
ax[1].set_title('Grafik sinx')

ax[2].plot(x, cos, color = 'g', label = 'cosx')
ax[2].set_title('Grafik cosx')

fig.legend(loc = 'upper center')
plt.show()

# soal no 2

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2*-np.pi, 2*np.pi, 100)
y = np.cos(x)
y2 = np.cos(x**2)
y3 = np.cos(x**3)
y4 = np.cos(x**4)
y5 = np.cos(x**5)

fig, ax = plt.subplots(figsize = (16, 8))

ax.plot(x, y)
ax.set_title('Grafik CosX')

ins1 = ax.inset_axes([-0.1, -0.1, 0.3, 0.3])
ins1.plot(x, y, 'b', x, y2, 'r')
ins1.set_title('Grafik CosX^2')

ins2 = ax.inset_axes([0.9, -0.1, 0.3, 0.3])
ins2.plot(x, y, 'b', x, y3, 'g')
ins2.set_title('Grafik CosX^3')

ins3 = ax.inset_axes([0.9, 0.9, 0.3, 0.3])
ins3.plot(x, y, 'b', x, y4, 'black')
ins3.set_title('Grafik CosX^4')

ins4 = ax.inset_axes([-0.1, 0.9, 0.3, 0.3])
ins4.plot(x, y, 'b', x, y5, 'y')
ins4.set_title('Grafik CosX^5')

plt.show()