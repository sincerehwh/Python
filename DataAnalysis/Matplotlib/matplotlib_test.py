'''
	Python绘图库
	

'''

# import matplotlib.pyplot as plt
# plt.plot([1,2,3])
# plt.ylabel("ylab")
# plt.xlabel("xlabel")
# plt.show()


import seaborn as sns

sns.set(color_codes=True)

import numpy as np

x = np.random.normal(size=100)
sns.distplot(x)
