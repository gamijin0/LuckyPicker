# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Bot.models import SendContent
import json
import os
class WeibospiderPipeline(object):
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        # filepath = "./RESULT"
        # if (os.path.exists(filepath) == False):
        #     os.mkdir(filepath)
        # # 文件名
        # import datetime
        #
        # filename = "XLContent[%s].txt" % (str(datetime.datetime.now())[0:10])
        # # 存储html
        # with open(os.path.join(filepath, filename), 'a') as f:
        #     f.write(item['content']+"\n")

        return item
    def open_spider(self, spider):
        self.file = open('./items.json', 'w')


    def close_spider(self, spider):
        self.file.close()

class MysqlPipeline(object):
    def process_item(self, item, spider):
        one=SendContent(content=item['content'])
        one.save()