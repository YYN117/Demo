class PrintTable():
    def __init__(self):
        print('倒置乘法表')
        self.chengfa()
    def chengfa(self):
        for i in range(9,-1,-1):
            for j in range(1,i+1):
                print('{}*{}={}'.format(i,j,i*j),end=' ')
            print('\n')

if __name__ == '__main__':
    PrintTable()
