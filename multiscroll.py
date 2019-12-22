import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

n = 3
b = [0, 1., 2.15, 3.6, 8.2, 13.]
m = [-1./7, 2./7, -4./7, 2./7, -4./7, 2./7] 

def h_(x):
    return m[2 * n - 1] * x + 0.5 * sum( [ (m[k - 1] - m[k]) * (abs(x + b[k]) - abs(x - b[k])) for k in range(1, 2 * n) ] )

def nscroll(x, y, z, alpha=9., beta=14.286, gamma=0):
    x_prime = alpha * (y - h_(x))
    y_prime = x - y + z
    z_prime = -beta * y - gamma * z
    return x_prime, y_prime, z_prime

# how many steps we propagate
nb_iters = int(1e8)
nb_particles = int(1e4)
dt = 0.01

# rather than draw the attractor directly, let's
# instead use a histogram to determine where we
# spend most of our time
h, w = 2400, 3200
hist = np.zeros((h, w), dtype=int)

x_min = -35
x_max = 35

y_min = x_min * (h / w) + 20
y_max = x_max * (h / w) - 20

print('x_min: ', x_min)
print('x_max: ', x_max)
print('y_min: ', y_min)
print('y_max: ', y_max)

for i in range(nb_iters):
    if i % nb_particles == 0:
        x, y, z = np.random.randn() * 15, np.random.randn() * 15, np.random.randn() * 15
    x_prime, y_prime, z_prime = nscroll(x, y, z)

    x += x_prime * dt
    y += y_prime * dt
    z += z_prime * dt

    # allow particles to settle
    if nb_iters < int(5e1):
        continue

    x_i = int( (x - x_min) * w / (x_max - x_min) )
    # we are only plotting the x and z axes here
    y_i = int( (y - y_min) * h / (y_max - y_min) )
    if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
        # remember that matrix is row by columns
        hist[y_i, x_i] += 1

im = np.zeros((h, w, 3), dtype=int)
sens = 4e-4
color = (36, 169, 174)
for i in range(h):
    for j in range(w):
        val = hist[i, j]
        r = int((1. - math.exp(-sens * val * color[0])) * 255)
        g = int((1. - math.exp(-sens * val * color[1])) * 255)
        b = int((1. - math.exp(-sens * val * color[2])) * 255)
        im[i, j, :] = r, g, b

plt.imsave('{}-doublescroll.png'.format(n), im, dpi=600, origin='lower')

plt.axis('off')
plt.imshow(im)
plt.show()
