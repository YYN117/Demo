'''
1.定义一个函数，参数为一个字符串（全部由小写英文字母组成），找出一个拆分位置，该位置满足拆分后的两个子字符串（每个字符串至少有一个字符）中相同的字符（包括重复的）最多；如有多个位置满足条件则取第一个。如输入的字符串为“helloworld“，则可能拆分的结果如下表，所以找到的拆分位置为5
拆分位置	左半	右半	相同字符数量
1	h	elloworld	0
2	he	lloworld	0
3	hel	loworld	2
4	hell	oworld	2
5	hello	world	3
6	hellow	orld	3
7	hellowo	rld	2
8	hellowor	ld	2
9	helloworl	d	0
2.接受用户输入的字符串，然后调用该函数进行测试
'''
def chai_fen():
    L = []
    x = input('输入字符串(小写)：')
    for i in range(1,len(x)):
        a = x[:i]
        b = x[i:]
        count = 0
        print(a,b)
        for j in a:
            for k in b:
                if j == k:
                    count += 1
        L.append(count)
    print(L)
    m = L.index(max(L))+1
    print(m)
if __name__ == "__main__":
    chai_fen()