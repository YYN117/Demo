'''
描述:
给你一个列表 L, 对L进行升序排序并输出排序后的列表。

例如：L = [8,2,50,3]

则输出：[2,3,8,50]
'''

L = [8,2,50,3]
L.sort()
print(L)
print('#####')
print(sorted(L))
print(L.sort())

'''
这道题的关键在于

如果你是这样写

b = L.sort()

print(b)的话，你就会得到一个空值。

同样，如果输出print（L.sort()）

你也会得到一个空值。



而你必须写：

L.sort()

ptint(L)

才行。
'''