
''' 高阶函数 '''

# 函数作为参数
def fff(a,b,f):
	return f(a)+f(b)

def f(x):
	return x**3

print(fff(2,3,f))


''' 常用高阶函数 '''
from functools import reduce

def odd(x):
	return x%2!=0

odd_lambda = lambda x:x%2!=0

def a_b_c_add(x,y,z):
	return x+y+z

a_b_c_add_lambda = lambda x,y,z:x+y+z

def sss(x,y):
	return x**y

sss_lambda = lambda x,y:x**y


# filter / map / reduce 是函数的不同参数带入方式

hundred = list(range(0,100))

hundred_odd = list(filter(odd,hundred)) # filter 将满足条件的数组成一个数组，过滤
print("hundred_odd: ",hundred_odd)

hundred_map = list(map(a_b_c_add,hundred,hundred,range(0,9))) # map将数组带入到前面的函数式，支持多个参数
print("hundred_map: ",hundred_map)

hundred_reduce = reduce(sss,range(1,10)) # reduce 按照顺序执行，计算总的结果
print("hundred_reduce",hundred_reduce)

''' 匿名函数 '''

# lambda -> 仅仅是做一个函数，换一种形式

li = [1,2,3,4,5,6,7,8,9,10]


reduce_list = reduce(lambda x,y:x*y,li)	# 
print(reduce_list)

map_list = list(map(lambda x,y:x*y,li,li)) #
print(map_list)

filter_list = list(filter(lambda x:x<6,li)) #
print(filter_list)

''' 装饰器 '''
# 对函数的包装
# 插入日志、性能测试、事务处理、缓存、权限校验等场景
# 装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用

def aDecorator(object):

	def __init__(self,fn):
		print("aDecorator : __init__")
		self.fn = fn

	def __call__(self):
		self.fn()
		print("adecorator : __call__")

@aDecorator
def func_new():
	print("Init a new function")

print("finsh aDecorator")

from functools import wraps

def h(fn):
	@wraps(fn)
	def wrapper():
		fn()
	return wrapper


''' 偏函数 '''

import functools
# 传入一部分参数

int36 = functools.partial(int,base=36)
print(int36("10"))

print(int('1000',base=10))


