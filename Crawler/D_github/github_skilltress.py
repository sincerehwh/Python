

import requests
from bs4 import BeautifulSoup


# 获取资源
# 存储资源
# 资源位置
# url = "https://github.com/TeamStuQ/skill-map/blob/master/data/source-skillmap-PNG-DesignByStuQ.md"
# respone = requests.get(url)
# with open("skill_tree.html","w") as f:
# 	f.write(respone.text)

# 创建 BeautifulSoup对象
soup = BeautifulSoup(open("skill_tree.html"))
#print(soup.())


all_lis = soup.find_all("li")

# for li in all_lis:
# 	print(li)

all_lis =  soup.find_all("li",class_="mr-3")
for li in all_lis:
	print(li)
	# print(li.children[0].attrs["href"])


