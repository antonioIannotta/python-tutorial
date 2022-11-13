import matplotlib.pyplot as plt
import numpy as np

data0 = np.random.normal(0, 0.5, size=(2, 100))
data1 = np.random.normal(1.0, 0.1, size=(2, 100))

plt.scatter(data0[0], data0[1], c='r', marker='*')
plt.scatter(data1[0], data1[1], c='b', marker='o')

plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Scatter Plot example')
plt.show()