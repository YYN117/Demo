

'''
递归调用：一个函数，调用自身，称为递归调用
递归函数：一个会调用自身的函数

循环能做的，递归也能做
'''

'''
方式：

1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数可用，调用自身计算上一次结果，再求出本次的结果
'''

#输入一个数（>=1），求1+2+3+...+n
def sum1(n):
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

'''
1+2+3+4+5
sum2(1)+2 = sum2(2)
sum2(2)+3 = sum2(3)
'''
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)
res = sum2(5)
print('res = ',res)