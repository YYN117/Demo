def selectionSort(L):
    i = 0
    while i < len(L)-1:
        minIndex = i
        for j in range(i + 1,len(L)):
            if L[j] < L[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            L[minIndex],L[i] = L[i],L[minIndex]
        i += 1

if __name__ == '__main__':
    L = [5,3,1,2,4]
    selectionSort(L)
    print(L)

