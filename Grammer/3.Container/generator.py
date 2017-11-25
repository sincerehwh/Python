
''' 生成器
	
	- 节省内存

	- 通过推倒获取对应的值

	- 用到了再计算

''' 

# 生成

squares = []

for i in range(1000):
	squares.append(i * i)
for i in range(10):
	print(squares[i])
print(squares)


squares_generator = (x*x for x in range(200))
for i in range(100):
	print(next(squares_generator))

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n += 1
	return 'Finished'

f = fib(100)
import traceback
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
try:
	print(next(f))
except StopIteration:
	print("Interation stoped!")

for i in fib(100):
	print(i)


# 遍历