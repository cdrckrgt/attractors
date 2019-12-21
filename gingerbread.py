import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

def ginger(x, y):
    x_prime = 1 - y + abs(x)
    y_prime = x
    return x_prime, y_prime

# how many random initializations we have
nb_inits = int(2e2)
# how many steps we propagate each initialization
nb_steps = int(1e4)

x = np.empty(nb_inits * (nb_steps + 1))
y = np.empty(nb_inits * (nb_steps + 1))

for i in range(nb_inits):

    idx = nb_steps * i

    x[idx] = 20 * np.random.rand() - 10
    y[idx] = 20 * np.random.rand() - 10

    for j in range(nb_steps):
        x_prime, y_prime = ginger(x[idx + j], y[idx + j])
    
        x[idx + j + 1] = x_prime
        y[idx + j + 1] = y_prime
    
fig = plt.figure()
ax = plt.axes()

ax.set_xlim(-20, 45)
ax.set_ylim(-20, 45)
for i in range(nb_inits):
    ax.scatter(x[nb_steps * i: nb_steps * (i + 1)], y[nb_steps * i: nb_steps * (i + 1)], marker='o', s=(72. / fig.dpi) ** 2)# , marker=',', linewidth=0.4)

plt.savefig('gingerbread.png')

plt.show()
