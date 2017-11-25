
''' 

	{key1:value,key2:value}

'''

dict1 = {1:123,2:1234,"1":1000,"2":2000,"1":12334} # 后面的key会覆盖前面相同的Key

print(type(dict1))

# 访问元素

print(dict1[1])
print(dict1["1"])


# 判断元素是否存在
print("1" in dict1)
print(2 in dict1)

# 增加||修改 元素
dict1[100] = 1000000

# 删除元素
print(dict1)
del(dict1["2"])
del(dict1["1"])
print(dict1)

# 遍历元素
for key in dict1: # 取出所有的Key
	print("Key:",key)
	print("Value:",dict1[key])

for (key, value) in dict1.items(): # 取出所有的项
	print(key,value)

# 获取所有的Key
keys = dict1.keys()
print(type(keys))
print(keys)

value = dict1.values()
print(type(value))
print(value)







