import matplotlib.pyplot as plt
import numpy as np

colors = ["red", "blue", "green", "purple", "orange", "yellow", "black", "pink", "brown", "cyan"]
percentvote = [30, 20, 15, 10, 5, 5, 5, 5, 3, 2]

plt.bar(colors, percentvote,lw=2)
plt.title("Color choices of students")
plt.xlabel("Colors")
plt.ylabel("Percentage of votes")
plt.yticks(percentvote,[str(x) + "%" for x in percentvote])
plt.show()