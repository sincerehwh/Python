import numpy as np
from pandas import Series,DataFrame


# 字典生成DataFrame,key为列的名字
dframe = {'names':['zhao','qian','sun','li','zhou','wu','zheng'],
		'years':[2011,2012,2013,2014,2015,2016,2017],
		'ages':[20,21,22,23,24,25,26]}

print("\nDataFrame(dframe): ")
print(DataFrame(dframe))

print("\nDataFrame(dframe) order as years-ages-names : ")
print(DataFrame(dframe,columns=["years","ages","names"])) # 指定列顺序

# 指定索引，在列中指定不存在的列，默认数据为NaN
dframe2 = DataFrame(dframe,columns=["years","ages","names"],index=['a','b','c','a','b','c','d'])

print("\nDataFrame(dframe) order widthIndex : ")
print(dframe2)
print(dframe2["years"])
print(dframe2.years)

dframe2.ages = 27 # 批量修改值
print(dframe2)

dframe2["addLine"] = (dframe2.years == 2016) # 赋值给新的列
print("\n",dframe2)
print("\n",dframe2.columns)

# DataFrame的转置
print("dframe2.T: ",dframe2.T)

# 指定索引顺序，使用切片初始化数据
#pdata = {"newYears",dframe2["years"][:1]}
#print(DataFrame(pdata))

# 指定索引和列的名称
dframe2.index.name = 'ppp'
dframe2.columns.name = 'columns'
print(dframe2)
print(dframe2.values)







