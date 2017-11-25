
'''
	正则表达式：
   	两种匹配模式：
   		1.搜索search() 
   		2.匹配match()


'''

import re


# ma = re.match(r"dog-","dog-dog- is a dog ,cat is a cat")
# # match 匹配一个 
# print(ma)

# # search 
# se = re.search(r"dog-","dog-dog- is a dog ,cat is a cat")
# print(se)

# # findall -> []
# al = re.findall(r"dog-","dog-dog- is a dog ,cat is a cat")
# print(al)


# 判断邮箱是否合法

str = "ssdf asdf sad sincere@126.com"
match = re.search(r'\w+@\+',str)
if match:
	print(match.group()) # \w不能匹配地址中的 "_" 和 "."

match = re.search(r'[\w.-]+@[\w.-]+',str)
if match:
	print(match.group())

# 判断手机是否合法





