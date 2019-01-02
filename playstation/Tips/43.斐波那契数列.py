'''
描述:
斐波那契数列为1,1,2,3,5,8...。数列从第三项起满足，该项的数是其前面两个数之和。现在给你一个正整数n（n < 10000), 请你求出第n个斐波那契数取模20132013的值（斐波那契数列的编号从1开始）。

例如：

n=1, 则输出：1

n=4, 则输出：3
'''
def fei_bo_na_qi(n):
    if n==0 or n==1:
        return 1
    p,q = 1,1
    for i in range(2,n+1):
        p,q = q,p+q
    return q

n = int(input('n:'))-1
print(fei_bo_na_qi(n)%20132013)