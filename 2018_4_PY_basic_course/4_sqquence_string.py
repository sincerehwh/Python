


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
print("{0:<30}1\n{1}{2:>30}".format("Right","Center","Left"))





