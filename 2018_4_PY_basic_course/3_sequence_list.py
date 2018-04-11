

sq_list = ["h",'e','laa','laa','odfdfff']


print('原列表：',sq_list)

# 修改列表元素
sq_list[1] = "H"
print("sq_list[1] = H 后的列表",sq_list)


############## 			##############
############## 列表方法	##############
##############  		##############

# append clear
# copy count
# extend index
# insert pop
# remove reverse
# sort 高级排序

#  append
sq_list.append("L")
print("sq_list.append('L'):",sq_list)

# extend
sq_list.extend(["L","L","H"])
print("sq_list.append('L'):",sq_list)

# copy
sq_list.copy()
print("sq_list.copy('L'):" ,sq_list) 

# count
print("sq_list.count('L'):  ",sq_list.count("L")) # ⚠️  1.返回的是第一个 2.没有的话会报错

# index
print("sq_list.index('L'):",sq_list.index("L")) # ⚠️  1.返回的是第一个 2.没有的话会报错

# insert 
sq_list.insert(10,"PPPP")
print('sq_list.insert(10:"PPP"):',sq_list)

# pop
print("pop:",sq_list.pop())

# remove
sq_list.remove("L")
print("sq_list.remove('L'):",sq_list)  # 第一个

# reverse 大 -》 小
sq_list.reverse()
print("sq_list.reverse()",sq_list)

# sort 小 -》 大
sq_list.sort()
print("sq_list.sort()",sq_list)

# clear
# sq_list.clear()
print("clear:",sq_list)

# 高级排序 https://wiki.python.org/moin/HowTo/Sorting
sq_list.sort(key=len)
print("sq_list.sort(key=len):",sq_list)

sq_list.sort(reverse=True)
print("sq_list.sort(reverse= ):",sq_list)



############## 			##############
##############  Tuple	##############
##############  		##############

sq_tuple = (1,2,3,4,5,6,"1","1")

# count
print("sq_tuple.count('L'):  ",sq_tuple.count("1")) # 第一个

# index
print("sq_tuple.index('L'):",sq_tuple.index("1")) 




