'''
描述:
给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。

例如： L=[2,8,3,50],

则输出：2
'''

# num = 1
two = 0
five = 0
L=[2,8,3,50]
# for i in range(len(L)):
#     num*=L[i]
for i in L:
    while i % 2 == 0:
        two += 1
        i = i/2
    while i % 5 == 0:
        five += 1
        i = i/5
print(min(two,five))
