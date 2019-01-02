'''
如果 a + b + c = 1000,且 a^2 + b^2 = c^2 (a,b,c为自然数),如何求出所有a,b,c的组合？
'''
#枚举法（蠢）
# import time
# start_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a+b+c == 1000 and a**2 + b**2 == c**2:
#                 print('a = {},b = {},c = {}'.format(a,b,c))
# end_time = time.time()
# print('timecost:{:.2f}'.format(end_time - start_time))
#耗时 = 143 秒

'''
时间复杂度 T = 1000 * 1000 * 1000 * 2
若1000换为N
则 T = N * N * N * 2   即  T(n) = n^3 * 2
大O法： 复杂度为 n^3
'''

#改进！！！！！！！！！！！！
#当a,b已知后，c = 1000 - a -b
import time
start_time = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        if  a**2 + b**2 == c**2:
            print('a = {},b = {},c = {}'.format(a,b,c))
# 没台机器执行的总时间不同，但执行基本运算数量大体相同
end_time = time.time()
print('timecost:{:.2f}'.format(end_time - start_time))
#耗时 1.33 秒
'''
T(n) = n * n * ( 1 + max(1,0))
     = n^2 * 2
     = O(n^2) 
'''