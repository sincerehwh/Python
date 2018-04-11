
list_ = [1,2,3,'1','2','3',(1,2,3),{"1":"one","2":"two"},[1,'2']]

# 访问值
print(list_[3])

# 更新元素
list_[1] = ("PPPP",)
print(list_)

# 删除元素
list_[0] = None # 这个可不行a
del list_[1] 
print(list_)


# 列表操作
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")


# 列表截取和拼接
new = list_[0:2] + list_[0:2]
print(new)

# 列表嵌套
list_ = [list_,list_,list_]
print(list_)

# 列表函数&方法
# len(list) 列表元素个数
# max(list) 返回列表元素最大值
# min(list) 返回列表元素最小值
# list(seq) 将元组转换为列表
print(len([1,2,3,4]))
print(max(['a','b','O','Z']))
print(min(list_))
print(list(list_))


# list.append(obj) 在列表末尾添加新的对象
# list.count(obj)  统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)	从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj) 将对象插入列表
# list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse()	反向列表中元素
# list.sort([func]) 对原列表进行排序
# list.clear()	清空列表
# list.copy() 复制列表



