''' 文件的读入与写入 '''
#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

''' read():将所有文件读到一个字符串里面
	readline():一行一行的读
	readlines():将文本文件中所有的行读到一个list中，一行一个元素

	open("","r") :
	"r":只读，
	"r+":读写
	"w":只写
	"w+"::读写
	"rb":读入二进制
	"rb+":读xie二进制
	"wb":写入二进制
	"wb+":读写二进制
	"a":追加
	"ab":追加二进制文件
	"a+":打开一个文件在末尾读写
	"ab+":打开一个二进制文件在末尾读写
'''


# 方法一: ------------------------------------

fileR = open("youth_En.txt","r")
fileW = open("write.txt","w")

''' read() '''
#read = fileR.read()
#print(read)

''' readline() 可以跳读  ''' 
# while True:
# 	line = fileR.readline()
# 	fileW.write(line[:]+"0000000000")
# 	print(line)
# 	if not line:
# 		break
# fileR.close()
# fileW.close()

''' readlines '''
read = fileR.readlines()
print(read)


# 方法二：------------------------------------
# 文件迭代器：
# file2_R = open("write.txt","w")
# for line in open("youth_En.txt","r"):
# 	print(line)
# 	file2_R.write(line[:])
# file2_R.close()


# 方法三：------------------------------------
# with open 自带关闭文本的功能
with open("i.png","rb") as f:
	#print(f.read())
	for line in f:
		print(line)

