from person import Person
class Student(Person):
    def __init__(self,name,age,stuId):
        #调用父类中的__init__
        super(Student,self).__init__(name,age)
        #子类可以有自己的属性
        self.stuId = stuId
