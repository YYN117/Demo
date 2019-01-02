class PrintTable():
    def __init__(self):
        print('乘法表')
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('{}x{}={}'.format(j,i,i*j),end=' ')
            print('\n')


if __name__ == '__main__':
    pt = PrintTable()