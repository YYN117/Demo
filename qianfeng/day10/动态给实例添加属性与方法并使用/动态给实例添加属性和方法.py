from types import MethodType

# 创建一个空类
class Person(object):
    __slots__ = ('name','age','speak')

per = Person()
#动态添加属性，体现了动态语音的灵活特点
per.name = 'Tom'
print(per.name)
#动态添加方法
'''
def say(self):
    print('my name is '+ self.name)
per.speak = say
per.speak(per)
'''

def say(self):
        print('my name is '+ self.name)
per.speak = MethodType(say,per)
per.speak()

#思考：如果想限制实例的属性该怎么办？
#例如：只允许给对象添加name，age，height，weight属性

#解决：定义类的时候，定义一个特殊的属性（__slots__）,可以限制动态添加的属性

# per.height = 180
# print(per.height)