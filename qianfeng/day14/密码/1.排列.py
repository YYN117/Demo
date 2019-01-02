import itertools

'''
1 2 3 4 中拿出3个数
'''
mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))

'''
从n个数字中选出m个：
4选3: 24种
4选2: 12种
4选1:  4种

可能性次数：n!/(n-m)!
'''