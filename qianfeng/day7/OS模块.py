import os
'''
OS:包含了普遍的操作系统的功能

'''

#获取操作系统类型   nt->windows   posix  ->Linux\Unix或 Mac Os X
print(os.name)

#获取操作系统中的所以环境变量
print(os.environ)

#获取指定环境变量
print(os.environ.get('APPDATA'))

#获取当前目录  ./a/
print(os.curdir)

#获取当前工作目录，即当前python脚本所在目录
print(os.getcwd())

#以列表形式返回指定目录下的所有的文件
print(os.listdir(r'C:\Users\Jhon117\Desktop\demo\day7'))

#在当前目录下创建新目录
# os.mkdir('sunck')

#删除目录
# os.rmdir('sunck')

#获取文件属性
# print(os.stat('sunck'))

#重命名
# os.rename('sunck','yyn')

#删除文件
# os.remove('file.txt')

#运行shell命令
# os.system('notepad')
# os.system('write')
# os.system('mspaint')
# os.system('msconfig')
# os.system('notepad')
# os.system('shutdowm -s -t 500')
# os.system('shutdown -a')
# os.system('taskkill /f /im notepad.exe')


#有些方法存在os模块里，还有一部分在os.path
#查看当前的绝对路径
print(os.path.abspath('./yyn'))

#拼接路径
p1 = r'C:\Users\Jhon117\Desktop\demo\day7'
p2 = 'yyn'
#参数2中不要有\
print(os.path.join(p1,p2))

#拆分路径
path2 = r'C:\Users\Jhon117\Desktop\demo\day7\yyn'
print(os.path.split(path2))

#获取扩展名
print(os.path.splitext(path2))

#是否是目录
print(os.path.isdir(path2))

#判断文件是否存在
print(os.path.isfile(path2))


#判断目录是否存在
path3 = r'C:\Users\Jhon117\Desktop\demo\day7'
print(os.path.exists(path3))

#获得文件大小(字节)
print(os.path.getsize(path2))

#文件的目录
print(os.path.dirname(path3))

#文件的名
print(os.path.basename(path3))