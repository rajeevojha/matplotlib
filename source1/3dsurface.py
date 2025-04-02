import matplotlib.pyplot as plt
import numpy as np

axs = plt.subplot(projection='3d')
x = np.arange(-5, 5, 0.1)
y=np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)

Z = np.sin(X) * np.cos(Y)

axs.plot_surface(X,Y,Z,cmap='viridis')
axs.set_title('3D Surface Plot',loc='right')
axs.set_xlabel('TEST')

plt.show()
plt.savefig('3d_surface.png',dpi=300)