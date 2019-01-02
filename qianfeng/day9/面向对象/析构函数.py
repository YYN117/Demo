
'''
析构函数：__del__() 释放对象是自动调用


'''

class Person(object):
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def __init__(self,name,age,height,weight):
        # print(name,age,height,weight)
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print('析构')

per = Person('hanmeimei',20,170,55)
#释放对象
del per

#对象释放以后无法访问
# print(per.age)

#在函数中定义的对象，会在函数结束时自动释放，这样可以减少内存空间的浪费
def func():
    per2 = Person('aa',1,1,1)

func()

while 1:
    pass