from ..items import WeibospiderItem
import scrapy
class MySpider(scrapy.Spider):
    name = 'XL'
    allowed_domains = ['http://news.sina.com.cn/hotnews/']
    start_urls = [
         'http://news.sina.com.cn/hotnews/',
         ]

    def parse(self, response):
        from bs4 import BeautifulSoup

        print(response)

        soup = BeautifulSoup(response.text, "html.parser")

        # pTitle=soup.findAll('div',class_="content_tit")
        pDiv = soup.find_all('td', class_="ConsTi")

        for con in pDiv:
            yield WeibospiderItem(content=con.get_text())


