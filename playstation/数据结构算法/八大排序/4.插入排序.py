def insertSort(lst):
    i = 1
    while i < len(lst):
        item = lst[i]
        j = i - 1
        while j >= 0:
            if item < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            else:
                break
        lst[j+1] = item
        i += 1
if __name__ == '__main__':
    lst = [5,6,4,9,2,1,0,3]
    insertSort(lst)
    print(lst)