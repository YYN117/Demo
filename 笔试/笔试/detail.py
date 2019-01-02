# coding:utf-8
import requests as req
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import etree
import sys,io,re,json,random,time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def getId(page):
    url = 'https://hugoboss.tmall.com/i/asynSearch.htm?mid=w-15332902183-0&pageNo='+str(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
        'Referer': r'https://hugoboss.tmall.com/category.htm?pageNo='+str(page)
    }
    html = req.get(url,headers=headers).text
    selector = Selector(text=html)
    list = []
    for i in range(1,21):
        for j in range(1,4):
            ID = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']').extract_first()
            # print(ID)
            pattern = re.compile('[1-9]\d*')
            id = re.findall(pattern,ID)
            id = id[0]
            list.append(id)
    return list

def getInfo(list):
    for i in list:
        url='https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
            'Referer': r'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-15332902183.164.77b25984wckk93&id='+str(i)+'&rn=28fbb8675a2ea4165ae148caee14acb4&abbucket=11'
        }
        html = req.get(url,headers=headers).text

        # selector = Selector(text=html)
        info = str(html)
        # print(info)
        pattern = re.compile('[1-9]\d*')
        comments = re.findall(pattern, info)
        print(comments)
        n = len(comments)
        if n == 3:
            total = comments[2]
            grade = comments[1]
            print(total,grade)
        if n == 4:
            total = comments[3]
            grade = comments[1]+'.'+comments[2]
            print(total,grade)
        if n == 1:
            total = 0
            grade = None
            print(total,grade)
        print('*********')
        # time.sleep(1)


def main():
    pages = 1
    for i in range(1,pages+1):
        try:
            print('*********正在请求第%d页**********'%i)
            list = getId(i)
            getInfo(list)
            time.sleep(1)
        except:
            continue

main()
