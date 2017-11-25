
import os
import string

# 1.创建文件夹
try:
	os.mkdir("DatasParts")
except Exception as e:
	print(e)

# 2.创建文件
row_csv = open("DatasParts/row.csv","a")
user_csv = open("DatasParts/user.csv","a")
mall_csv = open("DatasParts/mall.csv","a")
time_csv = open("DatasParts/time.csv","a")
longitude_csv = open("DatasParts/longitude.csv","a")
latitude_csv = open("DatasParts/latitude.csv","a")
wifi_infos_csv = open("DatasParts/wifi_infos.csv","a")


with open("/Users/hwh/Desktop/data.csv","r") as f:
	for line in f:
		each_row_items = line.split(',')
		row_csv.write(each_row_items[0]+"\n")
		user_csv.write(each_row_items[1]+"\n")
		mall_csv.write(each_row_items[2]+"\n")
		time_csv.write(each_row_items[3]+"\n")
		longitude_csv.write(each_row_items[4]+"\n")
		latitude_csv.write(each_row_items[5]+"\n")
		wifi_infos_csv.write(each_row_items[6]+"\n")
	
row_csv.close()
user_csv.close()
mall_csv.close()
time_csv.close()
longitude_csv.close()
latitude_csv.close()
wifi_infos_csv.close()



# flieDatas = f.readlines()
# print(len(flieDatas))
# print(flieDatas[0])
# print(flieDatas[1])