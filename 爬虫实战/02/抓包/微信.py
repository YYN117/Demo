#https://weixin.sogou.com/
'''
https://weixin.sogou.com/weixin?query=python&hp=40&sut=2044&lkt=4%2C1540196847330%2C1540196849372&_sug_=y&sst0=1540196849478&oq=Py&stj0=0&stj1=4&stj=0%3B4%3B0%3B0&stj2=0&hp1=&_sug_type_=&s_from=input&ri=0&type=2&page=1&ie=utf8&w=01015002&dr=1

https://mp.weixin.qq.com/s?src=11&timestamp=1540197017&ver=1197&signature=CTdo0NGNgFv2zO18A0DZmc6Y5UkB8osklFE2LhnT5Z8Yd6KeNKSY0QwTto7gB-MYSyTCW1sR0yaFOm1M0xjjAcld0xWTmI95lwEm*ofQidU-98uD1vpWw1QXFl7-dN-u&new=1

http://mp.weixin.qq.com/s?src=11&amp;timestamp=1540197017&amp;ver=1197&amp;signature=CTdo0NGNgFv2zO18A0DZmc6Y5UkB8osklFE2LhnT5Z8Yd6KeNKSY0QwTto7gB-MYSyTCW1sR0yaFOm1M0xjjAcld0xWTmI95lwEm*ofQidU-98uD1vpWw1QXFl7-dN-u&amp;new=1
'''

import re,urllib.request,time,urllib.error

#自定义函数，功能为使用代理服务器爬取网址
def use_proxy(proxy_addr,url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11')
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('exception:'+str(e))
        time.sleep(1)

key = 'Python'
proxy = '127.0.0.1:8888'
for i in range(10):
    key = urllib.request.quote(key)
    thispageurl = 'https://weixin.sogou.com/weixin?hp=40&query='+key+'&page='+str(i)
    thispagedata = use_proxy(proxy,thispageurl)
    print(len(str(thispagedata)))
    pat1 = 'a target="_blank" href="(.*?)'
    #re.S匹配多行
    rs1 = re.compile(pat1,re.S).findall(str(thispagedata))
    if(len(rs1)==0):
        print('{}页失败'.format(i))
        continue
    for j in range(0,len(rs1)):
        thisurl = rs1[j]
        thisurl = thisurl.replace('amp','')
        file = 'C:/Users/Jhon117/Desktop/demo/22/第'+str(i)+'页第'+str(j)+'篇文章.html'
        thisdata = use_proxy(proxy,thisurl)
        try:
            fh = open(file,'wb')
            fh.write(thisdata)
            fh.close()
            print('第{}页第{}篇成功'.format(i,j))
        except Exception as e:
            print(e)
            print('第{}页第{}篇失败'.format(i, j))





