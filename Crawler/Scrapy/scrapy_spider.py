
import scrapy


class HHSpider(scrapy.Spider):
	name = "Kaka"
	start_urls = ["http://www.julyedu.com/"]

	def parser(self,response):
		with opem("f.json",'w') as f:
			f.write(response)
		# for s_class in response.xpath('//*[@id="courseList"]/li[1]/ul'):
		# 	print(s_class.xpath("li[1]/a[1]/h3")).extract_first()

		# 	yield{"title":s_class.xpath()}.extract_first()


