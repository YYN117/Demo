# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentPipeline(object):
    def __init__(self):
        self.fh = open('C:/Users/Jhon117/Desktop/demo/22/b.txt', 'w')

    def process_item(self, item, spider):

        self.fh.write(item['positionName'][0]+'\n'+item['positionLink'][0]+'\n'+item['positionType'][0]+'\n'+item['positionNumber'][0]+'\n'+item['workLocation'][0]+'\n'+item['publishTime'][0]+'\n'+'*************'+'\n')
        return item


    def close_spider(self,spider):
        self.fh.close()