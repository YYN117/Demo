def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

if __name__ == '__main__':
    lyst = [5,4,2,1,3]
    bubbleSort(lyst)
    print(lyst)