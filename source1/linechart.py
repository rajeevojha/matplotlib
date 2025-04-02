import matplotlib.pyplot as plt
import numpy as np
import math

years = [2000 + x for x in range(10)]
weights = [80 +  np.random.random(x)*10  for x in range(10)]
weights = [80,82,81,79,84,88,84,82,81,80]
# print(len(years), len(weights))

plt.plot(years, weights,c='g',lw=2,linestyle='--')
plt.show()