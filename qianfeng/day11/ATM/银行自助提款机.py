'''
人
类名：Person
属性：姓名，身份证，电话，卡
行为

卡
类名：Card
属性：卡号，密码，余额
行为

提款机
类名：ATM
属性：
行为：开户，查询，取款，存款，转账，改密码，锁定，解锁，读卡，销户，退出

界面类
类名：View
属性：
行为：管理员界面  管理员登录 系统功能界面
'''
from view import View
from atm import ATM
import time
import pickle
import os
def main():
    #用户数据
    allUsers = {}
    #界面
    view = View()
    view.printAdminView()
    #管理员开机
    if view.adminOption():
        return -1
    filepath = os.path.join(os.getcwd(), 'allusers.txt')

    f = open(filepath ,'rb')
    allUsers = pickle.load(f)
    print(allUsers)

    atm = ATM(allUsers)

    while True:
        view.printSysFunctionView()
        #等待用户操作
        option = input('输入你的操作：')
        if option == '1':
            atm.createUser()
        elif option == '2':
            atm.searchUserInfo()
        elif option == '3':
            print('取款')
        elif option == '4':
            print('存款')
        elif option == '5':
            print('转账')
        elif option == '6':
            print('改密')
        elif option == '7':
            atm.lockUser()
        elif option == '8':
            atm.unlockUser()
        elif option == '9':
            print('补卡')
        elif option == '0':
            print('销户')
        elif option == 't':
            if not view.adminOption():
                f = open(filepath,'wb')
                pickle.dump(atm.allUsers,f)
                f.close()
                print(filepath)
                return -1

        time.sleep(2)


if __name__ == '__main__':
    main()