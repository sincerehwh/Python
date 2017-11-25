
'''
	列表推倒：

	-- 一维
	-- 二维

'''

arr = []
for i in range(100):
	arr.append(i)

print("arr: ",arr,"\n")

arr2 = [1] * 100
print("arr2: ",arr2,"\n")

arr3 = [i * 2 for i in range(100) ]
print("arr3: ",arr3,"\n")


arr4 = [[0] * 3] * 10 # 浅拷贝
arr4[0][0] = 122
print(arr4)


arr5 = [[0] * 3 for i in range(10)]  # 深拷贝
arr5[0][0] = 122
print(arr5)

o = {x:x % 2 == 0 for x in range(1000)}
print(o)
