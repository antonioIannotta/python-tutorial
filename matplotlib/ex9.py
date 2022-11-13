import matplotlib.pyplot as plt
import numpy as np

data0 = np.random.normal(0, 0.5, 500)
data1 = np.random.normal(0, 1.0, 500)
data = np.stack((data0, data1), axis=1)
plt.boxplot(data, whis=1.5)
plt.title('Example of Boxplot')
plt.show()