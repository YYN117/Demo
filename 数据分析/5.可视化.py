import pandas as pda
import numpy as npy
import matplotlib.pyplot as pyl
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',passwd='1234',db = 'kaige')
sql = 'select * from student'
data = pda.read_sql(sql,conn)
# print(k)
# a = k.describe()
# print(a)
print(data.values)
# print(data.values[0])
data2 = data.T
y1 = data2.values[2]
x1 = data2.values[0]
pyl.plot(x1,y1)
pyl.show()