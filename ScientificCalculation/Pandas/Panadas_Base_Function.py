import numpy as np
import pandas as pd
import sys
from pandas import Series,DataFrame,Index

'''
'''

# 重新指定索引及顺序
ser = Series([4.5,7.2,-6.0],index=['a','b','c'])
print(ser)

ser2 = ser.reindex(["a","c","b"])
print(ser2)

ser3 = ser.reindex(["PP","OO","II"],fill_value=0) # 指定不存在元素的默认值
print(ser3)

# 重新指定索引并指定元素填充方法
ser4 = Series([1,2,3],index=["1",'2','3'])
print(ser4)
# print(ser4.reindex(range(6),"ffill"))

# 对DataFrame 重新指定索引
frame = DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['name1','name2','name3'])
print(frame)

# 重新指定colume
states = ['Texas','Utah','California']
print(frame.reindex(columns=states))

# 对Dataframe重新指定索引，并指定元素填充方法
print(frame.reindex(index=['X','X','X'],method='ffill',columns=states))
print(frame.ix[['X','X','X'],states])



'''
	丢弃指定轴上的项：

		• 丢弃某条轴上的一个或多个项很简单，只要有一个索引数组或列表即可。由于 需要执行一些数据整理和集合逻辑，所以drop方法返回的是一个在指定轴上删 除了指定值的新对象
'''

se = Series(np.arange(5.),index=['a','b','c','d','e'])
print(se)
new_se = se.drop("e")
print(new_se)

data = DataFrame(np.arange(20).reshape((4,5)),index=['a','aa','aaa','aaaa'],columns=['111','222','333','444','555'])
print(data)

data_drop1=  data.drop(['a','aa'])
print(data_drop1)

data_drop2 = data.drop(['111'],axis=1)
print(data_drop2)


'''	

索引、选取和过滤：

		• Series索引(obj[...])的工作方式类似于NumPy数组的索引，只不过Series的 索引值不只是整数。

		• 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的 (inclusive)。

		• 对DataFrame进行索引其实就是获取一个或多个列

		• 为了在DataFrame的行上进行标签索引，引入了专门的索引字段ix。

		• DataFrame的索引选项：

			obj[val]：选取DataFrame的单个列或一组列。在一些特殊情况下会比较便利:布尔型数组(过滤 行)、切片(行切片)、布尔型DataFrame(根据条件设置值)。

			obj.ix[val]：选取DataFrame的单个行或一组行
			
			obj.ix[:, val]：选取单个列或列子集

			obj.ix[val1, val]：同时选取行或列
			
			reindex方法：将一个或多个轴匹配到新索引

			xs方法：根据标签选取单行或单列，并返回一个Series。

			icol、irow方法：根据整数位置选取单行或单列，并返回一个Series。

			get_value、set_value方法：根据行标签或列标签选取单个值

'''

#  索引获取
n = Series(np.arange(4.),index=['z','y','x','w'])
print('\n',n['z'],n['y'],n['x'],n['w'])

# 数组切片
print(n['z':'w']) # 闭区间

# DataFrame的索引
dataFrame = DataFrame(np.arange(16).reshape((4,4)),index=['qqq','www','eee','rrr'],columns=['1','3','4','x'])
print(dataFrame)
print(dataFrame['1']) # 打印列
print(dataFrame[['1','4']]) # 打印列 
print(dataFrame[:3])
print(dataFrame.ix['qqq',['1']]) # 指定索引和序列
print(dataFrame.ix['qqq',[1,2]]) 
print(dataFrame.ix[3]) # 从0打印到第三行
print(dataFrame.ix[:"www",'1']) # 从开始到‘www’行的‘1’列,


# 根据条件选择

print(dataFrame[dataFrame.x > 2])
print(dataFrame < 5)

dataFrame[dataFrame < 3 ] = 0 
print(dataFrame)



'''
	
		算术运算和数据对齐：

		• 对不同的索引对象进行算术运算

		• 自动数据对齐在不重叠的索引处引入了NA值，缺失值会在算术运算过程中传播。 

		• 对于DataFrame，对齐操作会同时发生在行和列上。

		• fill_value参数

		• DataFrame和Series之间的运算

'''

# 加法

s1 = Series([1.1,2.2,3.3,4.4,5.5,6.6],index=['z','s','c','g','y','u'])
s2 = Series([100,200,300,400,500,600],index=['z','x','c','v','b','n'])
print(s1)
print(s2)
print(s1+s2)


# 做加法时，索引和列都必须相同才能匹配
d1 = DataFrame(np.arange(16).reshape(4,4),index=['i1','i2','i3','i4'],columns=['c1','c2','c3','c4'])
d2 = DataFrame(np.arange(16,32).reshape(4,4),index=['i1','i2','i3','i4'],columns=['c1','c2','c3','c4'])

print('\n',d1)
print('\n',d2)
print('\n',d1+d2)

# 数据填充 -> 合并 。。。
df1 = DataFrame(np.arange(100.).reshape((10,10)),columns=list('abcdefghij'))
df2 = DataFrame(np.arange(100.,200.0).reshape((10,10)),columns=list('poiuytrewq'))
print('\n',df1)
print('\n',df2)
print('\n',df1+df2)
print(df1.add(df2,fill_value=100000))
print(df1.reindex(columns=df2.columns,fill_value=0))

# DataFrame 与 Series之间的操作
array = np.arange(12.0).reshape((3,4))
print("\n",array)
print('\n',array[0])
print('\n',array-array[0])

frame = DataFrame(np.arange(12.).reshape((4,3)),columns=list('abd'),index=list("ABCD"))
print("\n frame: ")
print(frame)
ser = frame.ix[0]
print(ser)
print(frame-ser)

ser2 = Series(range(3),index=list('bef'))
print(frame+ser2)
ser3 = frame['d']
print(frame.sub(ser3,axis=0)) # 按列减

'''

	函数应用和映射：

		• numpy的ufuncs(元素级数组方法)

		• DataFrame的apply方法

		• 对象的applymap方法(因为Series有一个应用于元素级的map方法)

'''

df = DataFrame(np.random.randn(4,3),columns=list('akk'),index=list('KKKK'))
print(df)
print(np.abs(df))

f = lambda x:x.max()-x.min()
print(df.apply(f))
print(df.apply(f,axis=1))

def f(x):
	return Series([x.min(),x.max()],index = ['min','max'])
print(df.apply(f))


# apply map 

_format = lambda x:'%.2f' % x
print(df.applymap(_format))

print(df['a'].map(_format))



'''

	 排序和排名：

	 	• 对行或列索引进行排序

		• 对于DataFrame，根据任意一个轴上的索引进行排序

		• 可以指定升序降序

		• 按值排序

		• 对于DataFrame，可以指定按值排序的列

		• rank函数
'''

# 根据索引排序，对DataFrame指定轴
ser = Series(range(4),index = list("abcd"))
print(ser.sort_index())
frame = DataFrame(np.arange(8).reshape((4,2)),index=['list1','list2','list3','list4'],columns=list('ab'))
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1,ascending=False)) # 降序排列


# 根据值排序
serser = Series([4,7,-3,-2])
print(serser.sort_values) 

# 对DataFrame指定列排序
frame = DataFrame({'a':[1,2,3],'b':[4,5,6]})
print(frame)
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a','b']))


# rank,求排名的平均位置（从1开始）
s = Series([1,2,3,4,5,6,7,8,9])
print(s.rank())
print(s.rank(method='first')) #  去第一次出现，不求平均值
print(s.rank(ascending=False,method='max')) # 逆序，并取最大值
frame = DataFrame({'b':[1,2,3,4,5],'c':[1,2,3,4,5],'d':[1,2,3,4,5],'c':[0,9,8,7,0]})
print(frame)
print(frame.rank(axis=1))



'''

	带有重复值的索引：

		• 对于重复索引，返回Series，对应单个值的索引则返回标量

'''

# print('重复的索引')
# obj = Series(range(5), index = ['a', 'a', 'b', 'b', 'c'])
# print(obj.index.is_unique) # 判断是非有重复索引
# print(obj['a'])               


# df = DataFrame(np.random.randn(4, 3), index = ['a', 'a', 'b', 'b'])
# print(df)
# print(df.ix['b'].ix[0])
# print(df.ix['b'].ix[1])

