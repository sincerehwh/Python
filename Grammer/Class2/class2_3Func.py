
''' 函数 '''

def function_name(arg_1,arg_2,arg_3):
	print(arg_1,arg_2,arg_3)
	return  arg_1,arg_2,arg_3

l = function_name(1,2,3)
print(l)
print(type(l))

# 参数带初始值
def add(num1=0,num2=0):
	return num1+num2

print(add()) #
print(add(num2=100,num1=11111)) # 参数可调换位置

# 可变参数 
def func_arr(name,*number):
	print(number)
	print(type(number))
	print(number[100])

def func_dic(name,**keyValue): # 带参数名的函数
	print(name)
	print(keyValue)
	print(type(keyValue))
func_dic('k',Guangdong='GuangZhou',GuangXi="NanNing")

def func_dict_s(name,*,animal,weight): # *号后面的参数，必须带上参数名
	print(name)
	print(animal)
	print(weight)

func_dict_s("Hello",animal="I am animal",weight=100)

def func_all(a,b=0,*arr,**dic):
	print(a)
	print(b)
	print(arr)
	print(dic)

func_all(1,"1","q",Name="name",gender="male")
func_all(1,*("1","q"),**{"Name":"name","gender":1000})


# 递归函数
def self_sum(i):
	if i < 0:
		raise ValueError
	elif i<=1:
		return i
	else:
		return i + self_sum(i - 1)

print(self_sum(995))

# 函数作为参数

p = print
p(1,2,3)





