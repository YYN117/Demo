import requests as req
import bs4
import json
import lxml,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
with open(r'F:\aa.txt', 'w', encoding='utf-8') as F:
    for i in range (1,30):
        url = 'http://search.chinahr.com/sh/job/pn'+str(i) + '/?key=python'
        ret = req.get(url)
        if ret.status_code==200:
            ret.encoding='utf-8'
            s = ret.text
            bs = bs4.BeautifulSoup(s, 'lxml')
            tes= bs.find_all(name='div',attrs={'class':'jobList pc_search_listclick'})
            for t in tes:
                tname=t.find(name='li',attrs={'class':'job-name'})
                tmp=t.find(name='li',attrs={'class':'job-salary'})
                tc=t.find(name='li',attrs={'class':'job-company'})
                tt=t.find_all(name='span')
                print(tname.get_text())
                F.write(json.dumps(tname.get_text(), ensure_ascii=False) + '\n')
                print(tmp.get_text())
                F.write(json.dumps(tmp.get_text(), ensure_ascii=False) + '\n')
                print(tc.get_text())
                F.write(json.dumps(tc.get_text(), ensure_ascii=False) + '\n')
                for n in tt[1:]:
                    print(n.get_text(), end=' ')
                    F.write(json.dumps(n.get_text(), ensure_ascii=False) + '\n')
                print('\n')
