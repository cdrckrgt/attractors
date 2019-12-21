import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def tinkerbell(x, y, a=0.9, b=-0.6013, c=2.0, d=0.5):
    x_prime = x ** 2 - y ** 2 + a * x + b * y
    y_prime = 2 * x * y + c * x + d * y
    return x_prime, y_prime


# how many steps we propagate
nb_iters = int(1e6)

# rather than draw the attractor directly, let's
# instead use a histogram to determine where we
# spend most of our time
h, w = 1600, 1600
hist = np.zeros((h, w), dtype=int)

x_min = -2
x_max = 2

y_min = x_min * (h / w)
y_max = x_max * (h / w)

print('x_min: ', x_min)
print('x_max: ', x_max)
print('y_min: ', y_min)
print('y_max: ', y_max)

x, y = -0.72, -0.64

for _ in range(nb_iters):
    x, y = tinkerbell(x, y)

    x_i = int( (x - x_min) * w / (x_max - x_min) )
    y_i = int( (y - y_min) * h / (y_max - y_min) )
    if (x_i >= 0 and x_i < w \
        and y_i >= 0 and y_i < h):
        # remember that matrix is row by columns
        hist[y_i, x_i] += 1

im = np.zeros((h, w, 3), dtype=int)
sens = 6e-4
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

plt.savefig('tinkerbell.png', dpi=600.)

plt.show()
