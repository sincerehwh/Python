



# 字符串格式设置

#########		#########
######### 精简版 #########
#########  		#########
format = "This is %s ,Who are you ? %s got to ... "
values = ("louis","2018.10.1")
st = format % values
print(st)

# from string import Template
# temple = Template("This is $who ,Who are you ? $when got to ... ")
# st = temple.substitute = (who="louis",when="2018.10.1")
# print(st)

#########		#########
######### 完整版 #########
#########  		#########

# 字段名
# 转换标志
# 格式说明符

str_1 = "{} {} {} {}".format(1,1,"22","33")
print(str_1)

str_2 = "{0} {1} {2} {3}".format("Index0","Index1","Index2","Index3")
str_3 = "{3} {2} {1} {0}".format("Index0","Index1","Index2","Index3")
print(str_2)
print(str_3)

# 手动
str_4 = "{game} {name} {bar} {status}".format(name = "name",game = "game",bar = "bar",status="status")
print(str_4)


#########  基本转换	#########

print("{:.2f}".format(10))
print("{:b}".format(10))
print("{:d}".format(10))
print("{:o}".format(10))
print("{:x}".format(10))
print("{:X}".format(10))
print("{:c}".format(100))

print("{}".format(10e-10))
print("{:g}".format(10e-10))
print("{:G}".format(10e-10))
print("{:%}".format(1))

#########  宽度+精度+千位分隔符 #########

print("{:10}".format(100)) # 数字加前面
print("{:10}".format("122")) # 文字加后面

print("{:.10f}".format(10e-3)) # 精度
print("{:10.1f}".format(10e-2)) # 宽度+精度
print("{:30,.3f}".format(10e10)) # 分隔符


#########  对齐方式 #########
print("{0:<20}\n{1:^20}\n{2:>20}".format("Right","Center","Left"))

print("{0:10.2f}\n{1:=10.3f}".format(100,-100)) # 等号填充

print("{:b}".format(42))
print("{:#b}".format(42))
print("{:g}".format(42))
print("{:#g}".format(42))
print("{:x}".format(42))
print("{:#x}".format(42))



#########			#########
######### 字符串方法 #########
#########  			#########
# center find join lower
# replace split strip translate 

print("louis".center(30))
print("louis".center(30,"^"))

print("louis".find("is"))
print("louis".find("is",0,16)) # [0,16)

li = ['1','2','3','4','5','6']
print("+".join(li))

print("HELLO".lower())
print("hello".upper())
print("h l world !".title())

print("I am a prog".replace("a","^^"))

spl = "12+13+14"
print(spl.split("+"))
print(int(spl.split("+")[0]))

stri = "  sdfdf ".strip() # 剔除两端的空格
print(stri)
stri = "***!!! name is a name *22!!** ".strip(" *!2")
print(stri)


table = str.maketrans(".","P")
tran = " ..OO.. ".translate(table)
print(tran)

# 判断字符串是否满足特定的条件
print("123".isalnum())
print("123".isalpha())
print("123".isdigit())
print("123.0".isdecimal())
print("Aa".islower())
print("Ab".isupper())
print("Ab".istitle())




