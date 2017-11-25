

'''
	发送请求

	传递URL参数

	读取响应内容（文本/二进制/Json)

	定制请求头部

	Post请求

	响应状态码

	重定向和历史
	
	超时

'''

import requests
from io import BytesIO
from PIL import Image
import json

url = "https://www.baidu.com"

# r = requests.get(url)

# print(r.text)
# print(r.status_code)
# print(r.encoding)


# 传递参数
# parameters = {"name":"oop","language":"Python"}
# r = requests.get(url,parameters)
# print(r.url)


# 二进制数据
# url = "https://github.com/TeamStuQ/skill-map/blob/master/data/designbyStuQ/png-MachineLearning-by-StuQ.png"
# r = requests.get(url)
# image = Image.open(BytesIO(r.content))
# image.save("ml.jpg")


# json的处理
# r = requests.get("http://192.168.9.105:9090/zt_serve/app/getSeatDistricts")
# print(type(r.json))
# print(r.text)

# 原始数据的处理 -> 省内存
# r = requests.get("http://upload-images.jianshu.io/upload_images/1835526-ba704b80a85700fe.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/700")
# with  open("2.jpg","wb+") as f:
# 	for chunk in r.iter_content(1024):
# 		f.write(chunk)

# 提交表单
# form = {"name":"louis"}
# r.requests.post("http:// ",data = form)
# r.requests.post("http:// ",data = json.dumps(form))

# # cookie 
# url = "https://www.baidu.com"
# r = requests.get(url)
# cookies = r.cookies
# for k,v in cookies.get_dict().items():
# 	print(k,v)

# cookies = {'c':'v1'}

# r = requests.get("http://www.baidu.com",cookies=cookies)
# print(r.text)


# 重定向和重定向历史
r = requests.head('http://github.com',allow_redirects = True)
print(r.url)
print(r.status_code)
print(r.history)


# 代理
proxies = {"http":'....',"https":""}

r.requests.get("...",proxies=proxies)








