

# 序列通用操作

# 索引 切片 + *
# 成员资格 len max min 

sq_list = [1,2,3,4,5,6]
sq_tuple =  (1,2,3,4,5,6)
sq_string = "1,2,3,4,5,6,"
print(sq_list)
print(sq_tuple)
print(sq_string,"\r\n")

sq_index = 0
sq_list_index = sq_list[sq_index]
sq_tuple_index = sq_tuple[sq_index]
sq_string_index = sq_string[sq_index]
print("列表索引{} ：".format(sq_index),type(sq_list_index),sq_list_index)
print("元组索引{} ：".format(sq_index),type(sq_tuple_index),sq_list_index)
print("字符索引{} ：".format(sq_index),type(sq_string_index),sq_string_index,"\r\n")

sq_slice_s = 0
sq_slice_e = 4
sq_list_slice = sq_list[sq_slice_s:sq_slice_e]
sq_tuple_slice = sq_tuple[sq_slice_s:sq_slice_e]
sq_string_slice = sq_string[sq_slice_s:sq_slice_e]
print("列表切片[{}:{}] ：".format(sq_slice_s,sq_slice_e),type(sq_list_slice),sq_list_slice)
print("元组切片[{}:{}] ：".format(sq_slice_s,sq_slice_e),type(sq_tuple_slice),sq_tuple_slice)
print("字符切片[{}:{}] ：".format(sq_slice_s,sq_slice_e),type(sq_string_slice),sq_string_slice,"\r\n")


sq_list_add = sq_list + sq_list 
sq_tuple_add = sq_tuple + sq_tuple
sq_string_add = sq_string + sq_string
print("列表切片+列表切片:",type(sq_list_add),sq_list_add)
print("元组切片+列表切片:",type(sq_tuple_add),sq_tuple_add)
print("字符切片+列表切片:",type(sq_string_add),sq_string_add)

sq_X = 4
sq_list_X= sq_list * sq_X 
sq_tuple_X = sq_tuple * sq_X
sq_string_X = sq_string * sq_X
print("列表切片+列表切片:",type(sq_list_X),sq_list_X)
print("元组切片+列表切片:",type(sq_tuple_X),sq_tuple_X)
print("字符切片+列表切片:",type(sq_string_X),sq_string_X)

sq_property = "1"
print(sq_property in sq_list)
print(sq_property in sq_tuple)
print(sq_property in sq_string)

print("len(sq_list):",len(sq_list))
print("len(sq_tuple)",len(sq_tuple))
print("len(sq_string)",len(sq_string))

print("max(sq_list):",max(sq_list))
print("max(sq_tuple)",max(sq_tuple))
print("max(sq_string)",max(sq_string))

print("min(sq_list):",min(sq_list))
print("min(sq_tuple)",min(sq_tuple))
print("min(sq_string)",min(sq_string))



