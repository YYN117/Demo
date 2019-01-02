'''
描述:
给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11
'''
a = int(input('a:'))
b = int(input('b:'))
hex1 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
# a = hex1[10]
s=''
flag = True
if a < 0:
    a = -a
    flag = False
if a == 0:
    s = 0
else:
    while a != 0:
        n = a % b
        a = a // b
        if n < 10:
            s = str(n) + s
        else:
            s = str(hex1[n]) + s
if flag == False:
    s = '-' + s

print(s)