'''
一、整数的二进制比较：
1.定义一个函数，参数为一个整数列表，返回该列表中整数的二进制中1最多的整数（如果数量相同，则返回第一个）
如：整数列表为[45,23,12,7]，则对应的二进制为[101101,10111,1100,0111]，前两个的1数量相同，则返回值为45
2.自行定义一个整数列表，然后调用该函数进行测试
'''
def bi_jiao():
    a_list = eval(input("请输入整数列表:"))
    l = []
    for i in a_list:
        a = bin(i).split('b')
        l.append(a[1])
    for j in l:
        L = []
        L.append(j.count('1'))
    m = L.index(max(L))
    print(a_list[m])

if __name__ == '__main__':
    bi_jiao()