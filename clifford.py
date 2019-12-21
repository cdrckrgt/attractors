import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def clifford(x, y, a=-1.7, b=1.8, c=-1.9, d=-0.4):
    x_prime = math.sin(a * y) + c * math.cos(a * x)
    y_prime = math.sin(b * x) + d * math.cos(b * y)
    return x_prime, y_prime

# how many steps we propagate
nb_iters = int(1e7)

# rather than draw the attractor directly, let's
# instead use a histogram to determine where we
# spend most of our time
h, w = 1600, 1600
hist = np.zeros((h, w), dtype=int)

x_min = -3.5
x_max = 3.5

y_min = x_min * (h / w)
y_max = x_max * (h / w)

print('x_min: ', x_min)
print('x_max: ', x_max)
print('y_min: ', y_min)
print('y_max: ', y_max)

x, y = 0, 0

for _ in range(nb_iters):
    x, y = clifford(x, y)

    x_i = int( (x - x_min) * w / (x_max - x_min) )
    y_i = int( (y - y_min) * h / (y_max - y_min) )
    if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
        # remember that matrix is row by columns
        hist[y_i, x_i] += 1

im = np.zeros((h, w, 3), dtype=int)
sens = 3e-4
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

plt.savefig('clifford.png', dpi=600.)

plt.show()
