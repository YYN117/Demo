 
'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式

json文件组成
{}  代表对象（字典）
[]  代表列表
:   代表键值对
,   分隔两个部分
'''
import json

jsonStr = "{'name':'sunck凯','age':18,'hobby':['money','power','english'],'parames':{'a':1,'b':2}}"
#将json格式的字符串转为python数据类型的对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData['hobby'])