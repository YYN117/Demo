
class Person(object):
    #这里的属性实际上属性类属性（用类名来调用）
    name = 'person'
    def __init__(self,name):
        #对象属性
        self.name = name

print(Person.name)
per = Person('tom')
#对象属性的优先级高于类属性
print(per.name)
#动态的给对象添加对象属性
per.age = 18 #只针对当前的对象生效，对于类创建的其他对象无效
print(Person.name)

#删除对象中的name属性，再调用会使用类属性（如果存在的话）
del per.name
print(per.name)

#注意：不要将对象属性与类属性重名，因为对象属性会屏蔽类属性，但当删除对象属性后，再使用则会属于类属性
