

''' 
类型：

	整数 - 浮点数 - 字符串 - 布尔值 - 空值

	函数 - 模块 - 类型

	自定义 类型

'''
import sys

print(type(123))
print(type(123.333))
print(type("Hello Python"))
print(type(True))
print(type(None))

print(type([1,2,3]))
print(type((1,"123",True)))
print(type(set([1,2,3,'w'])))
print(type({"Key":"Value"}))

def func(a):
	print(a)

class ClassName(object):
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

print(type(func)) # 函数
print(type(sys))  # 模块
print(type(ClassName)) 	# 类
print(type(ClassName(1)))	# 对象
print(type(type))

# 变量

''' 变量存储在内存中：
		堆区：全局的，谁请求谁释放
		栈区：

	变量的类型是可变的
'''

# 变量的初始化
try
	print(y)
except NameError:
	print("NameError 'y' is no define")


# 常见字符串的处理




# 条件判断


# 循环控制




# 函数