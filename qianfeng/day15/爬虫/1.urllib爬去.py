import urllib.request

url = r'http://www.baidu.com'
#解码
newUrl2 = urllib.request.unquote(url)
print(newUrl2)

#解码
newUrl = urllib.request.unquote(newUrl2)
print(newUrl)

# #向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen(newUrl)

# #读取文件的全部内容,会把读取的数据赋值给一个字符串变量
data = response.read()
print(data)
print(type(data))
#
# #读取一行
# # data = response.readline()
#
# #读取文件的全部内容，会把读取到的数据赋值给一个列表变量
# data = response.readlines()
# '''
# print(data)
# print(type(data))
# print(len(data))
# print(type(data[100].decode('utf-8')))
# '''
#
# #将爬取的网页写入文件
# # with open(r'C:\Users\Jhon117\Desktop\demo\day15\file\file1.html','wb') as f:
# #     f.write(data)
#
# #response 属性
# #返回当前环境的有关信息
# print(response.info())
#
# #返回状态码
# print(response.getcode())
# # if response.getcode() == 200 or response.getcode() == 304:
# #     # 处理网页
# #     # pass
#
# # 返回当前正在爬取的url地址
# print(response.geturl())
#
# url = r'https://www.bilibili.com/watchlater/#/av19956343/p140'
#
# newUrl = urllib.request.quote(url)
# print(newUrl)