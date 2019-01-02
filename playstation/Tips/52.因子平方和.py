'''
描述:
6 的因子有 1, 2, 3 和 6, 它们的平方和是 1 + 4 + 9 + 36 = 50. 如果 f(N) 代表正整数 N 所有因子的平方和, 那么 f(6) = 50.
现在令 F 代表 f 的求和函数, 亦即 F(N) = f(1) + f(2) + .. + f(N), 显然 F 一开始的 6 个值是: 1, 6, 16, 37, 63 和 113.
那么对于任意给定的整数 N (1 <= N <= 10^8), 输出 F(N) 的值.
'''
def ping_fang_he(N):
    L = []
    while N > 0:
        for i in range(1,N+1):
            if N % i == 0:
                L.append(pow(i,2))
        N -= 1
    print(sum(L))


N = int(input('N:'))
ping_fang_he(N)