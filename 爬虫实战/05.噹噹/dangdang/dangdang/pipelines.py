# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost',user='root',passwd='root',db ='dd',charset="utf8")
        conn = conn.cursor()
        conn.execute("SET NAMES utf8")
        for i in range(0,len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            comment = item['comment'][i]
            # print(title)
            # print(link)
            # print(comment)
            sql = "insert into books(title,link,comment) value('"+title+"','"+link+"','"+comment+"')"
            conn.query(sql)
        conn.close()
        return item
