
############ 导入模块 ############
############ 导入模块 ############
############ 导入模块 ############

# import math

# import math as pp

# from math import lgamma

# from sys import argv as sys_argv

# from json import *


############ 赋值 ############
############ 赋值 ############
############ 赋值 ############

a,b,c = 1,2,3
print(a,b,c)

x = 1,2,3,4,5,6,7,8
print(x)

x,*y,z = 1,2,3
print(x,y,z)

x = y = z = 10
print(x,y,z)

x += 10000
print(x)
x -= 1000 
print(x)
x *= 100
print(x)

y = ""
y += "name"
print(x)
y *= 3
print(x)

############ 条件 ############
############ 条件 ############
############ 条件 ############

print("i".isupper() == 0)

status = "Hello" if "H".isupper() else "World"
print(status)


########### 比较运算符
x = y = 0
x == y
x > y 

print(x == y) # 相等运算
print(x is y) # 相同运算
print(x in [1,2]) # 成员资格

a = "AA".islower() # 字符串比较
b = "BB".islower()
print( a > b )


############ 循环 ############
############ 循环 ############
############ 循环 ############

while 0==True:
	pass

for i in [1,2,3]:
	print(i)

# 迭代字典
d = {"A":"a","B":"b"}
for key in d:
	print(key)

for key,value in d.items():
	print(key,value)

# 并行迭代
a = ["Z","W","L","Z"]
b = ["1","2","3","4"]
cc = list(zip(a,b))
print(cc)

for i in zip(a,b): # 最短的序列为准
	print(i)

st_ = "This is a long string"
for i in enumerate(st_):
	print(i)

# 反向迭代+排序后迭代
print(sorted(st_))

for i in reversed(st_):
	print(i)
rev_ = list(reversed(st_))
print(rev_)
print("".join(rev_))

# 结束循环
i = 0
while  i < 10:
	i += 1
	if i == 5:
		print("5>>>le")
		continue
		i -= 1
	if i == 9:
		break
	print("index:{}".format(i))
else:
	print("")

for i in range(10):
	if i == 5:
		break
else:
	print("break le")

# 简单推导

x = [x * x for x in range(10)]
print(x)

x = [x**2 for x in range(10) if x != 5 ]
print(x)

y = [(x,y,z) for x in range(5) for y in range(5,10) for z in range(10,15)] # 从后向前迭代
print(y)

sq = {i:"{}".format(i,i**2) for i in range(10)}
print(sq)

# pass del exec

pass 

#del 删除的是指针，最终内存还是垃圾回收机制处理

# 命名空间 -> 添加值
spac = {}
spac["x"] = 2
spac["y"] = 3
exec("print('2x3',x*y)",spac)

eval("print('2x3',x*y)",spac)

print(ord("*"))













