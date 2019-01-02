import urllib.request,re,urllib.error
url = 'https://news.sina.com.cn/'
data = urllib.request.urlopen(url).read()

#ignore忽略编码错误
data = data.decode('utf-8','ignore')
pth = 'href="(https://[a-zA-Z]*.?news.sina.com.cn/.*?)"'
allurl = re.compile(pth).findall(data)

for i in range(len(allurl)):
    try:
        print('第{}次爬取'.format(i+1))
        thisurl = allurl[i]
        file = 'C:/Users/Jhon117/Desktop/demo/22/'+str(i)+'.html'
        urllib.request.urlretrieve(thisurl,file)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
print(len(allurl))
