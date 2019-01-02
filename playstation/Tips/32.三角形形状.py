'''
描述:
给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W.


三边是a，b，c
假设c最大
则
c²<a²+b²，是锐角三角形
c²=a²+b²，是直角三角形
c²>a²+b²，是钝角三角形
'''

def judgement(a,b,c):
    a, b, c = sorted([a, b, c])
    if (a + b > c) :
        if (c**2 < (a**2 + b**2)):
            print('R')
        elif (c**2 == (a**2 + b**2)):
            print('Z')
        elif (c**2 > (a**2 + b**2)):
            print('D')
    else:
        print('W')

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
judgement(a,b,c)