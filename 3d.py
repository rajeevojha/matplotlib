import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, c=z, cmap='Greens')
ax.set_title('3D Scatter Plot',loc='right')
plt.show()
plt.savefig('3d.png',dpi=300)