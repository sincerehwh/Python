
'''
	Beautiful Soup:

		格式化后浏览数据
		访问Tag
		访问属性
		获取文本
		注释处理
		搜索
		css选择器

''' 

# import requests
# c = requests.get("https://www.baidu.com")
# with open("soup.html",'w') as f:
# 	f.write(c.text)



from bs4 import BeautifulSoup

soup = BeautifulSoup(open("soup.html"))

#print(soup.prettify())
print(type(soup.title))
print(soup.title.name)
print(soup.title)

for items in soup.body.contents:
	print(items)


# CSS查找

print(soup.select(".sister"))
print(soup.select("#link1"))
print(soup.select("head > title"))
