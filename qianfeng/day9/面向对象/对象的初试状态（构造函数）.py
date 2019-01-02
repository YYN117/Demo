
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
    def openDoor(self):
        print('打开冰箱门')
    def fillEle(self):
        print('放进去')
    def closeDoor(self):
        print('关门')
    def __init__(self,name,age,height,weight):
        # print(name,age,height,weight)
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

        pass

'''
构造函数:__init__()  在使用类创建对象时自动调用
注意：如果不写出构造函数，则会默认自动添加一个空的构造函数
'''
per = Person('JHON',20,189,80)
print(per.name,per.age,per.height,per.weight)
per1 = Person('117',30,179,55)
print(per1.name,per1.age,per1.height,per1.weight)