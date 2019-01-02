import urllib.request

def imageCrawler(url,toPath):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'
    }
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    HTMLStr = response.read()
    with open(r'C:\Users\Jhon117\Desktop\demo\day16\0.爬虫联系\yhd.html','wb') as f:
        f.write(HTMLStr)

    pat = r''


url = 'http://search.yhd.com/c9987-0-0'
toPath =r'C:\Users\Jhon117\Desktop\demo\day16\0.爬虫联系\image'
imageCrawler(url,toPath)