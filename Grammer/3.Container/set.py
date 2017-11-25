'''
	- 无序

	- 不重复

'''

# 自动去重：C++内是有序的，python中是无序的
new_set = set([1,2,3,4,4,1111,4,4,5,5,6])
new_set2 =  set([11,22,33,44,45,1111,45,45,55,56,66])

print(type(new_set))
print(new_set)
print(type(new_set2))
print(new_set2)

# 判断元素是否存在
print(1 in new_set)
print("" in new_set2)

# 并集 
print(new_set | new_set2) 
print(new_set.union(new_set2))

# 交集
print(new_set & new_set2)
print(new_set.intersection(new_set2))

# 差集 A-B
print(new_set - new_set2)
print(new_set.difference(new_set2))

# 对称差 (A+B)-(A&B) 去除并集内的交集
print(new_set ^ new_set2)
print(new_set.symmetric_difference(new_set2))

# 修改元素
new_set.add("Hello") # 添加单个元素
new_set.update(['a','b','c']) # 添加整个的数组
print(new_set)

# 删除元素 必须知道值
new_set.remove("Hello")
print(new_set)

# 循环
for i in new_set:
	print(i)







