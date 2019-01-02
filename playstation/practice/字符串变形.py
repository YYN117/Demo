# -*- coding:utf-8 -*-
def trans(s, n):
    # write code here
    a = s.split(' ')
    a.reverse()
    b = []
    for i in a:
        if len(i)==1:
            if 65 <= ord(i) <= 90:
                b.append(chr(ord(i) + 32))
            elif 97 <= ord(i) <= 122:
                b.append(chr(ord(i) - 32))
        else:
            c = []
            for j in i:
                if 65 <= ord(j) <= 90:
                    c.append(chr(ord(j) + 32))
                elif 97 <= ord(j) <= 122:
                    c.append(chr(ord(j) - 32))
            b.append(''.join(c))
    d = ' '.join(b)
    print(d)
trans("This is a sample",16)
