# coding:utf-8
import requests, re
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

n = int(input('页数：'))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
file = open('淘宝零食.txt','w',encoding='utf-8')
for i in range(0,n):
    url = 'https://s.taobao.com/search?spm=a21bo.2017.201867-links-8.62.5af911d9wSyBZ4&q=%E9%9B%B6%E9%A3%9F&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180724&ie=utf8&bcoffset=12&ntoffset=12&p4ppushleft=1%2C48&s='+str(i*44)
    rs = requests.get(url,headers=headers)
    rs.encoding = 'utf-8'
    title = re.findall(r'"raw_title":"([^"]+)"', rs.text, re.I)  # 正则保存所有raw_title的内容，这个是书名，下面是价格，地址
    price = re.findall(r'"view_price":"([^"]+)"', rs.text, re.I)
    loc = re.findall(r'"item_loc":"([^"]+)"', rs.text, re.I)
    num = re.findall(r'"view_sales":"(.*?)"',rs.text,re.I)

    for j in range(0, len(title)):
        file.write('第{}页'.format(i+1)+'\n'+'序号：'+str(i*44+j+1)+'\n'+'产品：'+title[j]+'\n'+'价格：'+price[j]+'\n'+'地点：'+loc[j]+'\n'+'付款人数：'+num[j]+'\n\n')
file.close()