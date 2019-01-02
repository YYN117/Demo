import pymysql

db = pymysql.connect('localhost','root','1234','kaige')
cursor = db.cursor()

#检测表是否存在，若存在则删除
cursor.execute('drop table if exists bandcard')

#建表
sql = 'create table bandcard(id int auto_increment primary key,money int not null)'

cursor.execute(sql)

cursor.close()
db.close()