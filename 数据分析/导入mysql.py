import pandas as pda
import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',passwd='1234',db = 'kaige')
sql = 'select * from student'
k = pda.read_sql(sql,conn)
print(k)
a = k.describe()
print(a)