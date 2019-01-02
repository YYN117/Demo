# coding:utf-8
import requests, re
from bs4 import BeautifulSoup
import lxml,sys,io,json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

with open(r'C:\Users\Jhon117\Desktop\demo\爬虫实战.sb.txt','w',encoding='utf-8')as F:
    for i in range(1,2):
        print('**********')
        url = 'http://search.chinahr.com/sh/job/pn' + str(i) + '/?key=python'
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        s = r.text
        bs = BeautifulSoup(s,'html.parser')
        tes = bs.find_all(name='div', attrs={'class':'jobList pc_search_listclick'})
        for t in tes:
            tname = t.find(name='li', attrs={'class': 'job-name'})
            tmp = t.find(name='li', attrs={'class': 'job-salary'})
            tc = t.find(name='li', attrs={'class': 'job-company'})
            tt = t.find_all(name='span')
            print(tname.get_text())
            F.write(json.dumps(tname.get_text(), ensure_ascii=False) + '\n')
            print(tmp.get_text())
            F.write(json.dumps(tmp.get_text(), ensure_ascii=False) + '\n')
            print(tc.get_text())
            F.write(json.dumps(tc.get_text(), ensure_ascii=False) + '\n')
            for n in tt[1:]:
                print(n.get_text(), end=' ')
                F.write(json.dumps(n.get_text(), ensure_ascii=False) + '\n')
            print('')
            print('********')


