
# DOM 把整个XML读入内存，解析为树，因此
#	缺点：占用内存大，解析慢，
#	优点：可以任意遍历树的节点

from xml.dom import minidom

doc = minidom.parse("test.xml")
print(doc)

root = doc.documentElement
print(root)

books = root.getElementsByTagName("book")
for book in books:
	title = book.getElementsByTagName("title")
	print(title)
	
# root = doc.documentElement()
# print("root: ",dir(root))

