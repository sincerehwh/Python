
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
''' sum对True值计数 '''
# print ('对正数求和')
# arr = np_random.randn(100)
# print((arr > 0).sum())
# print ('对数组逻辑操作')

''' any和all测试布尔型数组，对于非布尔型数组，所有非0元素将会被当做True '''
# bools = np.array([False, False, True, False])
# print (bools.any()) # 有一个为True则返回True
# print (bools.all()) # 有一个为False则返回False



''' 排序 直接排序 - 指定轴排序 '''

print('一维数组排序')
arr = np_random.randn(8)
arr.sort()
print(arr)

print('二维数组排序')
arr = np_random.randn(5, 3)
print(arr)
arr.sort(1) # 对每一行元素做排序
print(arr)

print('找位置在5%的数字')
large_arr = np_random.randn(1000)
large_arr.sort()
print (large_arr[int(0.05 * len(large_arr))])


''' 去重:

	unique(x) 计算x中的唯一元素，并返回有序结果。

	intersect1d(x, y) 计算x和y中的公共元素，并返回有序结果。

	union1d(x, y) 计算x和y的并集，并返回有序结果。

	in1d(x, y) 得到一个表述"x的元素是否包含于y"的布尔型数组

	setdiff1d(x, y) 集合的差，即元素在x中且不在y中

	setxor1d(x, y) 集合的异或，即存在于一个数组中但不同时存在于两个数组中的元素

'''


print('用unique函数去重')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(sorted(set(names)))  # 传统Python做法
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

print('查找数组元素是否在另一数组')
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))


