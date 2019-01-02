import random,sys
# sys.setrecursionlimit(1000000)

def GetNum(num):
    list = []
    for i in range(num):
        list.append(random.randint(0,100))
    return list

def quickSort(list):
    n = len(list)
    if n <= 1:
        return list
    mid = random.randint(0,n-1)
    key = list[mid]
    right = []
    left = []
    for i in range(n):
        if list[i] > key:
            right.append(list[i])
        else:
            left.append(list[i])

    a = quickSort(left)
    b = quickSort(right)
    return a+b

if __name__ == '__main__':
    # num = eval(input('>>>'))
    a = GetNum(10)
    b = quickSort(a)
    print(a)
    print('**************')
    print(b)