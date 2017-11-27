# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sys
from pandas import Series,DataFrame,Index

'''
重新索引：

		• 创建一个适应新索引的新对象，该Series的reindex将会根据新索引进行重排。 如果某个索引值当前不存在，就引入缺失值

		• 对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理。 method选项即可达到此目的

		• reindex函数的参数：

			index：用作索引的新序列。既可以是Index实例，也可以是其它序列型的Python数据 结构。Index会被完全使用，就像没有任何复制一样。
			
			method：插值填充方式，ffill或bfill。

			fill_value：在重新索引过程中，需要引入缺失值时使用的替代值。

			limit：前向或后向填充时的最大填充量

			level：在MultiIndex的指定级别上匹配简单索引，否则选取其子集。

			copy：默认为True，无论如何都复制。如果为False，则新旧相等就不复制。
'''

import random
#导入random模块 用于生产随机数功能
a  =  range(97,123) # random.randint(97, 122)
#利用random.randint()函数生成一个随机整数a，使得97<=a<=122
#对应从“a”到“z”的ASCII码
c = [chr(x) for x in a] 

sers = Series(range(26),index = c)


# 获取Index
index = sers.index
print(index[:2])

# Index对象Read Only
try:
	index[0] = "c"
except :
	print(sys.exc_info()[0])


# 使用Index对象
index = Index(np.arange(9))
sers2 = Series(range(9),index=index)
print(index)
print(sers2.index)
print(sers2.index is index)


# 判断列和索引是否存在
pop = {'name':["n",'m','l','l','l'],
	   'years':[2016,2017,2018,2019,2020]}

sers3 = DataFrame(pop)
print(sers3.columns)
print(sers3.index)



