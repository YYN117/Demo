'''
描述:
有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？
现在给你一个正整数n（0
'''

def floor():
    n = int(input('n:'))
    if  n<0:
        print('ERROR')
    else:
        if n==1 or n==2:
            print(n)
        p,q = 1,2
        for i in range(3,n+1):
            p,q = q,p+q
        print(q)

if __name__=="__main__":
    floor()
