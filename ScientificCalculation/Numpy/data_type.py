
'''
________________________________
|	Data type  |   Description |
|______________|_______________|
			   |
bool		   |	Boolean (True or False) stored as a byte
int            | 	Platform integer (normally either int32 or int64)
int8		   |	Byte (-128 to 127)
int16		   |	Integer (-32768 to 32767)
int32		   |	Integer (-2147483648 to 2147483647)
int64		   |	Integer (9223372036854775808 to 9223372036854775807) //百亿亿
uint8		   |	Unsigned integer (0 to 255)	
uint16 		   |	Unsigned integer (0 to 65535)
uint32		   |	Unsigned integer (0 to 4294967295)
uint64		   |	Unsigned integer (0 to 18446744073709551615)
float		   |	Shorthand for float64.
float32		   |	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
float64 	   |	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
complex		   | 	Shorthand for complex128.
complex64	   | 	Complex number，represented by two 32-bit floats (real and imaginary components)
complex128	   |	Complex number,represented by two 64-bit floats (real and imaginary components)
bool - ?	   |	存储True和False值的布尔类型
object - O     |    Python对象类型
string_ - S    |    固定长度的字符串类型。S10代表长度为10的字符串。
unicode_ - U   |    固定长度的unicode类型

'''

import numpy as np


# 生成数组是指定数据类型
a_array = np.array([1,2,3,4,5],dtype=np.float64)
print(a_array)

b_array = np.array([1,2.11,3,4,5],dtype=np.int32)
print(b_array) 

''' 小数 --> 整数，小数部分会被去掉 '''

# astype

# 复制数组并转换数据类型
int_array = np.array([1,2,3,4,5])
print("int_array: ",int_array)

float_array = int_array.astype(np.float)
print("float_array: ",float_array)

complex_array = float_array.astype(np.complex)
print("complex_array: ",complex_array)

# 字符串 --> 数组
str_array = np.array(['1.1','2.1','3.1'],dtype=np.string_)
float_array = str_array.astype(dtype=np.float)
print(float_array)

# 使用其他数组的数据类型作为参数
int_array = np.arange(10) 
float_array = np.array([.11,.22,.33,.44],dtype=np.float64)
print(int_array.astype(int_array.dtype)) # astype做了复制，数组本身不变
print(int_array[0],int_array[1])












