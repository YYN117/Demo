def quick(lst):
    quickSort(lst, 0, len(lst) - 1)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def quickSort(lst, left, right):
    if left < right:
        boundarty = cut(lst, left, right)
        quickSort(lst, left, boundarty - 1)
        quickSort(lst, boundarty + 1, right)

def cut(lst, left, right):
    mid = (left+right) // 2
    key = lst[mid]
    lst[mid] = lst[right]
    lst[right] = key
    boundary = left
    for index in range(left,right):
        if lst[index] < key:
            swap(lst,boundary,index)
            boundary += 1
    swap(lst, boundary, right)
    return boundary


import random
def main(size = 20,sort=quick):
    list = []
    for i in range(size):
        list.append(random.randint(-100,100))

    print(list)
    sort(list)
    print(list)

if __name__ == '__main__':
    main()
