
class Person(object):
    name = ''
    age = 0
    height = 0
    weight = 0

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


'''
格式：对象名 = 类名（参数列表）
注意:没有参数时，小括号不能省略
'''

#实例化
per = Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''
per.name = 'tom'
per.age = 18
per.height = 160
per.weight = 80
print(per.name,per.age,per.height,per.weight)

'''
访问方法
格式:对象名.方法名(参数列表)
'''
per.openDoor()
per.fillEle()
per.closeDoor()
per.eat(' apple')