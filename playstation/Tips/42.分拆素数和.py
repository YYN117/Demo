'''
描述:
把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1.
'''
from math import sqrt
def su_shu_he(n):
    if not (n%2==0 and n<=10000):
        print('错了！操你妈！')
    else:
        L = []
        count = 0
        for i in range(2,n+1):
            for j in range(2,int(sqrt(i)+1)):
                if i%j == 0:
                    break
            else:
                L.append(i)

        for k in range(len(L)):
            for m in range(len(L)):
                if L[k] + L[m] == n and L[k] != L[m]:
                    # print(L[k],L[m])
                    count += 1

        print(count//2)

n = int(input('n:'))
su_shu_he(n)



