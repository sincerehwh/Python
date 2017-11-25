'''

	seed 确定随机数生成器的种子

	permutation	返回一个序列的随机排列或返回一个随机排列的返回

	shuffle	对一个序列就地随机乱序

	rand 产生均匀分布的样本值

	randint 从给定的上下限范围内随机选取整数

	randn 产生正态分布(平均值为0，标准差为1)

	binomial 产生二项分布的样本值

------ 2

	normal 产生正态(高斯)分布的样本值

	beta 产生Beta分布的样本值

	chisquare 产生卡方分布的样本值

	gamma 产Gamma分布的样本值

	uniform 产生在[0, 1]中均匀分布的样本值

'''


import numpy as np
import numpy.random as np_random
from random import normalvariate

print('正态分布随机数')

samples = np.random.normal(size=(4, 4))
print(samples)


print('\n批量按正态分布生成0到1的随机数')
N = 10
print([normalvariate(0, 1) for _ in xrange(N)])
print(np.random.normal(size = N))  # 与上面代码等价
