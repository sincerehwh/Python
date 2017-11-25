
import traceback #追溯


try:
	x = 1/0
except Exception as e:
	print(e)
else:
	print("nothing serious")
	x = 0
finally:
	print("I am always running")
