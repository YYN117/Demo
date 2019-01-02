from functools import reduce

def str2float(s):
    i = s.index('.')
    s = s[:i]+s[i+1:]
    return reduce(func,map(dicNum,s))/(10**i)

def dicNum(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
    return DIGITS[s]

def func(x,y):
    return x*10+y


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')







