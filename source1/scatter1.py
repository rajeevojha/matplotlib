import matplotlib.pyplot as plt
import numpy as np

X_data = np.random.rand(100)
Y_data = np.random.random(100) * 100

plt.scatter(X_data, Y_data,c="green", alpha=0.5,marker='$\heartsuit$')
plt.show()
