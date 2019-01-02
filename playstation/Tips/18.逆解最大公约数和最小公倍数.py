'''
描述:
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。注：所给数据都有解，不用考虑无解的情况。

例如：a=3, b = 60

则输出：12 15


!!!!!!!!!!   X,Y的最大公约数*最小公倍数=X*Y    !!!!!!!!!!!!!!!
'''
def nijie(a,b):
    sum = a*b
    for i in range(min(a,b),max(a,b)+1):
#公约数
        if i % a == 0 and b % i == 0 :
            y = (a*b)/i
            if sum > (y+i):
                sum = y + i
                min1 = i
                min2 = y
    if min1 > min2:
        print(int(min2),int(min1))
    else:
        print(int(min1),int(min2))

a = int(input('a:'))
b = int(input('b:'))
nijie(a,b)