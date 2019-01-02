# -*- coding: utf-8 -*

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdPipeline(object):
    def __init__(self):
        self.fh = open('C:/Users/Jhon117/Desktop/demo/22/c.txt','w')

    def process_item(self, item, spider):
        print(item['title'])
        print(item['market'])
        print(item['price'])
        print(item['comment'])
        print('--------')
        self.fh.write(item['title'][0]+'\n'+item['market'][0]+'\n'+item['price'][0]+'\n'+item['comment'][0]+'\n'+'*************'+'\n')
        return item

    def close_spider(self):
        self.fh.close()
