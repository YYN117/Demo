def createCounter():
    global n
    n = 0
    def counter():
        global n
        n += 1
        return n
    return counter

# def createCounter():
#     def f(n):
#         def counter():
#             return n+1
#         return counter
#     fs = []
#     for i in range(10):
#         fs.append(f(i))
#     return fs

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')