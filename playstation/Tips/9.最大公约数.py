'''
描述:
给你两个正整数a和b， 输出它们的最大公约数。

例如：a = 3, b = 5

则输出：1
'''

def gongyueshu(a,b):
    c = min(a,b)
    for i in range(1,c+1):
        if(a % i == 0) and (b % i == 0):
            gys = i
    return  gys

a = int(input('输入第一个：'))
b = int(input('输入第二个：'))

print('最大公约数是:',gongyueshu(a,b))