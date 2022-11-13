import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0.0, 20.0, 0.1)
plt.plot(data, np.sin(data), 'r--')
plt.xlabel('Values')
plt.ylabel('Sin function')
plt.title('Simple example')
plt.show()