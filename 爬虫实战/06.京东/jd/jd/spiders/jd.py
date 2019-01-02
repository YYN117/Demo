# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
import re
from jd.items import JdItem

class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com'] #允许爬取的域名
    start_urls = ['https://www.jd.com/']  #起始url
    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        try:
            i = JdItem()
            #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
            #i['name'] = response.xpath('//div[@id="name"]').extract()
            #i['description'] = response.xpath('//div[@id="description"]').extract()
            thisurl = response.url
            pat = "item.jd.com/(.*?).html"
            x = re.search(pat,thisurl)
            print(x)
            if(x):
                thisid = re.compile(pat).findall(thisurl)[0]

                title = response.xpath("//html/head/title/text()").extract()
                market = response.xpath("//div[@class='name']/a[@title]/text()").extract()
                priceurl = "https://p.3.cn/prices/mgets?callback=jQuery2115478&type=1&area=12_904_905_0&pdtk=&pduid=49570521&pdpin=jd_70195060640b4&pin=jd_70195060640b4&pdbp=0&skuIds=J_"+str(thisid)
                commenturl = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv69376&productId="+str(thisid)+"&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
                pricedata = urllib.request.urlopen(priceurl).read().decode('utf-8','ignore')
                commentdata = urllib.request.urlopen(commenturl).read().decode('utf-8','ignore')
                pricepat = '"p":"(.*?)"'
                commentpat = '"commentCount":(.*?),'
                price = re.compile(pricepat).findall(pricedata)
                comment = re.compile(commentpat).findall(commentdata)
                # print(title)
                # print(market)
                # print(price)
                # print(comment)
                # print(thisid)

                if(len(title) and len(market) and len(price) and len(comment)):
                    print(title[0])
                    print(market[0])
                    print(price[0])
                    print(comment[0])
                    print('*******************')
                    return  i
                else:
                    pass
            else:
                pass
            return  i
        except Exception as e:
            print(e)


