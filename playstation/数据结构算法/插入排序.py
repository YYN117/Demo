
def insertionSort(lyst):
    n = len(lyst)
    for i in range(1,n):
        j = i-1
        while j >= 0:
            if lyst[i] < lyst[j]:
                lyst[j+1],lyst[j] = lyst[j],lyst[i]
            j -= 1
    return lyst

if __name__ == '__main__':
    lyst = [2, 5, 1, 4, 3]
    insertionSort(lyst)
    print(lyst)

