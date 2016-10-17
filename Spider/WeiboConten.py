# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://baike.baidu.com/'
#payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=None)

r.encoding='utf-8'

soup=BeautifulSoup(r.text,"html.parser")


#pTitle=soup.findAll('div',class_="content_tit")

pContent=soup.findAll('div',class_="content_cnt")


# p=[pContent,pTitle]

# print(pContent)

for url in pContent:
    # print(url)
    if "词条"not in url.get_text()and "兑换"not in url.get_text()and "任务" not in url.get_text()and "商城"not in url.get_text():
        print(url.get_text())
    # print(url.get('a'))
    # if (url.get('a')==None):
    #     print(url.get_text())
#listUrls=soup.findAll()
