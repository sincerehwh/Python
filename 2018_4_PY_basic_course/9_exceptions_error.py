
# raise Exception


class NewException(Exception):
	pass


try:
	raise Exception	
except Exception as e:
	print(e.__doc__)
finally:
	print("Finished")


try:
	pass
except (ZeroDivisionError,TypeError) :
	print("error")

try:
	pass
except (ZeroDivisionError,TypeError) as e:
	print("error")
finally:
	pass

# while True:
# 	try:
# 		x = int(input("分子："))
# 		y = int(input("分母："))
# 		print(x/y)
# 	except Exception as e:
# 		raise
# 	else:
# 		break

# warning

from warnings import warn

warn("warnings")
warn("warnings",DeprecationWarning)