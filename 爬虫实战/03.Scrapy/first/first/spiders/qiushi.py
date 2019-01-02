# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem
from scrapy.http import Request
'''
<div class="content">
<span>

<a href="/article/121160670" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
'''

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']

    def start_requests(self):
        ua = {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}
        yield Request('http://www.qiushibaike.com/',headers = ua)

    def parse(self, response):
        it = FirstItem()
        it['content'] = response.xpath("//div[@class='content']/span/text()").extract() #提取段子的内容
        it['link'] = response.xpath("//a[@class='contentHerf']/@herf").extract() #提取段子的连接
        yield  it