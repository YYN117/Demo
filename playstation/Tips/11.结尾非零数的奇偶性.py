'''
给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。

例如：L=[2,8,3,50]

则输出：0
'''
two = 0
five = 0
L=[2,8,3,50]
for i in L:
    while i % 2 == 0:
        two += 1
        i = i/2
    while i % 5 == 0:
        five += 1
        i = i/5
c = min(two,five)
x = L[-(c+1)]
if x % 2 == 0:
    print('0')
if x % 2 == 1:
    print('1')
