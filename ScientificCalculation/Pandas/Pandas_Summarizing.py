'''
	常用方法选项：

		axis：指定轴，DataFrame的行用0，列用1。

		skipna：排除缺失值，默认值为True。

		level：如果轴是层次化索引的(即MultiIndex)，则根据level选取分组。

	常用描述和汇总统计函数：

		count：非NA值的数量

		describe：针对Series或各DataFrame列计算汇总统计

		min, max：计算最小值和最大值

		argmin, argmax：计算能够获取到最小值和最大值的索引位置(整数)

		idxmin, idxmax：计算能够获取到最小值和最大值的索引值

		sum：值的总和
		
		mean：值的平均数

		median：值的算术中位数

		mad：根据平均值计算平均绝对离差

		var：样本值的方差

		std：样本值的标准差

		skew：样本值的偏度(三阶矩)

		kurt：样本值的偏度(四阶矩)

		cumsum：样本值的累计和
		
		cummin, cummax：样本值的累计最大值和累计最小值

		cumprod：样本值的累计积

		diff：计算一阶差分

		pct_change：计算百分数变化

'''

import numpy as np
from pandas import DataFrame,Series,MultiIndex,Index,Panel
import pandas as pd
import pandas_datareader.data as web 
import sys
# import pandas.io.data as web

# 根据指定的Key计算统计信息
frame = DataFrame(np.arange(12).reshape((4,3)),index=[['a','b','c','d'],[1,2,3,4]],columns=[['a','b','c'],['A','B','C']])
print(frame)


frame.index.names = ['key1','key2']
print(frame)
print(frame.sum(level=['key1']))
print(frame.sum(level=['key2']))



''' 
		• 数值型和非数值型的区别

		• NA值被自动排查，除非通过skipna选项
'''

# Series的层次索引
data = Series(np.random.randn(10),index=[list('aaabbbcccd'),[1,2,3,4,5,1,2,3,4,5]])
print("\ndata:---- ",data)
print("\ndata.index:---- ",data.index)
print("\ndata.b:---- ",data.b)
print(data['b':'c'])
print(data[:2])
print(data.unstack())
print(data.unstack().stack())

# DataFrame的层次索引
frame = DataFrame(np.random.randn(12).reshape((4,3)),index=[list('abcd'),[1,2,3,4]],columns=[['col1','col2','col3'],["col11","col22","col33"]])
print(frame)

frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
print(frame)

print(frame.ix['a',1])
print(frame.ix['a',2])
print(frame.ix['a',1]['col1']['col11'])

# 直接用MultiIndex创建层次索引结构
print(MultiIndex.from_arrays([['S','M','L'],['XL','XXL','XXXL']],names=['name1','name2']))


'''
相关系数与协方差
• 相关系数:相关系数是用以反映变量之间相关关系密切程度的统计指标

• 协方差:从直观上来看，协方差表示的是两个变量总体误差的期望。如果两个 变量的变化趋势一致，也就是说如果其中一个大于自身的期望值时另外一个也 大于自身的期望值，那么两个变量之间的协方差就是正值;如果两个变量的变 化趋势相反，即其中一个变量大于自身的期望值时另外一个却小于自身的期望 值，那么两个变量之间的协方差就是负值。

'''

# all_data = {}
# for ticker in ['APL','IBM','MSFT','GOOG']:
# 	all_data[ticker] = web.get_data_yahoo(ticker,'11/25/2017','11/25/2017')
# 	price = DataFrame({tic:data['Adj Close'] for tic,data in all_data.iteritems()})
# 	volume = DataFrame({tic:data['Volume'] for tic,data in all_data.iteritems() })
# returns = price.pct_change()
# print(returns.tail())
# print(returns.MSFT.corr(returns.IBM))
# print(returns.corr())
# print(returns.corrwith(returns.IBM))
# print(returns.corrwith(returns.volume))


'''

• 常用方法

	is_in 计算一个表示“Series各值是否包含于传入的值序列中”的布尔型数组

	unique 计算Series中的唯一值数组，按发现的顺序返回。

	value_counts 返回一个Series，其索引为唯一值，其值为频率，按计数值降序排列。

'''

# 去重
ser = Series(list('jkhgfgrfcghbljgchfdzgsdxjgvjlhbljhvjgfxdfzrf'))
print(ser.unique())
print(ser.value_counts())

# 判断元素存在
mask = ser.isin(['b','c','h'])
print(mask)
print(ser[mask]) # 打印b、c元素

data = DataFrame({'Qu1':[1,2,4,5],'Qu2':[2,3,4,5],'Qu3':[1,2,3,3]})
print(data)
print(data.apply(pd.value_counts).fillna(0))
print(data.apply(pd.value_counts,axis = 1).fillna(0))


'''
	处理缺失数据 • NA处理方法

		dropna 根据各标签的值中是否存在缺少数据对轴

		fillba	样本值的标准差

		isnull 样本值的偏度(三阶矩)

		notnull
	
			• NaN(Not a Number)表示浮点数和非浮点数组中的缺失数据 
	
			• None也被当作NA处理

'''

df = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.5]],index=['a','b','c','d'],columns=['one','two'])

print(df)
print(df.sum()) # 按列求和
print(df.sum(axis=1)) # 按行求和

print(df.mean(axis=1,skipna=False))
print(df.mean(axis=1))

print(df.idxmax())
print(df.cumsum())
ser = Series(['a','b','c','d']*4)
print(ser.describe())

print(df.isnull())
df[0] = None
print(df)
print(df.isnull())


'''
	处理缺失数据 滤除缺失数据
		• dropna
		• 布尔索引
		• DatFrame默认丢弃任何含有缺失值的行
		• how参数控制行为，axis参数选择轴，thresh参数控制留下的数量
'''

from numpy import nan as NA

# 丢弃NA
data = Series([1,NA,3,NA,7])
print(data.dropna())
print(data[data.notnull()])

# 对DataFrame丢弃NA
data = DataFrame([[1,2,3],[4,5,6],[NA,NA,NA],[NA,6,3]])
print(data.dropna()) #默认只要某行有NA就全部都删除
print(data.dropna(how='all')) # 全部为NA才删除

data[4] = NA # 新增一列
print(data.dropna(axis=1,how='all'))
data = DataFrame(np.random.randn(7,3))
data.ix[:4,1] = NA
data.ix[:2,2] = NA
print(data)
print(data.dropna(thresh=2)) # 每行至少要有2个非NA元素



'''
	处理缺失数据 填充缺失数据
		• fillna
		• inplace参数控制返回新对象还是就地修改
'''

df = DataFrame(np.random.randn(7,3))
df.ix[:4,1] = NA
df.ix[:2,2] = NA
print(df.fillna(0))
df.fillna(0,inplace=True)
print(df)

# 不同行列填充不同的值
print(df.fillna({1:0.5,3:-1})) # 第三列不存在

# 不同的填充方式
df = DataFrame(np.random.randn(6,3))
df.ix[2:,1] = NA
df.ix[4:,2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill',limit = 2))

# 用统计数据填充
data = Series([1.,NA,3.5,NA,7])
print(data.fillna(data.mean()))


'''

层次化索引
	使你能在一个轴上拥有多个(两个以上)索引级别。
	抽象的说，它使你能以低 纬度形式处理高维度数据。
	• 通过stack与unstack变换DataFrame

层次化索引 重新分级顺序
	• 索引交换
	• 索引重新排序


'''



print('索引层级交换')
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
frame_swapped = frame.swaplevel('key1', 'key2')
print(frame_swapped)
print(frame_swapped.swaplevel(0, 1))

print('根据索引排序')
print(frame.sortlevel('key2'))
print(frame.swaplevel(0, 1).sortlevel(0))



'''

	层次化索引 根据级别汇总统计
	• 指定索引级别和轴


	层次化索引 使用DataFrame的列
	• 将指定列变为索引
	• 移除或保留对象
	• reset_index恢复

 	整数索引
	• 歧义的产生
	• 可靠的，不考虑索引类型的，基于位置的索引。
'''

print('使用列生成层次索引')
frame = DataFrame({'a':range(7),
                   'b':range(7, 0, -1),
                   'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd':[0, 1, 2, 0, 1, 2, 3]})
print(frame)
print(frame.set_index(['c', 'd']))  # 把c/d列变成索引
print(frame.set_index(['c', 'd'], drop = False)) # 列依然保留
frame2 = frame.set_index(['c', 'd'])
print(frame2.reset_index())


print('整数索引')
ser = Series(np.arange(3.))
print(ser)

try:
    print(ser[-1]) # 这里会有歧义
except Exception as e:
	print(e)

# ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
# print(ser2[-1])
# ser3 = Series(range(3), index = [-5, 1, 3])
# print(ser3.iloc[2])  # 避免直接用[2]产生的歧义

# print('对DataFrame使用整数索引')
# frame = DataFrame(np.arange(6).reshape((3, 2)), index = [2, 0, 1])
# print(frame)
# print(frame.iloc[0])
# print(frame.iloc[:, 1])


'''
	其它话题 面板(Pannel)数据
	• 通过三维ndarray创建pannel对象
	• 通过ix[...]选取需要的数据
	• 访问顺序:item -> major -> minor
	• 通过stack展现面板数据

'''

# px=web.DataReader('F-F_Research_Data_factors','famafrench')  

# Yahoo的数据源已经失效
pdata = Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2016', '1/15/2016')) for stk in ['AAPL', 'GOOG', 'BIDU', 'MSFT']))
print(pdata)
pdata = pdata.swapaxes('items', 'minor')
print(pdata)

print("访问顺序：# Item -> Major -> Minor")
print(pdata['Adj Close'])
print(pdata[:, '1/5/2016', :])
print(pdata['Adj Close', '1/6/2016', :])


print('Panel与DataFrame相互转换')
stacked = pdata.ix[:, '1/7/2016':, :].to_frame()
print(stacked)
print(stacked.to_panel())

