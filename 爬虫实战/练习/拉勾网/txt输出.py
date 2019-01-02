# coding:utf-8
import requests,json
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400"}
n = int(input('页数：'))
file = open('laogou.txt','w',encoding='utf-8')
for i in range(1,n+1):
    url = 'https://www.lagou.com/zhaopin/Python/'+str(i)+'/'
    response = requests.get(url,headers = headers)
    # print(response.text)
    text = response.text
    parser = etree.HTML(text)
    lis = parser.xpath('//li[@class="con_list_item default_list"]')
    info = []
    for li in lis:
        py = {}
        name = li.xpath("@data-positionname")[0]
        salary = li.xpath("@data-salary")[0]
        company = li.xpath("@data-company")[0]
        location = li.xpath(".//span[@class='add']/em/text()")[0]
        fuli = li.xpath(".//div[@class='li_b_r']/text()")[0]
        file.write('第{}页'.format(i)+'\n'+'职位：'+name+'\n'+'薪水：'+salary+'\n'+'公司：'+company+'\n'+'地点：'+location+'\n'+'福利：'+fuli+'\n\n\n')
file.close()
#         py['name'] = name
#         py['salary'] = salary
#         py['company'] = company
#         py['location'] = location
#         py['fuli'] = fuli
#         info.append(py)
#     info.append("第{}页结束************************************".format(i))
#     json.dump(info,file,ensure_ascii=False)
# file.close()