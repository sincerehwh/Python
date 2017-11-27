
# -*- codeing: utf-8 -*-

from pandas import Series


# 用数组生成Series

sers = Series([1,2,3,4,5,6,-1,-2.-3,-4,-5,-6])

print("sers: ",sers)

print("sers.values: ",sers.values)

print("sers.index: ",sers.index)


# 指定Series的Index

sers2 = Series([1,2,3,4,5],index=['a','b','c','d','e'])

print("sers2: ",sers2)

print("sers2.values: ",sers2.values)

print("sers2.index: ",sers2.index)

print("sers2[['a','b','c']: ",sers2[["a","b","c"]]) # 通过索引访问

print("sers2[[0,1,2,3]]: ",sers2[[0,1,2,3]]) # 通过下标访问

print("sers2[sers2 < 4]: ",sers2[sers2 < 4]) # 找出满足条件的元素

print("a" in sers2) # 判断索引是否存在


# 使用字典生成Series

dic = {"Tom":23,"Louis":26,"Kim":32}

index = ["Tom",'Louis','Kim'] # 指定的索引，不匹配的为NaN

sers3 = Series(dic,index=index)

print("sers3.index: ",sers3.index)
print("sers3.values: ",sers3.values)


# series 相加，相同索引部分相加
print(sers+sers2+sers3)


# 指定Series及其索引的名字
sers2.name = "po"
sers2.index.name = "Kim"

print(sers2)

# 替换Index

sers3.index = ["aaaa","baaaaa","caaaa"]
print(sers3)


