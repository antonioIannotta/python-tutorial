import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data0 = np.random.normal(0, 1.0, size=(100,))
sns.kdeplot(data0, color='g', bw_adjust=2, label='Smooth factor=2')
sns.kdeplot(data0, color='r', cumulative=True, label='CDF')
plt.legend()
plt.xlabel('X values')
plt.ylabel('Y values')
plt.show()
