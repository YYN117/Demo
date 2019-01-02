'''
self代表类的实例，不是类
哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__ 代表类名
'''
class Person(object):
    # name = ''
    # age = 0
    # height = 0
    # weight = 0

    #定义方法（定义函数）
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def say(self):
        print("Hello! my name is %s, I am %d years old" %(self.name,self.age))
        print(self.__class__)
        p = self.__class__('tt',30,10,20)
        print(p)

    #self不是关键字，使用其他标识符亦可
    def play(a):
        print('play')
    def __init__(self,name,age,height,weight):
        # print(name,age,height,weight)
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person('tom',20,160,80)
per1.say()
