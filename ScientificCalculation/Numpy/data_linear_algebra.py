
'''
	diag 以一维数组的形式返回方阵的对角线(或非对角线元素)，获将一维数组转换 为方阵(非对角线元素为0)。

	dot 矩阵乘法

	trace 计算对角线元素的和

	det 计算矩阵行列式

	eig 计算方阵的特征值和特征向量

	inv 计算方阵的逆

	pinv 计算矩阵的Moore-Penrose伪逆

	qr 计算QR分解

	svd	计算奇异值分解

	solve 解线性方程Ax = b，其中A为一个方阵。

	lstsq 计算Ax = b的最小二乘解

''' 


import numpy as np
import numpy.random as np_random
from numpy.linalg import inv, qr

print('矩阵乘法')
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x.dot(y))
print(np.dot(x, np.ones(3)))


x = np_random.randn(5, 5)
print('\n矩阵求逆:')
mat = x.T.dot(x)
print(inv(mat))  # 矩阵求逆
print(mat.dot(inv(mat))) # 与逆矩阵相乘，得到单位矩阵。

print('\n矩阵消元:')
print(mat)
q, r = qr(mat)
print(q)
print(r)
