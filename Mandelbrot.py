"""
MANDELBROT SET

By: Johan and CoPilot
"""
import sys
sys.path.append(r'c:\users\p070200\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages')
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 256

r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.axis("off")
plt.subplots_adjust(bottom=0.0, top=1.0, left=0.0, right=1.0)
plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='turbo')
#plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
