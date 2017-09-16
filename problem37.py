import numpy as np
import sysconfig
import sys
import matplotlib.pyplot as plt

N = 300
maxiter = 1000
step = 4.0 / N
rx = []
ry = []
for i in np.arange(-2.0, 2.0, step) :
    for j in np.arange(-2.0, 2.0, step) :
        c = complex(i, j)
        z = complex(0.0, 0.0) + c
        k = 0
        while k < maxiter and np.absolute(z) < 2.0 :
            z = z**2 + c
            k += 1
        if k == maxiter :
            rx.append(z.real)
            ry.append(z.imag)

heatmap, xedges, yedges = np.histogram2d(rx, ry, bins=100)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()
