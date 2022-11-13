import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0.0, 20.0, 0.1)
plt.plot(data, np.sin(data), 'r--', label='Sin function')
plt.plot(data, np.cos(data), 'b--', label='Cos function')
plt.xlabel('Values')
plt.ylabel('Functions')
plt.title('Simple example')
plt.xticks([0, 5, 10, 15, 20])
plt.legend(loc='upper left')
plt.show()