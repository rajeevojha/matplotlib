import matplotlib.pyplot as plt
import numpy as np

stock_a = [102,101,100,103,102]
stock_c = [95,98,97,99,93]
stock_b = [92,94,91,90,91]

plt.plot(stock_a, label='Stock A')
plt.plot(stock_b, label='Stock B')
plt.plot(stock_c, label='Stock C')
plt.legend()
plt.show()
