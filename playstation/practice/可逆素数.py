from math import sqrt
def prime():
    l = []
    for i in range(2,101):
        for j in range(2,int(sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            l.append(i)
    L = [2,3,5,7]
    for k in range(4,len(l)):
        a = int(str(l[k])[::-1])
        if a in l:
            L.append(a)
    x = ' '.join(map(str,L))
    print(x)
if __name__ == '__main__':
    prime()