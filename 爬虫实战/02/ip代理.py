import urllib.request
import re

def use_proxy(url,proxy_addr):
    #使用代理服务器
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    #添加全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
    return data

proxy_addr = '121.49.110.65:8888'
url = 'http://www.baidu.com'
data = use_proxy(url,proxy_addr)
print(len(data))