# -*- coding: utf-8 -*-
import scrapy
import json

class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']
    # start_urls = ['https://shouji.jd.com/']
# 'https://list.jd.com/list.html?cat=9987,653,655'

    def parse(self, response):

        # print(response.body)
        jd_json = json.loads(str(response.body,encoding='gbk'),encoding='gbk')

        result = []
        for data in jd_json['data']:
            for data2 in data['s']:
                url = data2['n'].split('|')[0]
                title = data2['n'].split('|')[1]
                # print(title, url)
                result1={"url":url,
                       'title':title,
                       'child' : []
                       }

                for data3 in data2['s']:
                    url2 = data3['n'].split('|')[0]
                    title2 = data3['n'].split('|')[1]
                    # print('*******',title2,  url2)

                    result2 = {"url":url2,
                               'title':title2,
                               'child' : []
                               }

                    for data4 in data3['s']:
                        url3 = data4['n'].split('|')[0]
                        title3 = data4['n'].split('|')[1]
                        # print('$$$$$$$$$$$$$$$$$$$$',title3,url3)
                        result2['child'].append({"url":url3,
                               'title':title3,
                               })
                    result1['child'].append(result2)
                result.append(result1)
        print(result)
        # pass
