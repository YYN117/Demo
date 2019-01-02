# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import  Request
from qsauto.items import  QsautoItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['qiushibaike.com']

    # start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        ua = {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}
        yield Request('http://www.qiushibaike.com/',headers = ua)

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )  #follow表示链接是否跟进

    def parse_item(self, response):
        i = QsautoItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        i['content'] = response.xpath("//div[@class='content']/text()").extract() #提取段子的内容
        i['link'] = response.xpath("//link[@rel='canonical']/@href").extract() #提取段子的连接
        print(i['content'])
        print(i['link'])
        print('')
        return i
