
# SAX 流模式，边读边解析，
#	缺点：需要自己处理事件
#	优点：占用内存小，解析快，

import string

from xml.parsers.expat import ParserCreate

class DefaultSaxhandler:
	def start_element(self,name,attrs):
		self.name = name
		print("start --------: %s ,attrs: %s" % (name,str(attrs)))

	def end_element(self,name):
		print("end  --------: %s " % name)

	def char_data(self,text):
		if text.strip():
			print("%s 's text is : %s " %(self.name,text))


parser  = ParserCreate() 
handler = DefaultSaxhandler()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

with open("test.xml","r") as f:
	parser.Parse(f.read())