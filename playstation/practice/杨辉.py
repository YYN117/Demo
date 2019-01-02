def yang_hui():
    global n
    n = int(input('n:'))
    l = [1]
    while True:
        yield l
        s = [l[i]+l[i+1] for i in range(len(l)-1)]
        l = [1]+s+[1]

res = []
t = 0
for i in yang_hui():
    y = list(map(str,i))
    x = ' '.join(y)
    print(x)
    t += 1
    if t == n:
        break
