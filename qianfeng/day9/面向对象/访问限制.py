class Person(object):
    def run(self):
        print(self.__money)
        print('run')
    def eat(self,food):
        print('eat'+food)
    def __init__(self,name,age,height,weight,money):
        # print(name,age,height,weight)
        #定义属性
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money
    #通过内部的方法，修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):
        #数据的过滤
        if money < 0 :
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money
    
per = Person('hanmeimei',20,170,55,100000)
# per.age = 10
# print(per.age)
#若要内部的属性不被外部直接访问,在属性前加两个下划线__，在python中如果在属性前加2个下划线，则该属性变成了私有属性（private）
#print(per.__money) 外部使用
per.run()  #内部可以使用

#不能直接访问__money的原因是因为python解释器将__money变成了_Person__money，虽然可以用_Person__money访问，但是不建议
per._Person__money = 1
print(per.getMoney())

#在python中  __XXX__ 属于特殊变量，可以直接访问
print(per.__age__)

#在python中 _XXX变量，这样的实例变量在外部也可以访问,但是按照约定的规则，当我们看到这样的变量时，其意思为：虽然可以被访问，但应视为私有，不要访问
print(per._height)