from matplotlib import pyplot as plt
import numpy as np

ages = np.random.normal(20,1.5,1000)
print(ages)

plt.hist(ages, bins=20, edgecolor='black',cumulative=True)
plt.show()