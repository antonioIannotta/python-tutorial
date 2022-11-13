import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 0.1, 500)
result = plt.hist(data, 5)

plt.xlabel('X')
plt.ylabel('PDF')
plt.title('Histogram example')
plt.show()