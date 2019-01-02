import pymysql

db = pymysql.connect('localhost','root','1234','kaige')
cursor = db.cursor()


sql = 'delete from bandcard where money=200'

try:
    cursor.execute(sql)
    db.commit() #提交
except:
    #如果提交失败，回滚至上一次的数据
    db.rollback()

cursor.close()
db.close()