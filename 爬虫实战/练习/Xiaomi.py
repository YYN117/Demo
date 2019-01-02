#coding:utf-8
import requests, re, xlwt, datetime
from bs4 import BeautifulSoup
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def getHtmlText(url, headers):
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('网页请求成功！')
        return r.text
    except:
        print("网页请求失败")


def parserPage(infoList, html):
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    goods = soup.find_all('li', 'gl-item')
    try:
        for good in goods:
            name = good.select('.gl-i-wrap .p-name.p-name-type-2 em')[0].text
            price = good.select('.gl-i-wrap .p-price i')[0].text
            shop = good.select('.gl-i-wrap .p-shop a')[0].text
            comment = good.select('.gl-i-wrap .p-commit strong')[0].text
            infoList.append([price,name,shop,comment])
        print("网页解析成功！")
    except:
        print("网页解析失败")


def Write_Excel(ls, name):
    print("正在写入Exce表：")
    workbook = xlwt.Workbook(encoding='utf-8')
    name = "京东" + name + "商品信息"
    table = workbook.add_sheet(name)
    # table.col(3).width=256*20
    value = ["序号","价格", "商品名称",'商家','评论']
    for i in range(len(value)):
        table.write(0, i + 1, value[i])
    for i in range(len(ls)):
        value = [i + 1, float(ls[i][0]), ls[i][1],ls[i][2],ls[i][3] ]
        for j in range(5):
            table.write(i + 1, j + 1, value[j])
    workbook.save(name + '.xls')
    print("写入Excel表成功！请在本程序下同一路径下寻找excle")


def main():
    print("当前系统时间为：", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    start_url = "https://search.jd.com/Search?keyword="
    goods = input("请输入需要爬取的京东商品名称：")
    num = int(input("请输入需要爬取的页面数量："))
    infoList = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    for i in range(1, num + 1):
        try:
            # "&enc=utf-8&psort=3&page="
            # https://search.jd.com/Search?keyword=iphone&enc=utf-8&wq=iphone&pvid=12ae7273668546f3ab31880e5d3b543c
            # https://search.jd.com/Search?keyword=iphone&enc=utf-8&page=3&s=57&click=0
            url = start_url + goods + "&enc=utf-8&psort=3&page="+ str(i * 2 - 1)
            print("*****正在请求京东第%d页网页..loading.....*****" % i)
            html = getHtmlText(url, headers)
            print("*****正在解析京东第%d页网页..loading.....*****" % i)
            parserPage(infoList, html)
        except:
            continue
    # print(infoList)
    Write_Excel(infoList, goods)


main()