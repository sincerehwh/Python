
try:
	import cPickle as pickle
except ImportError:
	import pickle


''' 序列化 - 反序列化 '''

# 定义对象
dic = {"name":"louis","weight":78,"height":175}

# 序列化处理
dicSer = pickle.dumps(dic)
print(dicSer)

# 创建或打开一个文件
file = open("serialize.txt",'wb')

# 将内容序列化写入文件
pickle.dump(dic,file)

# 关闭文件
file.close()

pickle.l



''' JSON '''
import json

# 定义字典
nDic = {"a":"Hello","b":"World"}

# json序列化处理
nDicS = json.dumps(nDic)

# 反序列化
f = json.loads(nDicS)
print(f)


