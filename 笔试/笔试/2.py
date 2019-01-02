# coding:utf-8
import requests as req
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import etree
import sys,io,re,json,random,time,csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def getSimple(page):
    url = 'https://hugoboss.tmall.com/i/asynSearch.htm?mid=w-15332902183-0&pageNo='+str(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
        'Referer': r'https://hugoboss.tmall.com/category.htm?pageNo=1'
    }
    html = req.get(url,headers=headers).text
    selector = Selector(text=html)
    list_sim = []
    for i in range(1,21):
        for j in range(1,4):
            data1 = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']/dd[2]/a').extract_first()
            pattern = re.compile('[H](.*?)$')
            name = str(re.findall(pattern,data1))
            title = 'H'+(name.replace('[','').replace(']','').replace("'",'').replace('</a>','')).lstrip()
            list_sim.append(title)

            data2 = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']/dd[2]/div/div[1]/span[2]').extract_first()
            pattern2 = re.compile('\d{3,6}')
            price = str(re.findall(pattern2,data2))
            price = price.replace('[','').replace(']','').replace("'",'')
            price = price + '.00'
            list_sim.append(price)

            data3 = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']/dd[3]/div/h4/a/span').extract_first()
            pattern3 = re.compile('<span>(.*?)</span>')
            comments = str(re.findall(pattern3,data3)).replace('[','').replace(']','').replace("'",'').replace('评价: ','')
            list_sim.append(comments)

            data4 = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']/dd[2]/div/div[3]').extract()
            pattern4 = re.compile('[1-9]\d*')
            deals = str(re.findall(pattern4,str(data4))).replace('[','').replace(']','').replace("'",'')
            list_sim.append(deals)
    print(list_sim)

getSimple(1)

