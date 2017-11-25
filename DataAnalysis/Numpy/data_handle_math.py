
'''
sum 对数组中全部或某轴向的元素求和。零长度的数组的sum为0。

mean 算术平均数。零长度的数组的mean为NaN。

std, var 分别为标准差和方差，自由度可调(默认为n)。

min, max 最大值和最小值

argmin 分别为最大值和最小值的索引

cumsum 所有元素的累计和

cumprod 所有元素的累计积

'''


# 标准差和方差的解释


# cumsum和cumprod的解释

import numpy as np
import numpy.random as np_random

print('求和，求平均')
arr = np.random.randn(5, 4)
print(arr )
print( arr.mean())
print( arr.sum())
print( arr.mean(axis = 1))  # 对每一行的元素求平均
print( arr.sum(0))  # 对每一列元素求和，axis可以省略。

# cumsum:
# - 按列操作：a[i][j] += a[i - 1][j]
# - 按行操作：a[i][j] *= a[i][j - 1]
# cumprod:
# - 按列操作：a[i][j] += a[i - 1][j]
# - 按行操作：a[i][j] *= a[i][j - 1]

print('cunsum和cumprod函数演示')
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(0))
print(arr.cumprod(1))


# 带axis参数的统计函数



import numpy as np
import numpy.random as np_random

''' sum对True值计数 '''
# print ('对正数求和')
# arr = np_random.randn(100)
# print((arr > 0).sum())
# print ('对数组逻辑操作')

''' any和all测试布尔型数组，对于非布尔型数组，所有非0元素将会被当做True '''
# bools = np.array([False, False, True, False])
# print (bools.any()) # 有一个为True则返回True
# print (bools.all()) # 有一个为False则返回False

