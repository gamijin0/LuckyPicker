# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#百度百科首页url
url = 'https://baike.baidu.com/'

r = requests.get(url, params=None)
#必须转换编码
r.encoding='utf-8'

soup=BeautifulSoup(r.text,"html.parser")

#pTitle=soup.findAll('div',class_="content_tit")

pContent=soup.findAll('div',class_="content_cnt")

#将结果存储在文件中
#url.get_text()为一条新闻，str；
import os

filepath = "./Result"
if (os.path.exists(filepath) == False):
    os.mkdir(filepath)
# 文件名
import datetime

filename = "weiboContent[%s].txt" % (str(datetime.datetime.now())[0:10])
# 存储html
with open(os.path.join(filepath, filename), 'w') as f:
    for url in pContent:
        if "词条" not in url.get_text() and "兑换" not in url.get_text() and "任务" not in url.get_text() and "商城" not in url.get_text():
            print(url.get_text())
            f.write(url.get_text())
            f.write('\n ')
            #print(isinstance(url.get_text(),str))


