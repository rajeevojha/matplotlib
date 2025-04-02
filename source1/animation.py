from matplotlib import pyplot as plt
import numpy as np

import random

heads_tails = [0,0]

for _ in range (100000):
    heads_tails[random.randint(0,1)] += 1
    plt.bar(['Heads', 'Tails'], heads_tails,color=['blue','red'])
    plt.pause(0.05)
    plt.clf()
plt.show()
