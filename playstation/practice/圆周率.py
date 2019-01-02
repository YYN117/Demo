import itertools as it
'''
itertools.takewhile(predicate, iterable)
和dropwhile相反

创建一个迭代器，生成iterable中predicate(item)为True的项，只要predicate计算为False，迭代就会立即停止。

即：从序列的头开始, 直到执行函数func失败.
'''
def pi(N):
    natuals =  it.count(1,2)
    odd = it.takewhile(lambda x:x<=2*N-1,natuals)
    odd = map(lambda x:(-1)**(x//2)*(4/x),odd)
    return sum(odd)

# if __name__ == '__main__':
#     N = int(input('输入：'))
#     print(pi(N))
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')