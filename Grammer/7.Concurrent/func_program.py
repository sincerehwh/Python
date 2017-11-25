
''' 
	三大特征
	1. 不可变数据
	2.函数作为变量使用
	3.尾递归优化：每次递归都重用stack

	优势：
	1.并行
	2.惰性求值
	3.确定性

	技术：
	1.map & reduce
	2.pipeline
	3.recursing
	4.currying
	5.higher order function 

	描述要干什么

'''


# get everage value of a serial numbers

number = [1,2,3,4,5,6,7,8,9,11,222,123,1,34,1,35,234534,5,34,5,324,5,24,5,2345,34]

number_count = 0
number_sum = 0
for i in number:
	number_sum = number_sum + i 
	number_count += 1
if number_count==0:
 	number_count = 1
number_everage = number_sum/number_count
print(number_everage)

from functools import reduce

number_average = (reduce(lambda x,y:x+y,number)/len(number))

print(number_average)


