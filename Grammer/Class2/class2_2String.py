
import string

print(type(string))

s = ' H e l l o P y t h o n '

# 字符串不可以被修改
# 去处空格 -> 返回新的字符串
# strip 剥去

print(s.strip()) # 两边的空格都去掉
print(s.lstrip()) # 左边的空格去掉
print(s.rstrip()) # 右边的空格去掉
print(s)


''' 字符串拼接 '''
str1 = '123'
str2 = '456'
str3 = str1+str2
print(str3)

''' 大小写转换 '''
strA = "AAAAAAAA"
stra = 'aaaaaaaa'

print(strA+" upper -> "+strA.upper())
print(stra+" upper -> "+stra.upper())
print(strA+" lower -> "+strA.lower())
print(stra+" lower -> "+stra.lower())
print(strA+" capitalize -> "+strA.capitalize()) #   

''' 位置比较 '''
str_1 = 'abcdefg hijkl mnopk'
str_2 = 'zwxtvduifhsakdfhjdhfkajsd'

try:
	print(str_1.index('fg'))
	print(str_2.index('fhk'))	
except ValueError:
	print('Value Error')


''' 长度计算 '''
string = '123456789'
print(len(string))

s = ''
if not s :
	print("'' is False") 


''' 分割与连接字符串 '''

str_ = '''1,2,3,
		  343234
		  ,,,34,5
		  ,34,,,,'''

splite = str_.split(',') # 按照字符分割，''不能作为分隔符
print(splite)

splite = str_.split('\n') # 用\n分割
print(splite)

splite = str_.splitlines() # 按照行来分割，
print(splite)

arr = ['111B','A222B','A333B'] 
print('-'.join(arr)) # 用'-'粘合字符串
print(','.join(arr)) # 用','粘合字符串
print('\n'.join(arr)) # 用','粘合字符串


''' 常用判断 '''

s = 'hello i am a python developer'
print(s.startswith('hello')) # 以某字符开头
print('12345ab'.isalnum()) # 
print('/t123434'.isdigit()) # 纯数字
print(' '.isspace()) # 纯空格
print(' '.islower()) # 纯小写
print(' '.upper()) # 纯大写
print('A，'.istitle()) # 开头大写


''' 数字与字符串的转化 '''
print(str('1'))
print(str('1.0'))
print(str('1.')) # 自动补零
print(str('12123123.1231'))
print(str('-23123.1231'))

print(int('123123123',4))
print(float('12121.1212'))

s = 'sdjfksajdfas'
l  = list(s)
print(l)


### 实现单词反转 'l love  China!' -> 'China! I love' // 要保留所有的空格
























