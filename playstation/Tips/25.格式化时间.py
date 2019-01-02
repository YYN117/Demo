'''
描述:
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
'''
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
res = t['year'].zfill(4)+'-'+t['month'].zfill(2)+'-'+t['day'].zfill(2)+' '+t['hour'].zfill(2)+':'+t['minute'].zfill(2)+':'+t['second'].zfill(2)
print(res)



'''
描述
Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

语法
zfill()方法语法：

str.zfill(width)
参数
width -- 指定字符串的长度。原字符串右对齐，前面填充0。
返回值
返回指定长度的字符串。

实例
以下实例展示了 zfill()函数的使用方法：

#!/usr/bin/python

str = "this is string example....wow!!!";

print str.zfill(40);
print str.zfill(50);
以上实例输出结果如下：

00000000this is string example....wow!!!
000000000000000000this is string example....wow!!!
'''