import math
import numpy as np

from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt

def rossler(x, y, z, a=0.2, b=0.2, c=5.7):
    x_prime = -y - z 
    y_prime = x + a * y
    z_prime = b + z * (x - c)
    return x_prime, y_prime, z_prime

dt = 0.01
# how many random initializations we have
nb_inits = int(1e1)
# how many steps we propagate each initialization
nb_steps = int(1e4)

x = np.empty(nb_inits * (nb_steps + 1))
y = np.empty(nb_inits * (nb_steps + 1))
z = np.empty(nb_inits * (nb_steps + 1))

for i in range(nb_inits):

    idx = nb_steps * i

    x[idx] = 5 * np.random.rand() - 1
    y[idx] = 5 * np.random.rand() - 1
    z[idx] = 5 * np.random.rand() - 1

    for j in range(nb_steps):
        x_prime, y_prime, z_prime = rossler(x[idx + j], y[idx + j], z[idx + j])
    
        x[idx + j + 1] = x[idx + j] + x_prime * dt
        y[idx + j + 1] = y[idx + j] + y_prime * dt
        z[idx + j + 1] = z[idx + j] + z_prime * dt
    
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.set_xlim3d(-20, 20)
ax.set_ylim3d(-20, 20)
ax.set_zlim3d(-20, 20)

ax.scatter3D(x, y, z, c=z, marker='o', s=(72. / fig.dpi) ** 2)

plt.savefig('rossler.png')

plt.show()
