'''
描述:
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。这里将字母表的z和a相连，如果超过了z就回到了a。

例如a="cagy", b=3,

则输出 ：fdjb
'''
def jia_mi(a,b):
    l = []
    b = int(b)
    if not (0<=b<26):
        print('b:ERROR')
    for i in a:
        if ord(i)+b>122:
            y = chr((ord(i) + b) - 122 + 96)
            l.append(y)
        else:
            y = chr(ord(i) + b)
            l.append(y)
    z = ''.join(l)
    print(z)

a = input('a:').lower()
b = input('b:')
jia_mi(a,b)