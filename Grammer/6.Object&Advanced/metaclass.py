

# 使用 type 函数动态创建类

def init(self,name):
	self.name = name


def say(self):
	print(self.name+" say " + somthing)

# (,) tuple只有一个元素时需要加
Hello = type("Hello",(object,),dict(__init__ = init,hello = say)) 

# print(Hello("111").say())
# __new__

