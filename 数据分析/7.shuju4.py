# -*- coding:UTF-8 -*-
import pymysql
import pandas as pd
import numpy as np
conn = pymysql.connect(host='localhost',user='root',passwd='1234',db='test')
sql = "select * from taob"
sql1 = "select price,comment from taob"
data = pd.read_sql(sql1,conn)
print(data.describe())
#理查标准化
data2 = (data - data.min())/(data.max() - data.min())
# print(data2)
#标准差标准化
data3 = (data - data.mean())/data.std()
# print(data3)
#小数定标规范化
k=np.ceil(np.log10(data.abs().max()))
data4 = data/10**k
# print(data4)

#等宽离散化
data5 = data['price'].copy()
data6 = data5.T
data7 = data6.values
# print(sorted(data7))
print(data7)
k = 4
a = pd.cut(data7,k,labels=['cheap','medium','lux','top'])
a1 = pd.cut(data7,[0,13,45,78,100,457,1020122])
a2 = pd.cut(data7,[0,20,100,300,500,2000,data7.max()])
print(a2)