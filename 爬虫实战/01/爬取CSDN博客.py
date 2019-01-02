import urllib.request,re,urllib.error

url = 'https://blog.csdn.net/'
head = ('User-Agent','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11')
opener = urllib.request.build_opener()
opener.addheaders = [head]
data = opener.open(url).read()
data = data.decode('utf-8','ignore')
pth = 'a href="(https://blog.csdn.net/.*?)"'
allurl = re.compile(pth).findall(data)

for i in range(len(allurl)):
    try:
        print('第{}次爬取'.format(i+1))
        thisurl = allurl[i]
        file = 'C:/Users/Jhon117/Desktop/demo/22/'+str(i+1)+'.html'
        urllib.request.urlretrieve(thisurl,file)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
print(len(allurl))
