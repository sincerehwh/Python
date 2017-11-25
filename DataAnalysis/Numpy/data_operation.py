
# -*- coding: utf-8 -*-

# 数组和标量之间的运算

'''
	1.无需循环即可以批量运算
	2.大小相同的数组元素之间的运算可以应用到元素级别
	3.标量和数组之间的运算应用到元素级别

'''

import numpy as np

# 数组乘法/减法
# array = np.array([[0,2,3,4,5],[1,2,3,4,5]])
# print(array**2)
# print(array[0:2])


# 对高纬数组的访问和操作
# 使用切片访问和操作数组
# a1 = np.array([1,2,3,4,5,6,7,8,9])
# print(a1[0:5])

a2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("a2: ",a2)
#print(a2[:5])
#print(a2[:2,:3]) # 0-1行，0-2列

#a2[:,0:2] = 0

#print(a2) # 这就是操作数组的极品啊！！！


# 布尔型索引
# import numpy.random as np_random
# name_array = np.array(["a","b","c","d","e","f","g","h",'i','j'])
# random_array = np_random.randn(10,10)
# print(random_array)
# print(name_array=="a")
#print(random_array[name_array=="b",:3]) # 切片必须和数组一样大


# 花式索引
# a2 3行，四列
print(a2[:,:]) # 所有行，所有列
print(a2[1,:]) # 第1行的所有元素
print(a2[[1,2],:]) # 第一行，第二行的所有元素
print(a2[:,[1,2,3]]) # 所有行的1，2，3列元素
print(a2[[1,1],[2,3]]) # 第一行的index=2的元素，第一行的index=3的元素


level_1_1 = [1,1,1]
level_1_2 = [2,2,2]
level_1_3 = [3,3,3]
level_2 = [level_1_1,level_1_2,level_1_3]
level_3 = [level_2,level_2,level_2]

a3 = np.array(level_3)
print(a3[[0],[0],[0]]) # 行、列、层





