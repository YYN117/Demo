# -*- coding: utf-8 -*-
# @date: 2018\11\16 001616:59
# @Author  : huangtao！！
# @FileName: 滚动条.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Programmer_huangtao
# 如果要定位的元素在页面的下方不可见的位置，需要对页面的滚动条进行操作，才能正确的
# 定位该元素
############################方法一:
# 将滚动条滚动到页面底部
# js = "documentElement.scrollTop=1000"#针对Firefox有效
# js = 'document.body.scrollTop=1000'#针对Chrome有效
# driver.execute_script(js)

# 将滚动条滚动到页面顶部
# js = "documentElement.scrollTop=0"
# driver.execute_script(js)
#############################方法二：
# 将滚动条滚动到可视范围内，只要能够定位该元素即可
# scrollIntoView(false)：参数flase是指元素不会滚动到页面顶部，只要在View页面
# 显示即可
# target = driver.find_element_by_xpath('//div[@id="3"]/h3/a')
# arguments[0]：指代的就是target，就是要定位的元素
# driver.execute_script("arguments[0].scrollIntoView(false);",target)
# time.sleep(5)
# print(target)
# target.click()
# ==============================================================================================
from time import sleep
# 时间库
from selenium import webdriver
# 模拟浏览器selenium
from lxml import etree

# xpath
chrome = webdriver.Chrome()
# 定义chrome方法浏览器
url = 'https://search.jd.com/Search?keyword=macbook%20pro&enc=utf-8&suggest=3.def.0.V16&wq=mac&pvid=37a8b260e0cb4727b9ea1f3b9c170cda'
# 访问的url,通过测试发现京东的数据只是加载30个，使用selenium第一次爬取时，但是拉动滚动条，发现源代码加载了30条商品数据，所以爬取京东数据时，要加入滚动条
chrome.get(url)
# 把url放到chrome方法里
js = 'document.documentElement.scrollTop=10000'
chrome.execute_script(js)
# 加入滚动条方法
sleep(5)
# 加入睡眠时间，发现拉动滚动条时，如果不加人时间的话，会是原来的数据，因为没有加载成功，所以加入睡眠时间，确定数据成功加载
html = chrome.page_source
# 得到html
e = etree.HTML(html)
# 使用etree方法解析
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]//i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')
# 解析商家名称和价格，但是商家信息有问题，发现寻找text（）时，数据为70，有其他不想要的数据，所以直接找到<em>标签
print(len(names))
# 打印商家数量
for name, price in zip(names, prices):
    # 循环遍历一下商家和价格
    print(name.xpath('string(.)'), ":", price)
    # 解析<em>标签中的内容，然后打印商家和价格
