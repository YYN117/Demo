# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        item = DangdangItem()
        item['title'] = response.xpath("//a[@class='pic']/@title").extract()
        item['link'] = response.xpath("//a[@class='pic']/@href").extract()
        item['comment'] = response.xpath("//a[@class='search_comment_num']/text()").extract()
        yield item

        #循环爬取多页
        '''
        http://category.dangdang.com/cp01.54.06.00.00.00.html
        http://category.dangdang.com/pg2-cp01.54.06.00.00.00.html
        http://category.dangdang.com/pg3-cp01.54.06.00.00.00.html
        '''
        for i in range(1,5):
            url = 'http://category.dangdang.com/pg'+str(i)+'-cp01.54.06.00.00.00.html'
            yield Request(url,callback=self.parse)
