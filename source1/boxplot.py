import matplotlib.pyplot as plt
import numpy as np

heights = np.random.normal(172, 8, 300)

plt.boxplot(heights)

plt.show()