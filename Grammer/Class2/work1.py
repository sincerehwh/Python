
def reserve(str_list,start,end):
	while  start<end:
		str_list[start],str_list[end] = str_list[end],str_list[start]
		start += 1
		end -= 1

sentece = " Hello, I am louis hwh, an iOS developer "
str_list = list(sentece)
i = 0

while  i < len(str_list):
	if str_list[i] != " ":
		start = i
		print(start,"start")
		end = start+i
		while  (end < len(str_list)) and str_list[end] != " ":
			end += 1
		reserve(str_list,start,end-1)
		i = end
	else:
		i += 1


print(str_list)