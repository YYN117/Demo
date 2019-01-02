import urllib.request
import urllib.parse
url = 'http://www.iqianyue.com/mypost/'
data = urllib.parse.urlencode(
    {
        'name':'835256216@qq.com',
        'pass':'161684131343134aff'
    }
).encode('utf-8')
req = urllib.request.Request(url,data)
des = urllib.request.urlopen(req).read()
with open('C:/Users/Jhon117/Desktop/demo/01.html','wb') as f:
    f.write(des)
