# coding:utf-8
import pymysql

def connect():
    db = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='test')
    return db

def exec(db):
    cursor = db.cursor()
    #将data1和data2中相同的数据创建一个表same
    create_same = cursor.execute('create table if not exists same select Name1,Product1,Date1,Name2,Product2,Date2 from data1,data2 where data1.Name1=data2.Name2 and data1.Product1=data2.Product2 and data1.Date1=data2.Date2 order by Name1 asc,Product1 asc,Date1 asc')
    #添加Result列
    add_T = cursor.execute("alter table same add column Result varchar(20) default 'TRUE' after Date1")

    #创建final_result表
    sql = 'create table if not exists Final_Result (Name1 varchar(20), Product1 varchar(20), Date1 date,Result varchar(20), Name2 varchar(20), Product2 varchar(20), Date2 date)'
    cursor.execute(sql)

    #将same中的数据插入final_result表中
    sql1 = 'insert into final_result(Name1,Product1,Date1,Result,Name2,Product2,Date2)select Name1,Product1,Date1,Result,Name2,Product2,Date2 from same'
    cursor.execute(sql1)

    #将data1与same对比，将data1独有的数据制作uni1表
    sql_uni1 = 'create table if not exists uni1 select Name1,Product1,Date1 from data1 where (data1.Date1 not in (select Date1 from same))or(data1.Product1 not in (select Product1 from same))or(data1.Name1 not in (select Name1 from same)) order by Name1 asc,Product1 asc,Date1 asc'
    cursor.execute(sql_uni1)
    #添加Result列
    cursor.execute("alter table uni1 add column Result varchar(20) default 'FALSE' after Date1")

    # 将data2与same对比，将data2独有的数据制作uni2表
    sql_uni2 = 'create table if not exists uni2 select Name2,Product2,Date2 from data2 where (data2.Date2 not in (select Date2 from same))or(data2.Product2 not in (select Product2 from same))or(data2.Name2 not in (select Name2 from same)) order by Name2 asc,Product2 asc,Date2 asc'
    cursor.execute(sql_uni2)
    #添加Result列
    cursor.execute("alter table uni2 add column Result varchar(20) default 'FALSE' after Date2")

    #将uni1和uni2中的数据分别插入到final_result表中
    sql_fin1 = 'insert into final_result(Name1,Product1,Date1,Result)select Name1,Product1,Date1,Result from uni1'
    sql_fin2 = 'insert into final_result(Name2,Product2,Date2,Result)select Name2,Product2,Date2,Result from uni2'
    cursor.execute(sql_fin1)
    cursor.execute(sql_fin2)

    db.commit()

def main():
    db = connect()
    exec(db)
    db.close()

main()


