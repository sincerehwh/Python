


import time 

import datetime

print(time.time())
print(time.localtime())

#休眠
# for i in range(1,10):
# 	time.sleep(i)
# 	print("sdfds")

print(datetime.date.today())
print(datetime.datetime.now())

d =  datetime.date(2017,11,20)
t = datetime.time(14,11)
print(d)
print(t)

# 今天 - 明天 - 后天

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)

print(today,yesterday,tomorrow)

# 
