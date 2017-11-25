
'''
	Scipy : 是一种使用NumPy来做高等数学、信号处理、优化、统计的扩展包 http://docs.scipy.org/doc/

		Linear Algebra (scipy.linalg)

		Statistics (scipy.stats)

		Spatial data structures and algorithms (scipy.spatial)

''' 

import numpy as np

from scipy import linalg

A = np.array([[1,2],[3,4]])

a = linalg.det(A)

print(a)

    