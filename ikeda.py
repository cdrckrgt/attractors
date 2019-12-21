import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def ikeda(x, y, u=0.918):
    t = 0.4 - 6 / (1 + x ** 2 + y ** 2)
    x_prime = 1 + u * (x * math.cos(t) - y * math.sin(t))
    y_prime = u * (x * math.sin(t) + y * math.cos(t))
    return x_prime, y_prime

# how many steps we propagate
nb_iters = int(1e8)
nb_particles = int(5e4)

# rather than draw the attractor directly, let's
# instead use a histogram to determine where we
# spend most of our time
h, w = 1600, 1600
hist = np.zeros((h, w), dtype=int)

x_min = -2
x_max = 8

y_min = x_min * (h / w) - 2
y_max = x_max * (h / w) + 1

print('x_min: ', x_min)
print('x_max: ', x_max)
print('y_min: ', y_min)
print('y_max: ', y_max)

for i in range(nb_iters):
    if i % nb_particles == 0:
        x, y = np.random.randn() * 20, np.random.randn() * 20
    x, y = ikeda(x, y)
    # allow particles to settle
    if i % nb_particles < int(5e1):
        continue

    x_i = int( (x - x_min) * w / (x_max - x_min) )
    y_i = int( (y - y_min) * h / (y_max - y_min) )
    if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
        # remember that matrix is row by columns
        hist[y_i, x_i] += 1

im = np.zeros((h, w, 3), dtype=int)
sens = 1.5e-2
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

plt.savefig('ikeda.png', dpi=600.)

plt.show()
