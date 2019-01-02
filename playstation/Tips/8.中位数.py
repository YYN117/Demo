'''
描述:
给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。

例如： L=[0,1,2,3,4]

则输出：2

'''
L=[0,1,2,3]
L = sorted(L)
size = len(L)
if size%2 == 1:
    print(L[(size-1)//2])
if size%2 == 0:
    a = (L[size//2]+L[size//2-1])/2.0
    print('%.1f'%a)