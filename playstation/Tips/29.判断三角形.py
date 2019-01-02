'''
一个三角形中，任意两边之和大于第三边，任意两边之差小于第三边。
'''

def sanjiao(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        print('YES')
    else:
        print('NO')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
sanjiao(a,b,c)
