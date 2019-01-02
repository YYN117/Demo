# coding:utf-8
import requests as req
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import etree
import sys,io,re,json,random,time,csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def getIndex(url,headers):
    r = req.get(url,headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    print('检索请求成功')
    soup = BeautifulSoup(html,'html.parser')
    # goods = (soup.find_all(class_='skin-box-bd'))
    items = soup.find_all('li','cat fst-cat')
    items2 = soup.find_all('a','snd-cat-name')
    for item in items:
        title1 = item.select('.fst-cat-name')[0].text
        print(title1)
    for sec in items2:
        print(sec.string)

def main():
    start_url = 'https://hugoboss.tmall.com/category.htm?'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    getIndex(start_url,headers)


main()