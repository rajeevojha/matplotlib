import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine',loc='right')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('cos',loc='right')

axs[1, 0].plot(x, np.random.random(100))
axs[1, 0].set_title('random',loc='right')

axs[1, 1].plot(x, np.log(x))
axs[1, 1].set_xlabel('Log')

fig.suptitle('4 plots Demo', fontsize=16)  

fig.savefig('4_plots.png',dpi=300)

plt.show()