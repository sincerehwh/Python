
''' 只读列表 

'''

tup = (1,2,3,4,5,6,7)

print(type(tup))


try:
	tup[0] = 1000
except Exception as e:
	print(e)
