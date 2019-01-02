# coding:utf-8
import requests as req
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from lxml import etree
import sys,io,re,json,random,time,csv
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
'''
注:
每个产品与网站左侧的分类名单没有找到对应的关系，即网页代码中每个产品并未给出所属的类型，比如第一件商品属于男士新品，故列表中没有加入产品所属类型

商品详情页中没有‘大家都在说’的信息，仅有评分、销量，故无法得到‘大家都在说’
'''

# def getUrl(url,headers):
#     try:
#         r = req.get(url,headers=headers)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         t = r.text
#         print('网页请求成功')
#         return t
#     except:
#         print('网页请求失败')

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

def getSimple(page):
    url = 'https://hugoboss.tmall.com/i/asynSearch.htm?mid=w-15332902183-0&pageNo='+str(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
        'Referer': r'https://hugoboss.tmall.com/category.htm?pageNo='+str(page)
    }
    html = req.get(url,headers=headers).text
    selector = Selector(text=html)
    list_sim = []
    if page < 12:
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
                if len(deals)!= 0:
                    list_sim.append(deals)
                else:
                    list_sim.append('0')
    if page == 12:
        for i in range(1, 10):
            for j in range(1, 4):
                data1 = selector.xpath(
                    '/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(j) + ']/dd[2]/a').extract_first()
                pattern = re.compile('[H](.*?)$')
                name = str(re.findall(pattern, data1))
                title = 'H' + (name.replace('[', '').replace(']', '').replace("'", '').replace('</a>', '')).lstrip()
                list_sim.append(title)

                data2 = selector.xpath('/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(
                    j) + ']/dd[2]/div/div[1]/span[2]').extract_first()
                pattern2 = re.compile('\d{3,6}')
                price = str(re.findall(pattern2, data2))
                price = price.replace('[', '').replace(']', '').replace("'", '')
                price = price + '.00'
                list_sim.append(price)

                data3 = selector.xpath(
                    '/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(j) + ']/dd[3]/div/h4/a/span').extract_first()
                pattern3 = re.compile('<span>(.*?)</span>')
                comments = str(re.findall(pattern3, data3)).replace('[', '').replace(']', '').replace("'", '').replace(
                    '评价: ', '')
                list_sim.append(comments)

                data4 = selector.xpath(
                    '/html/body/div/div[3]/div[' + str(i) + ']/dl[' + str(j) + ']/dd[2]/div/div[3]').extract()
                pattern4 = re.compile('[1-9]\d*')
                deals = str(re.findall(pattern4, str(data4))).replace('[', '').replace(']', '').replace("'", '')
                if len(deals) != 0:
                    list_sim.append(deals)
                else:
                    list_sim.append('0')
        data1 = selector.xpath( '/html/body/div/div[3]/div[10]/dl/dd[2]/a').extract_first()
        pattern = re.compile('[H](.*?)$')
        name = str(re.findall(pattern, data1))
        title = 'H' + (name.replace('[', '').replace(']', '').replace("'", '').replace('</a>', '')).lstrip()
        list_sim.append(title)

        data2 = selector.xpath('//html/body/div/div[3]/div[10]/dl/dd[2]/div/div[1]/span[2]').extract_first()
        pattern2 = re.compile('\d{3,6}')
        price = str(re.findall(pattern2, data2))
        price = price.replace('[', '').replace(']', '').replace("'", '')
        price = price + '.00'
        list_sim.append(price)

        data3 = selector.xpath('/html/body/div/div[3]/div[10]/dl/dd[3]/div/h4/a/span').extract_first()
        pattern3 = re.compile('<span>(.*?)</span>')
        comments = str(re.findall(pattern3, data3)).replace('[', '').replace(']', '').replace("'", '').replace(
            '评价: ', '')
        list_sim.append(comments)

        data4 = selector.xpath(
            '/html/body/div/div[3]/div[10]/dl/dd[2]/div/div[3]/span').extract()
        pattern4 = re.compile('[1-9]\d*')
        deals = str(re.findall(pattern4, str(data4))).replace('[', '').replace(']', '').replace("'", '')
        if len(deals) != 0:
            list_sim.append(deals)
        else:
            list_sim.append('0')
    return list_sim

def getId(page):
    url = 'https://hugoboss.tmall.com/i/asynSearch.htm?mid=w-15332902183-0&pageNo='+str(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
        'Referer': r'https://hugoboss.tmall.com/category.htm?pageNo='+str(page)
    }
    html = req.get(url,headers=headers).text
    selector = Selector(text=html)
    id_list = []
    if page < 12:
        for i in range(1,21):
            for j in range(1,4):
                ID = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']').extract_first()
                pattern = re.compile('[1-9]\d*')
                id = re.findall(pattern,ID)
                id = id[0]
                id_list.append(id)
    if page == 12:
        for i in range(1,10):
            for j in range(1,4):
                ID = selector.xpath('/html/body/div/div[3]/div['+str(i)+']/dl['+str(j)+']').extract_first()
                pattern = re.compile('[1-9]\d*')
                id = re.findall(pattern,ID)
                id = id[0]
                id_list.append(id)
        ID = selector.xpath('/html/body/div/div[3]/div[10]/dl').extract_first()
        pattern = re.compile('[1-9]\d*')
        id = re.findall(pattern, ID)
        id = id[0]
        id_list.append(id)
    return id_list

def getInfo(list):
    # time.sleep(1)
    total_and_grade = []
    for i in list:
        url='https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400",
            'Referer': r'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-15332902183.164.77b25984wckk93&id='+str(i)+'&rn=28fbb8675a2ea4165ae148caee14acb4&abbucket=11'
        }
        html = req.get(url,headers=headers).text
        info = str(html)
        # print(info)
        pattern = re.compile('[1-9]\d*')
        comments = re.findall(pattern, info)
        n = len(comments)
        if n == 3:
            total = comments[2]
            grade = comments[1]
            total_and_grade.append(total)
            total_and_grade.append(grade)
        if n == 4:
            total = comments[3]
            grade = comments[1]+'.'+comments[2]
            total_and_grade.append(total)
            total_and_grade.append(grade)
        if n == 1:
            total = 0
            grade = '无数据'
            total_and_grade.append(total)
            total_and_grade.append(grade)
    return total_and_grade

def main():
    start_url = 'https://hugoboss.tmall.com/category.htm?'
    # pages = 12
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
    # getIndex(start_url,headers)
    csvFile = open(r"C:\Users\Jhon117\Desktop\demo\笔试\product_table1.csv", 'w', newline='')
    csvFile2 = open(r"C:\Users\Jhon117\Desktop\demo\笔试\product_eva_table1.csv", 'w', newline='')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(('product_id', 'Sku_name', 'Total_sales', 'price', 'Total_comment_count', 'Product_score'))
        writer2 = csv.writer(csvFile2)
        writer2.writerow(('product_id', 'eva_tag'))

        for i in range(1,13):
            if i < 12:
                try:
                    # url = start_url+'pageNo='+str(i)
                    print('///////////////////////正在请求第%d页///////////////////////'%i)
                    # html = getUrl(url,headers)
                    simpleInfo = getSimple(i)
                    print(simpleInfo)
                    id = getId(i)
                    print(id)
                    time.sleep(1)
                    total_score = getInfo(id)
                    print(total_score)
                    print('/////////////////////////第%d页完成/////////////////////////'%i)
                    for j in range(61):
                        writer.writerow((id[j],simpleInfo[j*4],simpleInfo[(j*4)+3],simpleInfo[(j*4)+1],total_score[j*2],total_score[(j*2)+1]))
                        writer2.writerow((id[j],total_score[(j*2)+1]))
                    time.sleep(1)
                except:
                    continue
            if i == 12:
                try:
                    print('///////////////////////正在请求第%d页///////////////////////'%i)
                    simpleInfo = getSimple(i)
                    print(simpleInfo)
                    id = getId(i)
                    print(id)
                    total_score = getInfo(id)
                    print(total_score)
                    print('/////////////////////////第%d页完成/////////////////////////'%i)
                    for j in range(29):
                        writer.writerow((id[j],simpleInfo[j*4],simpleInfo[(j*4)+3],simpleInfo[(j*4)+1],total_score[j*2],total_score[(j*2)+1]))
                        writer2.writerow((id[j],total_score[(j*2)+1]))
                    time.sleep(1)
                except:
                    continue

    finally:
        csvFile.close()

main()