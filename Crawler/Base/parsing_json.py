
import json

dic = {"C":"stdio.h","Objective-C":"UIKit","Swift":"PKHUD","Python":"requests"}
print(dic)
print(type(dic))

# object -> json
encode = json.dumps(dic)
print(encode)
print(type(encode))

# json -> object
decode = json.loads(encode)
print(decode)
print(type(decode))

dic_to_json = json.loads('{"name":"louis","age":"26"}')
print(dic_to_json)
print(type(dic_to_json))

