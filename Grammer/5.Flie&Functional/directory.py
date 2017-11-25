import os

# print(os.uname())
# os.name() is posix -> #nix
# os.name() is nt -> windows

''' 查看 创建路径 '''

# 获取路径
absPath = os.path.abspath(".")
print(absPath)

# 拼接路径
newPath = os.path.join(absPath,"12")
print(newPath)

# 拆分路径
split = os.path.split(newPath) 
print(split)

# 拆分文件 . 后缀名  
splitName = os.path.splitext(newPath)
print(splitName)


''' 修改文件的权限 '''

# chmod(path, mode) # 改变path指向的文件的权限。相当于$chmod命令。

# chown(path, uid, gid) # 改变path所指向文件的拥有者和拥有组。相当于$chown命令。

# stat(path) # 查看path所指向文件的附加信息，相当于$ls -l命令。

# symlink(src, dst) # 为文件dst创建软链接，src为软链接文件的路径。相当于$ln -s命令。

''' 创建\删除\修改 文件夹'''

# try:
# 	os.mkdir(newPath) # 如果存在文件夹，重新创建 ->  FileExistsError
# except Exception as e:
# 	print(e)

# try: 
# 	os.rmdir("pppppp1") # FileNotFoundError
# except Exception as e:
# 	print(e)

# try:
# 	os.rename(split[1],"") #FileNotFoundError
# except Exception as e:
# 	print(e)


''' 移动文件夹/复制文件夹 '''

#方法一： 读入写入文件 

#方法二： shutil
#  import shutil

# shutil.copyfile("you.txt",newPath+"/")

''' 列出文件夹的文件名 '''
list = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".txt"]
print(list)



