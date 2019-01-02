'''
读文件过程：
1、打开文件
2、读文件内容
3、关闭文件
'''


'''
1，打开文件
open(path,flag,[encoding],[errors])
path:要打开的文件路径
flag:打开方式
r      以只读方式打开文件，文件的描述符放在文件的开头
rb     以二进制格式打开文件用于只读，文件的描述符放在开头
r+     打开一个文件用于读写，文件的描述符放在文件的开头
w      打开一个文件只用于写入，如果该文件已经存在会覆盖，不存在则创建新文件
wb     打开一个文件值用于写入二进制，如果该文件已经存在会覆盖，不存在则创建新文件
w+     打开一个文件用于读写，如果该文件已经存在会覆盖，不存在则创建新文件
a      打开一个文件用于追加，如果文件存在，文件描述符将放在文件末尾
a+     打开一个文件用于读写，如果文件存在，文件描述符将放在文件末尾
encoding:编码方式
errors:错误处理
'''


path = r'C:\Users\Jhon117\Desktop\demo\day7\file1.txt'
f = open(path,'r',encoding='utf-8')



'''
2.读文件内容
'''
#1，读取文件全部内容

# str1 = f.read()
# print(str1)

#2,读取指定字符数
str2 = f.read(10)
print('*'+str2+'*')

str3 = f.read(10)
print('$'+str3+'$')

#3,读取整行，包括'\n'字符
str4 = f.readline()
print(str4)
str5 = f.readline()
print(str5)

#4 读取指定字符数
# str6 = f.readline(10)
# print(str6)

#5 读取所以行并返回列表
# list7 = f.readlines()
# print(list7)

#6 若给的数字大于0，返回实际size字节的行数
list8 = f.readlines(25)
print(list8)

#修改描述符的位置
print('&&&&&&&&&&&&')
f.seek(0)
str9 = f.read()
print(str9)

'''
3,关闭文件
'''

f.close()



#完整过程

try:
    f1 = open(path,'r',encoding=utf-8)
    print(f1.read())
finally:
    if f1:
        f1.close()

#
with open(path,'r',encoding='utf-8')as f2:
    print(f2.read())


#将信息写入缓冲区

f.write('yyn is a poor man')

#刷新缓冲区
#直接把内部缓冲区的数据立刻写入文件，不是被动等待
f.flush()

while True:
    pass

f.close()