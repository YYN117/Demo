from card import Card
from user import User
import random
class ATM(object):
    def __init__(self):
        self.allUsers = {}
    def createUser(self):
        #目标：向用户字典中添加键值对
        name =input('输入姓名：')
        idCard = input('输入ID：')
        phone =input('输入电话：')
        prestoreMoney = int(input('输入预存款金额:'))
        if prestoreMoney < 0:
            print('预存款输入有误，开户失败....')
            return  -1
        onePasswd = input('请设置密码')
        #验证密码
        if not self.checkPasswd(onePasswd):
            print('开户失败')
            return 1

        cardStr = self.randomCardId()
        card = Card(cardStr,onePasswd,prestoreMoney)
        user = User(name,idCard,phone,card)
        #存到字典
        self.allUsers[cardStr] = user
        print('开户成功:%s'%(cardStr))
    def searchUserInfo(self):
        cardNum = input('输入卡号：')
        user = self.allUsers.get(cardNum)
        if not user:
            print('不存在')
            return -1
        if user.card.cardLock:
            print('已锁定')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码错误,已锁定')
            user.card.cardLock = True
            return -1
        print('账号：%s   余额：%d'%(user.card.cardId,user.card.cardMoney))
    #取款
    def getMoney(self):
        pass
    #存款
    def saveMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    def changePasswd(self):
        pass
    def lockUser(self):
        cardNum = input('输入卡号：')
        user = self.allUsers.get(cardNum)
        if not user:
            print('不存在')
            return -1
        if user.card.cardLock:
            print('已锁定')
            return  -1
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码错误,锁失败')
            return -1
        tempIdCard = input('输入ID：')
        if tempIdCard != user.idCard:
            print('身份证错误，锁定失败')
            return  -1

        user.card.cardLock = True
        print('已锁定')

    def unlockUser(self):
        cardNum = input('输入卡号：')
        user = self.allUsers.get(cardNum)
        if not user:
            print('不存在')
            return -1
        if not user.card.cardLock:
            print('未锁定')
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print('密码错误,解锁失败')
            return -1
        tempIdCard = input('输入ID：')
        if tempIdCard != user.idCard:
            print('身份证错误，解锁失败')
            return  -1

        user.card.cardLock = False
        print('解锁成功')
    def newCard(self):
        pass
    def KillUser(self):
        pass

    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input('输入密码：')
            if tempPasswd == realPasswd:
                return True
        return False

    #生成卡号
    def randomCardId(self):
        while True:
            str = ''
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str


