'''
原型：filter(fn,1sd)
参数1为函数
参数2为序列

功能：用于过滤序列
即：把传入的函数依次作用于序列的每个元素，根据返回的是True还是False决定是否保留该元素

'''

list1 = [1,2,3,4,5,6,7,8,9]
#筛选条件
def func(num):
    #偶数保留
    if num%2 == 0:
        return True
    #奇数去除
    return False
l = filter(func,list1)
print(list(l))