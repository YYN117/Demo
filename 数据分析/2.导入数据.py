# coding:utf-8
import sys,io,xlrd
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import pandas as pda
i = pda.read_excel('C:/Users/Jhon117/Desktop/demo/爬虫实战/英才网.csv')
print(i.describe())
print(i.sort_values(by='序号')) #排序

#导入MySQL数据
# import pymysql
# conn = pymysql.connect(host = 'localhost',user = 'root',passwd='root',db = 'hexun')
# sql = 'select * from myhexun'
# k = pda.read_sql(sql,conn)

#导入html数据
from bs4 import BeautifulSoup
import html5lib
l = pda.read_html(r'C:\Users\Jhon117\Desktop\demo\数据分析\abc.html')
print(l)
m = pda.read_html(r'https://book.douban.com/')
print(m)

#导入文本
t = open('abc.txt')
n = pda.read_table(t)
print(n)