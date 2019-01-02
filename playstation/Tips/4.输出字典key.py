'''
描述:
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

例如：a={1:1,2:2,3:3}, 则输出：1,2,3

'''
a={1:1,2:2,3:3}
b = a.keys()
print(type(b))
b = list(b)
print(type(b))
c = []
for i in b:
    if str(i).isdigit():
        # Python isdigit()方法检测字符串是否只由数字组成。
        c.append(i)
c.sort()
print(','.join(str(j) for j in c ))