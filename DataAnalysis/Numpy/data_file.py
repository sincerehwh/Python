
'''
	- 将数组以二进制格式保存到磁盘

	- 存取文本文件

'''

import numpy as np



print('数组文件读写')
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))


print('多个数组压缩存储')
np.savez('array_archive.npz', a = arr, b = arr)
arch = np.load('array_archive.npz')
print(arch['b'])



print('读取csv文件做为数组')
arr = np.loadtxt('array_ex.txt', delimiter = ',')
print(arr)



