
''' 迭代器
	
	- 直接作用于For循环

	- 可以被next调用，返回下一个值，Inter惰性计算序列

	- 

'''

from collections import Iterable
from collections import Iterator

# isinstance 判断继承关系

# 判断是不是可迭代
# print(isinstance([1,2,3,4,5,6],Iterable))
# print(isinstance({"1":"2","2":"2"},Iterable)
# print(isinstance('1234567788',Iterable))

# 判断是不是迭代器
# print(isinstance([1,2,3,4,5,6],Iterator))
# print(isinstance({1:"2",2:"2"}),Iterator)
# print(isinstance("1234567788",Iterator))


def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n += 1
	return 'Finished'

fun = fib(10)

print(isinstance(fun,Iterator))
print(isinstance(fun,Iterable))
