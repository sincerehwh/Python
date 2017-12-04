'''
# 转义

# 运算

# 多行字符串

# Unicode字符串

# 字符串函数

'''


# 转义
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出



# 运算
# +	字符串连接	a + b  
# *	重复输出字符串	
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	H in a 输出结果 1
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	M not in a 输出结果 1
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print r'\n' prints \n 和 print R'\n' prints \n
# %	格式字符串	请看下一节内容。

print("hello"+ " world")
print("hello world. "*10)
print("hello world. "[0])
print("hello world. "[0:100])
print("hello world. " in "hello world. ")
print(r"1""3""5""7")

print ("Python %s 诞生于 %d 年？" % ('是', 1986))


# 多行字符串 下面的两个字符串是等价的
str = "这是 \n\
一段 \n\
很长 \n\
的字 \n\
符串"
print(str)

str = """这是
一段
很长
的字
符串"""
print(str,"\n")



''' 字符串的内建函数


'''


# 首字母大写
hello =  "hello python".capitalize()
print(hello)

# center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
print(hello.center(100,'?'))

# count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。 
# str.count(sub, start= 0,end=len(string))
print("as;dbfiasbdifnlasdjnf;ajnds;fjnas;i duflahsdfhlasjdnfkjnasd;fjnasjdnf;kajns".count('as',0,1000))

# decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
# bytes.decode(encoding="utf-8", errors="strict")
 # encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
ecstr = str.encode("utf-8")
print(ecstr)
destr = ecstr.decode("utf-8")
print(destr)


# endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
# endswith()方法语法： str.endswith(suffix[, start[, end]])
# startswith(str, beg=0,end=len(string))
str = "www.baidu.com"
print(str.endswith(".com",0,1000))

# expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# expandtabs()方法语法：
# str.expandtabs(tabsize=8)
# tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。
str = """www\twww"""
print(str)
print(str.expandtabs(10))

# isalnum() 方法检测字符串是否由字母和数字组成。
# isalnum()方法语法：
# str.isalnum()
print(str.isalnum())

# decimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
print("123".isdecimal())

# isalpha() 方法检测字符串是否只由字母组成。
print("ablG".isalpha())

# str.isdigit() 检测字符串是否只由数字组成
print("123".isdigit())

# islower() 方法检测字符串是否由小写字母组成。
print("abc".islower())

# isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
print("U: ",u"12992039".isnumeric())

#  isspace() 方法检测字符串是否只由空白字符组成。
print(" ".isspace())

# istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
print("He is Go ".istitle())

# isupper() 方法检测字符串中所有的字母是否都为大写。
print("HELLO".isupper())

# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
print("__".join(["1","2",'3','4','5']))

# len() 字符串的长度
print(len("hhhhh"))

# lower() 方法转换字符串中所有大写字符为小写。
print("LPppppPPPPp".lower())

# upper() 方法转换字符串中所有小写字符为大写。
print("oooopaodfs".upper())

# swapcase() 方法用于对字符串的大小写字母进行转换
print("AbCdEfGh".swapcase())

# 所有单词都是以大写开始,其余字母均为小写
print("a b cEEE DEEEe".title())

# lstrip() 方法用于截掉字符串左边的空格或指定字符。
print("     122 333".lstrip())
print("ppppp122 333".lstrip('pp'))

# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
print("     122 333".strip())
print("ppppp122 333".strip('pp'))

# maketrans() 方法用于创建字符映射的转换表
# Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# str.maketrans(intab, outtab)
# intab -- 字符串中要替代的字符组成的字符串。
# outtab -- 相应的映射字符的字符串。

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))


# max() 方法返回字符串中最大的字母
str = "POIDHDHHXZ"
print(max(str))

# min() 方法返回字符串中最小的字母
str = "POIDHDHHXZa"
print(min(str))


# replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str = "# replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max字，则替换不超过 max字"
print(str.replace("字","words",3))


# index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# index()方法语法：
# str.index(str, beg=0, end=len(string))
# str不在 string中会报一个异常。
str = "?Hello python????????"
print(str.index("ll")) 

# rindex()
str = "?Hello python????????"
print(str.rindex("lo")) 

# find() 方法检测字符串中是否包含子字符串 str ，
# 如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
str = "?Hello python????????"
print(str.find("lll")) 

# rfind() 从右边开始查找,返回字符串最后一次出现的位置，如果没有匹配项则返回-1
str = "rfind() 从右边开始查找,返回字符串最后一次出现的位置，如果没有匹配项则返回-1"
print(str.rfind("()",0,10000))


# rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串

str = "111"
print(str.rjust(10,"0")) 


# string 字符串末尾的指定字符（默认为空格）.
str = "PPP00p"
print(str.rstrip("PPP00p"))


# split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
# str.split(str="", num=string.count(str)).
str = "print (str.split())"
print (str.split()) # 默认用空格分割
print (str.split('i',100)) # 
print (str.split('s')) # 分割全部


# splitlines() 按照行('\r', '\r\n', \n')分隔，
# 返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# str.splitlines([keepends])
# keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。
str = """p
O
P
PPP
LL"""
print(str.splitlines(True))


# translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
# translate()方法语法：
# str.translate(table[, deletechars]); 
# bytes.translate(table[, delete])    
# bytearray.translate(table[, delete]) 
# 返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。
intab = "字"
outtab = "P"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
str = "# 返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。"
print(str.translate(trantab))

# zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
str = "a000"
print(str.zfill(40))





