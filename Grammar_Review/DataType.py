# -*- utf-8 -*- 



# Python keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# data type:
	# Number（数字）
	# String（字符串）
	# List（列表）
	# Tuple（元组）
	# Sets（集合）
	# Dictionary（字典）


# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# isinstance 认为子类是一种父类类型
# type 不会认为子类是一种父类类型
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, complex))



# String（字符串）
# Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
# 字符串的截取的语法格式如下：变量[头下标:尾下标]

string = "<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>"
print(string[0:1000]) # 可以越界
print(string[0:-1]) # 负数代表从末尾起，这个是 左开右闭区间 [0,-1）
print(type(string)) # 字符串的底层应该是一个元组


# List（列表）
# 使用最频繁的数据类型。
# 列表中元素的类型可以不相同，它支持数字，字符串，列表。
list_ = [1,2,3,4,'5','6','7','8',[1,2,3,4,5]]
print("\n改变前的list：",list_)
list_[3] = ['元素可以变']
print("改变前的list：",list_)


# Tuple（元组）:
# 元素不可以修改
# 元素的类型可以不相同，它支持数字，字符串，列表。

tuple_ = (1,2,3,4,5,5,67,"NB")
print("\n改变前的元组：",tuple_)
try:
	tuple_[0] = "Python 用着比Perl爽！"
except Exception as e:
	print("出错了：",e)


# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和去重。
# 大括号 { } 或者 set() 函数创建集合，创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 集合的运算

empty_set = set()
set_a = {1,2,3,4,"0000"}
set_b = {'hello python','0000',678,88,1}
print('\nset_a:',set_a)
print('set_b:',set_b)
print("set_a | set_b：",set_a | set_b)
print("set_a - set_b：",set_a - set_b) # a-b  
print("set_b - set_a：",set_b - set_a) # b-a 这两个的结果可是不一样的
print("set_a & set_b:",set_a & set_b) 
print("set_a ^ set_b:",set_a ^ set_b) # (a|b) - (a&b)
print("(set_a|set_b)-(set_a&set_b)",(set_a|set_b)-(set_a&set_b))


# Dictionary（字典）
# 字典是无序的对象集合。
# 字典当中的元素是通过键来存取的
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型

dic = {}
dic["python"] = "很简洁的编程工具"
print(dic)


''' Python数据类型转换工具 

	

	-> Float

	-> Complex

	-> String

'''

# -> Int
x = "1000_02" #不可以有空格，不可以有特殊字符(可以有下划线)
int_x =  int(x,base=10) # base后面要转的进制
print(int_x)

# -> Float
y = 0o100 #"1000"
float_y = float(y) 
print(y)

# -> complex
real = 100
imag = 10
z = complex(real,imag)
print(z)
z = complex('100+10j')
print(z)

# -> String
class O:
	pass
object_ = [1,2,3,4] # 只要是对象就能转化？？-_-> 
print(str(O()))


# 将对象 x 转换为表达式字符串
# repr() 函数将对象转化为供解释器读取的形式。
print(repr(O()))

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
# 以下是 eval() 方法的语法:
# eval(expression[, globals[, locals]])
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
print(eval("10**3**2"))


# tuple(s)
# 将序列 s 转换为一个元组
# string、list和tuple都属于sequence（序列）。
tuple_str = tuple("# string、list和tuple都属于sequence（序列）")
print(tuple_str)

# list(s)
# 将序列 s 转换为一个列表
list_tuple = list(tuple_str)
print(list_tuple)

# set(s)
# 转换为可变集合
set_list = set(list_tuple)
print(set_list)


# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。

dic_a = dict(a='a', b='b', t='t')     # 传入关键字
print("dic_a: ",dic_a)

dic_b = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
print("dic_b: ",dic_b)

dic_c = dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
print("dic_c: ",dic_c)


# frozenset(s) s:可迭代的对象，比如列表、字典、元组等等。
# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
f_set1 = frozenset(dic_a)
print(f_set1)
f_set2 = frozenset(set_list)
print(f_set2)


# chr(x)
# 将一个整数转换为一个字符
# chr(i) 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
# i -- 可以是10进制也可以是16进制的形式的数字。
# 前 127位是Ascii码表，后面是Unicode的码表
for index in range(1000):
	string_num = chr(index) 
	print(index,":  ",string_num)

# ord(x)
# 返回对应的 ASCII 数值，或者 Unicode 数值
print(ord('🔚')) 

# hex(x)
# 将一个十进制数转换为一个十六进制字符串
he = hex(100000000)
print(he)

# oct(x)
# 将一个整数转换为一个八进制字符串
oc1 = oct(0x1888)
print(oc1)
oc2 = oct(1000000)
print(oc2)




























