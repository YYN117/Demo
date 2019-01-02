import urllib.request
import re

def jokeCrawler(url):
   headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'
    }

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    HTML = response.read().decode('utf-8')

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'

    re_joke = re.compile(pat,re.S)
    diveList = re_joke.findall(HTML)
    print(diveList)
    print(len(diveList))

    with open(r'C:\Users\Jhon117\Desktop\demo\day15\file\file3.html','w') as f:
        f.write(HTML)

url = 'https://www.qiushibaike.com/'
info = jokeCrawler(url)
