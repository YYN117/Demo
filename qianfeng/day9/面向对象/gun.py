class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox = bulletBox
    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print('None')
        else:
            self.bulletBox.bulletCount -= 1
            print('剩余%d发'%(self.bulletBox.bulletCount))