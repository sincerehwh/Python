
''' 特点：
	-- 起始值 index = 0
	-- 数据项不需要相同的类型

'''

# 创建
list1 =  [1,2,3,3,3,"4",[1,2,3],{"name":"louis"}]

# 查：内容 - 索引
print(list1[0])  # 正数索引
print(list1[-1]) # 负数索引

print(list1.index("4"))
print(list1.index(3))
try:
	print(list1.index(10000))
except Exception as e:
	print(e)

# 增
list1.append(1000) # 加单个值
list1.append([1,2,3,4,5,6]) # 将后面的元素作为一个整体
list1.extend([1,2,3,4,5,6]) # 将后面的每一个元素作为一个整体

print(list1)

# 删
print(list1)
del(list1[0:5])
print(list1)

# 改


# 判断是否为空
list2 = []
if not list2 :
	print("[] is not None")
if len(list2) == 0:
	print("list2 is empty")

# 遍历数组：
for i in [1,2,3,4,5,6]:
	print(i)

for i in range(len([1,2,3,4,5,6])):
	print([1,2,3,4,5,6][i])






 