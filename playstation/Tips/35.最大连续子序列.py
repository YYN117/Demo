'''
描述:
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).
'''
#笨办法
L = [2,-3,3,50]
s = []
for i in range(len(L)+1):
    for j in range(i,len(L)+1):
        a = sum(L[i:j])
        s.append(a)
print(max(s))
