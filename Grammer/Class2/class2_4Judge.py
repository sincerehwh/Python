
''' if 
	python do not have switch
'''

a = 0

if a == False:
	print('a==False')


x = None
if x is not None:
	print( "x=0"+',x is not None')

'''  for '''
for i in  range(1,10):
	print(i)

''' while '''
i = 0
while i > 100:
	i = i+100 
	print(i)

''' continue pass  '''
for i in range(1,10000):
	if i == 100:
		pass #
	elif i > 100:
		continue
	elif i > 1000:
		print(i)
	else:
		break




