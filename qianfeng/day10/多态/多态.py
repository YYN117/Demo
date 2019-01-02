'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物
'''
from cat import Cat
from  mouse import Mouse
from person import Person
tom = Cat('tom')
jerry = Mouse('Jerry')

# tom.eat()
# jerry.eat()

#思考：添加100种动物，都有name属性和eat方法
#定义了一个有name属性和eat方法的Animal类，让动物继承自Animal

#定义一个人类，可以喂猫和老鼠吃东西
per = Person()
per.feedAnimal(tom)
