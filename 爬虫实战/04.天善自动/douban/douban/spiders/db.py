# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest#向服务器发送请求
import urllib.request

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    #豆瓣有反爬机制，需要代理
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    # start_urls = ['http://douban.com/']
    def start_requests(self):
        return [Request('https://www.douban.com/accounts/login',callback=self.parse,meta={'cookiejar':1})]
        #设置cookie开启

    def parse(self, response):
        #提取验证码
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        url = 'https://www.douban.com/accounts/login'
        # 有码
        if len(captcha)>0:
            print('高清有码！')
            localpath = 'C:/Users/Jhon117/Desktop/demo/爬虫实战/04.天善自动/YZM.jpg'
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            print('请查看本地验证码图片并输入')
            captcha_value = input('验证码：')
            #redir设置登录后跳转的地址
            data = {'form_email':'835251902@qq.com',
                    'form_password':'90a092a1sv',
                    'captcha-solution':captcha_value,
                    'redir':'https://www.douban.com/people/186352558/'}

        else:
            print('高清无码！')
            #redir设置登录后跳转的地址
            data = {'form_email':'835251902@qq.com',
                    'form_password':'90a092a1sv',
                    'redir':'https://www.douban.com/people/186352558/'}
        print('loading....')
        return [FormRequest.from_response(response,meta={'cookiejar':response.meta['cookiejar']},headers=self.header,formdata=data,callback=self.next)]  #发送信息

    def next(self,response):
        print('已爬!')
        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])


