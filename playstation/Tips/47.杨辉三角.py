'''
描述:
还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
..............
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如n=2,则输出：
1
1 1
'''
# L = [1]
# # s = [L[i]+L[i+1] for i in range(len(L)-1)]
# # print(s)
# s=[]
# for i in range(len(L)-1):
#     s.append(L[i]+L[i+1])
#     print(L[i]+L[i+1])
# # print(s)

n = int(input('n:'))
def yang_hui():
    L = [1]
    while True:
        yield L
        s = [L[i]+L[i+1] for i in range(len(L)-1)]
        L = [1] + s + [1]

res = []
t = 0
for i in yang_hui():
    y = list(map(str,i))
    x = ' '.join(y)
    x = x.center(100)
    print(x)
    t += 1
    if t == n:
        break

