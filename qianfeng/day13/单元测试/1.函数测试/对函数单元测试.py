'''
单元测试:
作用：用来对一个函数、一个类或一个模块进行正确性校验工作

结果：
1、单元测试通过，说明测试的函数功能正常
2、单元测试不通过，说明函数功能有BUG，或者测试条件输入有误

'''
def mySum(x,y):
    # x += 1
    return x + y

def mySub(x,y):
    return x - y

print(mySum(1,2))