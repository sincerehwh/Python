

''' 
	数组的转置和轴对称

'''

import numpy as np
import numpy.random as np_random


''' 矩阵运算

	加法
	| 1,2 |     | 2,4 |	   | 3,6 |
	|	  |	 +  |	  |  = |     |
	| 3,4 |	    | 3,4 |	   | 6,8 |

	减法
	| 3,4 |     | 2,4 |	   | 1,0 |
	|	  |	 -  |	  |  = |     |
	| 3,5 |	    | 3,4 |	   | 0,1 |

	乘法
	| 3,4 |     	  | 6,8 |
	|	  |	 X 2  =	  |     |
	| 3,4 |	     	  | 6,8 |	
	
	*乘法 
	| 3,4 |     | 2,2 |	    | 6,8 |
	|	  |	 *  |	  |  =  |     |
	| 3,5 |	    | 3,1 |	    | 9,5 |
	
	点乘dot(a,b)  a矩阵的列数 = b矩阵的行数 	->  a  b  
	a_11 x X_11 + a_12 x X_12 = Y_1		  | a_11, a_12 |     | X_11 , X_21 , X_31 |
	a_21 x X_21 + a_22 x X_22 = Y_2  -->  | a_21, a_22 |	 | X_12 , X_22 , X_32 | 
	a_31 x X_31 + a_32 x X_32 = Y_3 	  | a_31, a_32 |		
	
	| a,b |     | 1,2 |	    | ax1+bx3,ax1+bx4 |
	|	  |	 *  |	  |  =  |     			  |
	| c,d |	    | 3,4 |	    | cx1+dx3,cx2+dx4 |
	
'''


# 转置矩阵
array = np.arange(15).reshape((3,5))
print(array)
print(array.reshape(5,3)) #重构
print(array.T) # 转置

# 矩阵做点积

# array = np_random.randn(6,3) # 生成随机矩阵
print("------- array: ")
print(array)

print("------- array.T: ")
print(array.T)

print("矩阵相乘：")
print(array*array) # 纬度必须相同

print("矩阵做点积：")
print(np.dot(array,array.T))


# 高纬矩阵转换
print("\n-- 生成高维度矩阵 --\n")
arr = np.arange(24*4).reshape((3,2,4,4)) # 三层、两列、四行
print(arr)

print("\n-- 高纬矩阵转换 --\n")
print("ranspose((1,0,2)): ")
print( arr.transpose((1,0,3,2)) ) # 空间上把轴的位置做了调换，即变成了两层三列
 
print("\n-- 高纬矩阵转换 --\n")
print(arr.transpose((1,0,3,2)).reshape(3*2,8*2))


print(arr.swapaxes(1,2)) # 直接交换第一个和第二个坐标


