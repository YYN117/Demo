class SchoolMember:
    count = 0
    def __init__(self,name):
        self.name = name
        SchoolMember.count += 1
        print('name {}'.format(self.name))
        print('count {}'.format(SchoolMember.count))
    def introduce(self):
        print('My name is {}'.format(self.name))
    def __del__(self):
        SchoolMember.count -= 1
        print('{} leave, count is {}'.format(self.name,SchoolMember.count))

class Teacher(SchoolMember):
    def __init__(self,name,salary):
        SchoolMember.__init__(self,name)
        self.salary = salary
    def introduce(self):
        SchoolMember.introduce(self)
        print('I am a teacher,salary is {}'.format(self.salary))
    def __del__(self):
        SchoolMember.__del__(self)

class Student(SchoolMember):
    def __init__(self,name,mark):
        SchoolMember.__init__(self,name)
        self.mark = mark
    def introduce(self):
        SchoolMember.introduce(self)
        print('I am a student, mark is {}'.format(self.mark))
    def __del__(self):
        SchoolMember.__del__(self)
t = Teacher('大桥未久',16461651)
t.introduce()
s = Student('杨雨诺',98)
s.introduce()
