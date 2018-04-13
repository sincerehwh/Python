

# 多态：对不同类型的对象执行相同的操作

# 封装：隐藏实现细节

# 集成：根据通用类创建专用类别

class A(object):
	"""docstring for A"""
	def __init__(self):
		super(A, self).__init__()

	def run(self):
		print("A is running")

class B(object):
	"""docstring for B"""
	def __init__(self):
		super(B, self).__init__()

	def run(self):
		print("B is running")

class C(object):
	def __init__(self):
		super(C,self).__init__()
	def run(self):
		print("C is running")


def create(obj):
	obj.run()
create(A())

C().run()


# 抽象基类

from abc import ABC,abstractmethod

class Base(ABC):
	@abstractmethod
	def load(set):
		pass

class APPBase(Base):

	def load():
		pass

	def a():
		pass

c = APPBase()



		
