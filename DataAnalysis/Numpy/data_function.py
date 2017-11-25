'''

# 一元函数

abs, fabs 计算整数、浮点数或复数的绝对值。对于非复数值，可以使用更快的fabs。

sqrt 计算各元素的平方根。相当于arr ** 0.5

sqare 计算各元素的平方。相当于arr ** 2

exp 计算各元素的e^x

log, log10, log2, log1p 分别为自然对数、底数为10的log、底数为2的log和log(1 + x)。

sign 计算各元素的正负号:1(正数)、0(零)、-1(负数)。

ceil 计算各元素的ceiling值，即大于等于该值的最小整数。

floor 计算各元素的floor值，即小于等于该值的最小整数。


# 二元函数

rint 将各元素值四舍五入到最接近的整数，保留dtype。

modf 将数组的小数部分与整数部分以两个独立数组的形式返还。

isnan 返回一个表示“哪些值是NaN(这不是一个数字)”的布尔型数组

isfinite, isinf 分别返回一个表示“哪些元素是有限的(非inf，非NaN)”或“哪些元素是 无穷的”的布尔型数组

cos, cosh, sin, sinh, tan, tanh 普通型或双曲型三角函数

arccos, arccosh, arcsin, arcsinh, arctan, arctanh 反三角函数

copysign 将第二个数组中的符号复制给第一个数组中的值

greater, greater_equal, less, less_equal,equal, not_equal 执行元素级的比较，最终产生布尔型数组。

logical_and, logical_or, logical_xor执行元素级的真值逻辑运算，最终产生布尔型数组。

logical_not 计算各元素not x的真值。相当于-arr。

'''

import matplotlib.pyplot as plt
import numpy as np
import pylab

points = np.arange(-5,5,0.01)
print(points)

xs,ys = np.meshgrid(points,points) #xs,ys互为转置矩阵
print(xs)
print(ys)

z = np.sqrt(xs ** 2,ys ** 2 )
print(z)

plt.imshow(z,cmap = plt.cm.gray)
plt.colorbar()
plt.title("HHH")
pylab.show()













