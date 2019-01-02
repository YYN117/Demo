from pymongo import MongoClient

# 连接服务器
conn = MongoClient('localhost',27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

# 添加文档
# collection.insert({'name':'帅宝','age':23,'gender':1,'address':'靖江','isDelete':0})
collection.insert([{'name':'廖博士','age':23,'gender':1,'address':'安庆','isDelete':0},{'name':'龙哥','age':25,'gender':1,'address':'宿迁','isDelete':0}])

# 断开
conn.close()