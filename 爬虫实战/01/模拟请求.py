import urllib.request
keywd = '磊哥'
keywd = urllib.request.quote(keywd) #中文编码
url = 'http://www.baidu.com/s?wd='+keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
with open('C:/Users/Jhon117/Desktop/demo/02.html','wb') as f:
    f.write(data)