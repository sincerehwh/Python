# 描述器

class Describer:
	def __init__(self,fget = None,fset = None,fdel = None):
		print("__init__",fget)
		self.fget = fget
		self.fset = fset
		self.fdel = fdel

	def __get__(slef,instance,cls):
		if self.fget:
			self.fget(instance)

	def __set__(self,instance,value):
		if self.fset:
			self.fset(instance,value)

	def __del__(self,instance):
		if self.fdel:
			self.fdel(instance)

	def getter(self,fn):
		self.fget = fn 

	def setter(self,fn):
		print("setter")
		self.fset = fn

	def deler(self,fn):
		self.fdel = fn


class Person:
	@Describer
	def score(self):
		return self._score

	@score.setter
	def set_score(self,value):
		self._score = value

st = Person()












