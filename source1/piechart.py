import matplotlib.pyplot as plt
import numpy as np

colors = ["red", "blue", "green", "purple", "orange"]
votes = [30,12,43,5,15]
explode = [0.1,0,0,.5,0]
plt.pie(votes, labels=colors, autopct='%1.1f%%', startangle=90,explode=explode) #autopct is used to show percentage on the pie chart

plt.show()
