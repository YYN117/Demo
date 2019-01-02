# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    # start_urls = ['http://tencent.com/']
    baseURL = 'https://hr.tencent.com/position.php?&start='
    offset = 0  #偏移量
    start_urls = [baseURL+str(offset)] #第二页+10，第三页+20

    def parse(self, response):

        #请求响应
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencentItem() #引入字段类

            #文本内容，取列表的第一个元素[0]，将取出的Unicode编码转为utf-8
            item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode('utf-8')
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0].encode('utf-8')
            item['positionType'] = node.xpath("./td[2]/text()").extract()[0].encode('utf-8')
            item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0].encode('utf-8')
            item['workLocation'] = node.xpath("./td[4]/text()").extract()[0].encode('utf-8')
            item['publisTime'] = node.xpath("./td[5]/text()").extract()[0].encode('utf-8')

            yield item

        if self.offset<200:
            self.offset+=10
            url = self.baseURL + self.offset
            yield scrapy.Request(url,callback=self.parse())