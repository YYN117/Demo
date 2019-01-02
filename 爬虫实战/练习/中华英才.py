# coding:utf-8
import requests, xlwt
from bs4 import BeautifulSoup
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def getHtmlText(url, headers):
    try:
        r = requests.get(url, headers=headers)
        # Response对象status_code属性标识http请求响应的状态码：
        # 如果是返回200，则raise_for_status()并不会抛出异常
        r.raise_for_status()
        # 从内容分析出的响应内容编码方式（备选编码方式）
        r.encoding = r.apparent_encoding
        s = r.text
        print('网页请求成功！')
        return s
    except:
        print("网页请求失败")

def parserPage(infoList, html):
    # html字符串创建BeautifulSoup对象
    soup = BeautifulSoup(html, "html.parser")
    # goods = soup.find_all(name='div', attrs={'class':'jobList pc_search_listclick'})
    goods = soup.find_all('div', 'jobList pc_search_listclick')
    try:
        for good in goods:
            # name = good.select('.gl-i-wrap .p-name.p-name-type-2 em')[0].text
            name = good.select('.job-name')[0].text
            # name = good.find(name='li',attrs={'class':'job-name'})
            # price = good.find(name='li',attrs={'class':'job-salary'})
            price = good.select('.job-salary')[0].text
            # company = good.find(name='li',attrs={'class':'job-company'})
            company = good.select('.job-company')[0].text
            reward = good.find_all(name='span')
            # res = good.select('.job-fuli span').text
            # name = name.get_text()
            # price = price.get_text()
            # company = company.get_text()
            res = []
            for i in reward[1:]:
                res.append(i.get_text())
            res = '  '.join(res)
            infoList.append([name,price,company,res])
        print("网页解析成功！")
    except:
        print("网页解析失败")

def Write_Excel(ls):
    print("正在写入Exce表：")
    workbook = xlwt.Workbook(encoding='utf-8')
    name = "求职信息"
    table = workbook.add_sheet(name)
    # table.col(3).width=256*20
    value = ["序号","工作", "待遇",'公司','福利']
    for i in range(len(value)):
        table.write(0, i + 1, value[i])
    for i in range(len(ls)):
        value = [i + 1, ls[i][0], ls[i][1],ls[i][2],ls[i][3]]
        for j in range(5):
            table.write(i + 1, j + 1, value[j])
    workbook.save('英才网.csv')
    print("写入Excel表成功！请在本程序下同一路径下寻找excle")

def main():
    start_url = 'http://search.chinahr.com/sh/job/pn1/?key=python'
    num = int(input("请输入需要爬取的页面数量："))
    infoList = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    for i in range(1, num + 1):
        try:
            # http://search.chinahr.com/sh/job/pn1/?key=python
            # http://search.chinahr.com/sh/job/pn3/?key=python
            url = 'http://search.chinahr.com/sh/job/pn'+str(i)+'/?key=python'
            print("*****正在请求中华英才网第%d页网页..loading.....*****" % i)
            html = getHtmlText(url, headers)
            print("*****正在解析中华英才网第%d页网页..loading.....*****" % i)
            parserPage(infoList, html)
        except:
            continue
    Write_Excel(infoList)

main()

