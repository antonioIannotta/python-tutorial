import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0.0, 20.0, 0.1)
plt.plot(data, np.sin(data), '--r')
plt.xlabel('Values')
plt.ylabel('Sin function')
plt.title('Simple example')
plt.text(5, 0, r'$\pi$')
plt.text(10, 1, r'$\frac{\pi}{2}$')
plt.xticks([0, 5, 10, 15, 20])
plt.show()