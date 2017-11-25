
arr = [1,2,3,4,5,6,7,8,9,'a','b','c','d']

# 切片 [start:end:steps]

print(arr[:9])  # [:) 左闭右开区间
print(arr[:9:2])
print(arr[0:9])
print(arr[0:10:3])
print(arr[5:100:3]) # 越界不处理
print(arr[9:200]) # 

# 负值处理
print(arr[5:-2])
print(arr[100::-1]) # 从大到小

# 切片生成新的对象
re_arr = arr[::-1]
print(re_arr)
