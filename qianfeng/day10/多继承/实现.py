from Child import  Child

def main():
    c = Child(300,100)
    print(c.money,c.faceValue)
    #注意：如果父类中方法名相同，默认调用括号中前面的父类方法
    c.func()

if __name__ == '__main__':
    main()