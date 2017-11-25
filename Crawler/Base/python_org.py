import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    # 处理标签开始
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass
    
def get_structure_entry(url):
    # 获取文本，并用gb2312解码
    content = requests.get(url).content
    # 确定要查找字符串的开始结束位置，并用切片获取内容。

    start = content.find('<div class="toctree-wrapper compound"')
    end = content.find('</div>')
    content = content[start:end + len('</div>')].strip()
    structure = []
    # 生成Sax处理器
    handler = DefaultSaxHandler(structure)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return structure

provinces = get_structure_entry('https://docs.python.org/3/library/index.html')

print(provinces)