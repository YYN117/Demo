import re
import urllib.request
# pat = '<div class="name">[\S]*</div>'
pat = '<div class="name">(.*?)</div>'
path = 'https://read.douban.com/provider/all'
data = urllib.request.urlopen(path).read()
data = data.decode('utf-8')
res = re.compile(pat).findall(data)
print(res)
# print(data)
with open(r'C:/Users/Jhon117/Desktop/demo/01.txt','w') as f:
    for i in range(len(res)):
        f.write(res[i]+'\n')
