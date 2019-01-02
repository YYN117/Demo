import pymysql

db = pymysql.connect(host = 'localhost',user='root',password='1234',port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:',data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
db.close()
# db = pymysql.connect(host = 'localhost',user='root',password='1234',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null,primary key(id))'
# cursor.execute(sql)
# db.close()