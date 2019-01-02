import urllib.request

url = 'https://blog.csdn.net/weiwei_pig'
head = ('User-Agent','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11')
opener = urllib.request.build_opener()
opener.addheaders = [head]
data = opener.open(url).read()
with open('C:/Users/Jhon117/Desktop/demo/03.html','wb') as f:
    f.write(data)