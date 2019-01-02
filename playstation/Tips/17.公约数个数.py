def num(a,b):
    c = min(a,b)
    d = 0
    for i in range(1,c+1):
        if a % i == 0 and b % i == 0:
            d += 1
    print(d)

a = int(input('a:'))
b = int(input('b:'))
num(a,b)