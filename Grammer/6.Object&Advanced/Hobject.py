
import traceback

class Person:
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("Score must be int")

		elif (value<0) or (value>100):
			raise ValueError("Score must in range(0,101)")
		self._score = value

	@property 
	def double_score(self):
		return self._score * 2

p = Person()
p.score = 76
print(p.score)

try:
	p.score = "sdfd"
except Exception as e:
	print(e)

