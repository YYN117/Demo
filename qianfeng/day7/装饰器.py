


def outer(func):
    def inner(age):
        if age < 0:
            age = 0

        func(age)
    return inner

@outer  #使用@将装饰器应用到函数，相当于say = outer(say)
def say(age):
    print('suck is %d years old'%(age))


# say = outer(say)
say(-10)