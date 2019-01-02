def bubbleSort(lyst):
    n = len(lyst)
    for i in range(n):
        for j in range(i+1,n):
            if lyst[i] > lyst[j]:
                lyst[i],lyst[j]=lyst[j],lyst[i]
    return lyst

if __name__ == '__main__':
    lyst = [5,4,2,1,3]
    bubbleSort(lyst)
    print(lyst)