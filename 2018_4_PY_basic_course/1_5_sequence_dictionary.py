

### 创建字典 ### 

person = {"name":"louis","age":"27"}

print(person)

it = [('name','louis'),('age','27')]
d = dict(it)
print(d)

person = dict(name="louis",age="27")
print(person)


######### 基本的操作 #########
######### 基本的操作 #########
######### 基本的操作 #########

print(len(person))

print(person["name"])

person["name"] = "Pop"
print(person)

del person["name"]
print(person)

print("age" in person)


# 字典的字符串设置
dic = {"name":"louis"}
print("Who is {name}?".format_map(dic))


######### 字典方法 #########
######### 字典方法 #########
######### 字典方法 #########

# clear copy fromkeys
# get itmes keys 
# pop popitem setdefault
# update values 

or_dic = {"1":"A","2":"B","3":"C","4":"D","123":None}


cp_dic = or_dic.copy()
print(cp_dic)

print(or_dic.clear())

fk_dic = cp_dic.fromkeys(["1","2","3","4"])
print(fk_dic)

get_dic = cp_dic.get("is","None??")
print(get_dic)

items = cp_dic.items()
print(items)

keys = cp_dic.keys()
print(keys)

values = cp_dic.values()
print(values)

pop = cp_dic.pop("1") # 不存在会报错
print(pop)

pop_item = cp_dic.popitem()
print(pop_item)

cp_dic.setdefault("123","123") # 原来不存在重新设置
print(cp_dic)

new_dic = {"Louis":"name","1":"Perfect"}
cp_dic.update(new_dic)
print(cp_dic)












