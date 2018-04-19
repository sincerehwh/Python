
def builder(array):
	for l in array:
		for li in array:
			yield li


# print(list(builder([[1,2,3],[4,5,6]])))


def flattern(nested):
	result = []
	try:
		try: nested + ""
		except TypeError:pass
		else: raise TypeError
		for sub in nested:
			for el in flattern(sub):
				result.append(el)
	except TypeError:
		result.append(nested)
	return result


def conflict(state,nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i] - nextY) in (0,nextY-i):
			return True
	return False

def queens(num=8,state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num-1:
				yield(pos,)
			else:
				for result in queens(num,state + (pos,)):

print(list(queens(8)))
