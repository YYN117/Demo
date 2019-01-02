import  itertools


mylist = list(itertools.combinations([1,2,3,4,5],4))
print(mylist)
print(len(mylist))

'''
5选4  5种
5选3  10种
5选2  10种
5选5  1种

次数：n!/（m!*（n-m）！）

'''