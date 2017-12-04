
import requests

# http://www.python-requests.org/en/master/

def http(url):
	with open("http_request.txt",'a') as f:
		options_response = requests.options(url)
		print("options_response: ",options_response.headers,'\n')
		f.write("\noptions_response:%s \n" % options_response.headers)

		head_response = requests.head(url)
		print("head_response: ",head_response.headers,'\n')
		f.write("\nhead_response:%s \n" % head_response.headers)

		get_response = requests.get(url)
		print("get_response: ",get_response.headers,'\n')
		f.write("\nget_response:%s \n" % get_response.headers)

		put_response = requests.put(url)
		print("put_response: ",put_response.headers,'\n')
		f.write("\nput_response:%s \n" % put_response.headers)


		post_response = requests.post(url)
		print("post_response: ",post_response.headers,'\n')
		f.write("\npost_response:%s \n" % post_response.headers)



		delete_response = requests.delete(url)
		print("delete_response: ",delete_response.headers,'\n')
		f.write("\ndelete_response:%s \n" % delete_response.headers)


		patch_response = requests.patch(url)
		print("patch_response: ",patch_response.headers,'\n')
		f.write("\npatch_response: " % patch_response.headers)


r = requests.get("http://www.louishwh.top")
print(r.status_code)


r = requests.get("http://www.baidu.com")
print(r.status_code)


# 200/OK，请求成功
# 201 请求已实现，新资源请求已建立
# 201 已接受请求，但尚未处理

# 400 请求无法被服务器理解
# 401 请求需要用户验证
# 403 服务器理解请求，拒绝执行
# 404 Not Found 

