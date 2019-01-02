'''
描述:
给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。
如a=3, b =4, 则输出5.000。
'''
import math
def google(a,b):
    c = math.sqrt(pow(a,2)+pow(b,2))
    print('{:.3f}'.format(c))
    print('%.3f'%c)

a = int(input('a:'))
b = int(input('b:'))
google(a,b)