'''
给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。

若存在，输出Yes,否则输出No

例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。
'''
def ANS(a,b):
    for x in range(-10000,max(abs(a),abs(b))+1):
        if x*(a-x) == b:
            print('Yes')
            break
        elif x == max(abs(a),abs(b)):
            print('No')
            break

a = int(input('a:'))
b = int(input('b:'))
ANS(a,b)

