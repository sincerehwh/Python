
# 抽象是程序能够被人理解的关键所在

def show_detail(lis):
	'show the detail of list'
	lis[0] = "0000"
	for i in lis:
		print(i)

print(show_detail.__doc__)

help(show_detail)


lis = ["1","2","3","4"]
show_detail(lis)

print(lis)


# 关键字参数
def person_msg(name,where,age=20):
	print("{}的{}来自{}".format(age,name,where))

person_msg("louis", "China")

# 可变参数
def all_numbers(*numbers,min):
	print(numbers)
def all_kvs_0(min_,**kvs):
	print(min_,kvs)
def all_kvs_1(kvs):
	print(kvs)


all_numbers(1,2,3,4,5,min=10)
dic =  {"num0":123,"num1":1234}
all_kvs_0(min_=10,a=10,b="11")
all_kvs_0(min_=10,**dic)
print(dic)
all_kvs_1(dic)

# 函数嵌套

# 递归
def reduce(x):
	y = x - 1
	print(x)
	if y == 0:
		return 0
	else:
		return reduce(y)


def factorial(x):
	print(x)
	if x == 1:
		return 1
	else:
		return factorial(x-1)*x

print(factorial(10))


########## 函数式编程 ##########
########## 函数式编程 ##########
########## 函数式编程 ##########

_list = [1,2,3,4,5,6,7,8,9,10]

# map:func list -> 不循环
def map_func(x):
	return x**x
map_func_list = list(map(map_func,_list))
print(map_func_list)

# filter 
def filter_func(x):
	return x % 2 == 0
filter_func_list = list(filter(filter_func,_list))
print(filter_func_list)

from functools import reduce
# reduce 
def reduce_func(x,y):
	print(x)
	return x*y
reduce_func_list = reduce(reduce_func,_list)
print(reduce_func_list)

# lambda函数
a = lambda a,b,c:a+b+c/3
print(a(1,2,3))


# apply
#result = apply(lambda x,y:print(y,x),(1,2))
#print(result)










