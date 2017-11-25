'''
Pandas是一种构建于Numpy的高级数据结构和精巧工具，快速简单的处理数据:

	支持自动或明确的数据对齐的带有标签轴的数据结构。
	整合的时间序列功能。
	以相同的数据结构来处理时间序列和非时间序列。
	支持传递元数据(坐标轴标签)的算术运算和缩减。
	灵活处理丢失数据。
	在常用的基于数据的数据库(例如基于SQL)中的合并 和其它关系操作。

数据结构:Series和DataFrame

'''

import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

print(s)

dates = pd.date_range("20130101",periods=6)
print(dates)
