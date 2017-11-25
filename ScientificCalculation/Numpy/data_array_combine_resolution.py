'''

	concatenate 最一般化的连接，沿一条轴连接一组数组

	vstack, row_stack 以面向行的方式对数组进行堆叠(沿轴0)

	hstack, 以面向行的方式对数组进行堆叠(沿轴1)

	column_stack 类似于hstack，但是会先将一维数组转换为二维列向量。

	dstack 以面向“深度”的方式对数组进行堆叠(沿轴2)

	split 沿指定轴在指定的位置拆分数组

	hsplit, vsplit, dsplit split的便捷化函数，分别沿着轴0、轴1和轴2进行拆分。


''' 

import numpy as np
import numpy.random as np_random


''' 数组重塑 '''

# reshape重塑数组
print("将一维数组转换为二维数组:")
arr = np.arange(8)
print(arr.reshape((4, 2)))
print(arr.reshape((4, 2)).reshape((2, 4))) # 支持链式操作


# -1自动推导维度大小
print("\n维度大小自动推导:")
arr = np.arange(15)
print(arr.reshape((5, -1)))

print("\n获取维度信息并应用:")
other_arr = np.ones((3, 5))
print(other_arr.shape)
print(arr.reshape(other_arr.shape))

print("\n高维数组拉平:")
arr = np.arange(15).reshape((5, 3))
print(arr.ravel())

''' 数组的合并和拆分 '''

# 数组连接函数
print('连接两个二维数组')
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print("\n按行连接: ",np.concatenate([arr1, arr2], axis = 0))  # 按行连接
print("\n按列连接: ",np.concatenate([arr1, arr2], axis = 1))  # 按列连接

# 堆叠
print('垂直stack与水平stack')
print(np.vstack((arr1, arr2))) # 垂直堆叠
print(np.hstack((arr1, arr2))) # 水平堆叠

# 拆分数组

arr = np_random.randn(5, 5)
print(arr)
print('\n水平拆分')
first, second, third = np.split(arr, [1, 3], axis = 0)
print('first: ',first)
print('second',second)
print('third',third)

print('\n垂直拆分')
first, second, third = np.split(arr, [1, 3], axis = 1)
print('first: ',first)
print('second',second)
print('third',third)

# 堆叠辅助类 _r对象
arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np_random.randn(3, 2)

# 堆叠辅助类 _c对象
print('\nr_用于按行堆叠')
print(np.r_[arr1, arr2])

print('\nc_用于按列堆叠')
print(np.c_[np.r_[arr1, arr2], arr])
print('\n切片直接转为数组')
print(np.c_[1:6, -10:-5])

'''  元素的重复操作  '''

# _repeat
print('\nRepeat: 按元素')
arr = np.arange(3)
print(arr.repeat(3))
print(arr.repeat([2, 3, 4])) # 3个元素，分别复制2, 3, 4次。长度要匹配！

print('Repeat，指定轴')
arr = np_random.randn(2, 2)
print(arr.repeat(2, axis = 0)) # 按行repeat
print(arr.repeat(2, axis = 1)) # 按列repeat
print(arr.repeat(2, axis = 0)) # 按行repeat
# _tile
print('Tile: 参考贴瓷砖')
print(np.tile(arr, 2))
print(np.tile(arr, (2, 3)))  # 指定每个轴的tile次数


'''  花式索引的等价函数 '''
print('Fancy Indexing例子代码')
arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print(arr[inds])
# take
print('\n使用take')
print(arr.take(inds))
# put
print('\n使用put更新内容')
arr.put(inds, 50)
arr.put(inds, [70, 10, 20, 60])
print(arr)

print('\ntake，指定轴')
arr = np_random.randn(2, 4)
inds = [2, 0, 2, 1]
print(arr)
print(arr.take(inds, axis = 1))  # 按列take

