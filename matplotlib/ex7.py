import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0.0, 20.0, 0.1)
plt.plot(data, np.power(data, 2), 'ro-', linewidth=0.1, label='Sqr function')
plt.plot(data, np.sqrt(data), 'b*-', linewidth=2, label='Sqrt function')
plt.xlabel('X')
plt.ylabel('F(X)')
plt.title('Line example')
plt.legend(loc='upper left')
plt.show()