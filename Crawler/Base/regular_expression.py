import re


# 3位数字 3到8个数字

mr = re.match(r'\d{3}-\d{3,8}',"010-11000000000000")

print(mr.string)


# 分组

m = re.match(r'(\d{3})-(\d{3,8})$',"010-11000000000000")


# 分割字符串
p = re.compile(r'\d+')
print(p.split("one1two2three3forth40"))

