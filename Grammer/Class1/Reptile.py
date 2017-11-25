
# coding: utf-8

import requests
import xml.etree.ElementTree as ET

from xml.parsers.expat import ParserCreate

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class  DefaultSaxHandler(object):
	"""docstring for  DefaultSaxHandler"""
	def __init__(self, provinces):
		self.provinces = provinces

	def start_element(self,name,attrs):
		if name != "map":
			name = attrs["titles"]
			number = attrs["href"]
			self.provinces.append((name,number))

	def end_element(self,name):
		pass

	def char_data(self,text):
		pass

def get_provinces(url):
	content = requests.get(url).content.decode('gb2312')

	print(content.encode('utf-8'))
	start = content.find('<map name= \"map_86" id=\"map_86\">')
	end = content.find('<map>')

	content = content[start:end + len('</map>')].strip()
	print("content")
	print(content)

	provinces = []
	handler = DefaultSaxHandler(provinces)
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(content)
	return provinces

provinces = get_provinces('http://www.ip138.com/post')
print(provinces)







