from pymongo import MongoClient

# 连接服务器
conn = MongoClient('localhost',27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

# 更新
collection.update({'name':'lilei'},{'$set':{'age':29}})

#删除
collection.remove({'name':'lilei'})

#删库跑路
collection.remove()

# 断开
conn.close()