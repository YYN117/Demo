
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

'''
格式：对象名 = 类名（参数列表）
注意:没有参数时，小括号不能省略
'''

#实例化
per1 = Person()
print(per1)

per2 = Person()
print(per2 )