import matplotlib.pyplot as plt
import numpy as np

data1 = np.array([71.4, 3.1, 0.4, 0.3, 24.8])
label = ['Christianity', 'Islam', 'Buddhism', 'Hinduism', 'Other']
plt.pie(data1)
plt.legend(label)
plt.title('Religion in Italy')
plt.show()