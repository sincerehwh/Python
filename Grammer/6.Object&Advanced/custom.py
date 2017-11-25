
# 类的定制

# __str__ :
# __iter__ :
# __next__ :
# __getitem__

# class Manager:
# 	def __init__(self,name):
# 		self.name = name

# 	def __str__(self): #__str__ 系统自用的方法,打印类信息之前调用
# 		print("000000")
# 		return "Hello," + self.name + "!!!"

# print(Manager("122222"))



# 
# class Summer:
# 	def __init__(self,startNumber = 0,endNumber = 100):
# 		self.startNumber = startNumber
# 		self.endNumber = endNumber
# 		self.sum = 0
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):  # 允许迭代，计算处理
# 		if self.startNumber < self.endNumber:
# 			self.sum = self.sum + 1
# 			self.startNumber = self.startNumber+1
# 			return self.sum
# 		else:
# 			print("finished")
# 			quit()
# 			return self.sum
# for i in Summer():
# 	print(i)


# class Fib:
# 	def __getitem__(self,n):
# 		a,b = 1,1
# 		for i in range(n):
# 			a, b = b, a+b
# 		return a 
#
# f = Fib()
# print(f[0])

class M:
	def __calll__(self):
		print("This can be call")		

m = M()
print(callable(m))
print(callable(max))
print(callable([1,2,3]))
print(callable(True))
print(callable("str"))











