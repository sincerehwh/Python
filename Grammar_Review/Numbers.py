

# 数字

# 运算

# 转化

# 函数：


''' 数学函数：
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y) 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 
  Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根。
'''

import math

# abs(x)
number = abs(-1000)
print(number)

# ceil(x) ->  上舍整数
number = math.ceil(3.3)
print(number)

# floor(x) -> 下舍整数
number = math.floor(8.8)
print(number)

# (x>y)-(x<y)
o_0 = (1>0)-(1<0)
print(o_0)

# exp(x)
number = math.exp(10)
print(number)

# fabs(x)
number = math.fabs(-100)
print(number)

# log(x)
# log10(x)
number = math.log(1000,10)
print(number)

# max(x1, x2,...) min(x1, x2,...)
max_ = max([1,2,3])
print(max_)
max_ = max(1,2,3,4,5,6)
print(max_)

# modf(x)
print(math.modf(100.001)) # 前面位小数部分，后面为整数部分

# pow(x, y) x**y
print(pow(2,8)) 

# round(x [,n]) x的四舍五入值,给出n值，则代表舍入到小数点后的位数
print(round(1005.551))
print(round(1005.451))
print(round(1005.5535,2))
print(round(1005.5555,3))

# sqrt(x)
print(math.sqrt(0.1))


'''
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。	
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''


'''
数学常量
常量	描述
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
'''
print(math.pi)
print(math.e)



