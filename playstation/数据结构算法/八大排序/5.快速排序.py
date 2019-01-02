#
# def top(lst):
#     quicksort(lst,0,len(lst)-1)
#
# def exc(lst,i,j):
#     t = lst[i]
#     lst[i] = lst[j]
#     lst[j] = t
#
# def quicksort(lst,left,right):
#     if left < right:
#         location = findkey(lst,left,right)
#         quicksort(lst,left,location-1)
#         quicksort(lst,location+1,right)
#
# def findkey(lst,left,right):
#     mid = (right + left)//2
#     key = lst[mid]
#     # lst[mid] = lst[right]
#     # lst[right] = key
#     lst[mid],lst[right] = lst[right],lst[mid]
#     boundary = left
#     for index in range(left,right):
#         if lst[index] < key:
#             exc(lst,index,boundary)
#             boundary += 1
#     # exc(lst,right,boundary)
#     exc(lst,boundary,right)
#     return boundary
#
# import random,time
#
# def main(num = 100,sort = top):
#     a = time.time()
#     list = []
#     for i in range(num):
#         list.append(random.randint(1,num+1))
#         # list.append(random.sample(range(1,500000),num))
#
#     print(list)
#     sort(list)
#     print('**************************************************')
#     print(list)
#     b = time.time()
#     t = b-a
#     print(t)
#
# if __name__ == '__main__':
#     main()

from typing import List

def start(list: List[int]):
    quicksort(list, 0, len(list)-1)

def swap(list: List[int], i, j):
    list[i], list[j] = list[j], list[i]

def quicksort(list: List[int], left, right):
    if left < right:
        location = find(list, left, right)
        quicksort(list, left, location-1)
        quicksort(list, location+1, right)

def find(list: List[int], left, right):
    mid = (left + right) // 2
    key = list[mid]
    list[mid] = list[right]
    list[right] = key
    boundary = left
    for index in range(left, right):
        if list[index] < key:
            swap(list, index, boundary)
            boundary += 1
    swap(list, boundary, right)
    return boundary

import random, time

def main(num=100, sort=start):
    a = time.time
    list = []
    for i in range(num):
        list.append(random.randint(-100, 100))
    print(list)
    sort(list)
    print(list)

if __name__ == '__main__':
    main()