'''
重写:将函数重新定义写一遍
__str__()：在调用print打印对象时自动调用，是给用户使用的，是一个描述对象的方法。
__repr__()：是给机器用的，在python解释器中直接敲对象名再回车后调用的方法
注意：无str时且有repr时，repr=str

'''
class Person(object):
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return '%s-%d-%d-%d'%(self.name,self.age,self.height,self.weight)

per = Person('hanmeimei',20,170,55)
print(per)

#特点：当一个对象属性值很多，且都需要打印，重写了__str__方法后，简化了代码