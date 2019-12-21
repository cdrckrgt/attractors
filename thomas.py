import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def thomas(x, y, z, b=0.208186):
    x_prime = math.sin(y) - b * x
    y_prime = math.sin(z) - b * y
    z_prime = math.sin(x) - b * z
    return x_prime, y_prime, z_prime

# how many steps we propagate
nb_iters = int(1e7)
nb_particles = int(1e4)
dt = 0.01

# rather than draw the attractor directly, let's
# instead use a histogram to determine where we
# spend most of our time
h, w = 1600, 1600
hist = np.zeros((h, w), dtype=int)

x_min = -6
x_max = 6

y_min = x_min * (h / w)
y_max = x_max * (h / w)

print('x_min: ', x_min)
print('x_max: ', x_max)
print('y_min: ', y_min)
print('y_max: ', y_max)


for i in range(nb_iters):
    if i % nb_particles == 0:
        x = 2 * np.random.rand() - 1
        y = 2 * np.random.rand() - 1
        z = 2 * np.random.rand() - 1

    x_prime, y_prime, z_prime = thomas(x, y, z)

    x += x_prime * dt
    y += y_prime * dt
    z += z_prime * dt

    # allow particles to settle
    if nb_iters < int(5e1):
        continue

    x_i = int( (x - x_min) * w / (x_max - x_min) )
    # we are only plotting the x and z axes here
    y_i = int( (z - y_min) * h / (y_max - y_min) )
    if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
        # remember that matrix is row by columns
        hist[y_i, x_i] += 1

im = np.zeros((h, w, 3), dtype=int)
sens = 2.5e-4
color = (36, 169, 174)
for i in range(h):
    for j in range(w):
        val = hist[i, j]
        r = int((1. - math.exp(-sens * val * color[0])) * 255)
        g = int((1. - math.exp(-sens * val * color[1])) * 255)
        b = int((1. - math.exp(-sens * val * color[2])) * 255)
        im[i, j, :] = r, g, b

plt.axis('off')

plt.imshow(im)

plt.savefig('thomas.png', dpi=600.)

plt.show()
