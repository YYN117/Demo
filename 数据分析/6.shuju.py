'''
import pymongo
cilent = pymongo.MongoClient(host='local',port=27017)
db = cilent['images360']
collection = db['images']
'''
import pymysql
import numpy as np
import pandas as pda
conn = pymysql.connect(host='localhost',user = 'root',password='1234',port=3306,db='kaige')
sql = 'select * from student'
data = pda.read_sql(sql,conn)
print(data.describe())

# x = 0
# data['price'][(data['price']==0)]=None
# for i in data.columns:
#     for j in range(len(data)):
#         if(data[i].isnull())[j]:
#             data[i][j] = 36
#             x+=1
# print(x)

data2 = data.T
age = data2.values[2]
id = data2.values[1]
import matplotlib.pylab as pyl
pyl.plot(id,age,'o')
pyl.show()