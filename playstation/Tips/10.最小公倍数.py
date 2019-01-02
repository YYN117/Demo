'''
描述:
给你两个正整数a和b， 输出它们的最小公倍数。

例如：a = 3, b = 5

则输出：15
'''

def gongbeishu(a,b):
    c = max(a,b)
    while True:
        if (c % a == 0) and (c % b == 0):
            gbs = c
            break
        else:
            c += 1
    return  c

a = int(input('输入第一个数字：'))
b = int(input(('请输入第二个数字：')))
print('最小公倍数是',gongbeishu(a,b))