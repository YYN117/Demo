import random

class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = input('输入测试次数：')
            try:
                num = int(numStr)
            except:
                print('输入整数')
                continue
            else:
                break

        ball = [0,0,0,0,0,0,0,0,0,0]
        for i in range(num):
            n = random.randint(1,10)
            ball[n-1]+=1
        for i in range(1,11):
            print('第{}号球出现的概率为{}'.format(i,(ball[n-1])/num))

if __name__ == '__main__':
    SB = SelectBall()