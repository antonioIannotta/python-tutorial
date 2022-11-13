import matplotlib.pyplot as plt
import numpy as np

xvalue = [2.873, 2.148, 8.98, 6.642, 3.769]
yvalue = ["Rome", "Paris", "London", "Madrid", "Berlin"]
plt.bar(yvalue, xvalue, color=['m', 'r', 'g', 'b', 'y'], hatch='/')
plt.xlabel('EU capitals')
plt.ylabel('Population in millions')
plt.title('Bar example')
plt.show()