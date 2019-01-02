import re

'''
字符串切割
'''
str1 = 'sunck    is a good man'
print(str1.split(' '))
print(re.split(r' +',str1))  # x+ 表示至少一个x

'''
re.finditer函数
原型：finditer(pattern,string,flags = 0)
参数： 
patter： 匹配的正则表达式
string： 要匹配的字符串
flags: 标志位，用于控制正则表达式的匹配方式

功能： 扫描整个字符串，与findall类似，扫描整个字符串，返回一个迭代器
'''
str3 = 'sunck is a good man! sunck is a nice man! sunck is a handsome man'
d = re.finditer(r'(sunck)',str3)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break

'''
字符串的替换个修改
sub(pattern,repl,string,count=0,flags=0)
subn(pattern,repl,string,count=0,flags=0)

pattern:    正则表达式(规则)
repl:       指定的用来替换的字符串
string:     目标字符串
count:      最多替换次数
flags:      默认0
功能：      在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定字符串。可以指定替换的次数，如果不指定，替换所以匹配的字符串

区别：      前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
'''
str5 = 'sunck is a good good good man'
print(re.sub(r'(good)','nice',str5))
print(type(re.sub(r'(good)','nice',str5)))
print(re.subn(r'(good)','nice',str5))
print(type(re.subn(r'(good)','nice',str5)))
print('&&&&&&&&&')

'''
分组：
概念：     除了简单的判断是否匹配之外，正则表达式还可以提取子串。用()括起来的表示的是提取分组

'''
str6 = '010-53247654'
m = re.match(r'(?P<first>\d{3})-(?P<last>\d{8})',str6)
#使用序号获取对应组的信息，group(0)代表原始字符串
print(m.group(0))
print(m.group(1))
print(m.group('first'))
print(m.group(2))
#查看匹配的各组的情况
print(m.groups())

'''
编译：当使用正则表达式时，re模块做两件事
1、编译正则表达式。如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern,flags=0)
pattern:要编译的正则表达式

'''
pat = r'^1(([3578]\d)|(47)){8}$'
#编译成正则对象
re_telephone = re.compile(pat)
print(re_telephone.match('18260032928'))

