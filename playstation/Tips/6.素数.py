'''
描述:
输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
'''

'''
基本判断思路
在一般领域，对正整数n，如果用2到n之间的所有整数去除，均无法整除，则n为质数。
质数大于等于2 不能被它本身和1以外的数整除
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
        return True
'''
# from math import sqrt
# l = []
# for i in range(2,101):
#     for j in range(2,int(sqrt(i)+1)):
#         if i%j == 0:
#             break
#     else:
#         l.append(i)
# print(' '.join(map(str,l)))

# num = 2
# count = 0
#
# while num < 100:
#     flag = 1
#     i = 2
#     while num>i:
#         if num % i == 0:
#             flag = 0
#             break
#         i += 1
#     if flag == 1:
#         count += 1
#         print(num,end=' ')
#     num +=1
# print(count,end='\n')


from math import sqrt
l = []
count = 0
for i in range(2,101):
    for j in range(2,int(sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        l.append(i)
        count += 1
print(' '.join(map(str,l)))
print(count)