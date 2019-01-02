# -*- coding: utf-8 -*-
def start(list):
    quick(list,0,len(list)-1)

def exchange(list,i,j):
    t = list[i]
    list[i] = list[j]
    list[j] = t

def quick(list,left,right):
    if left < right:
        key = cut(list,left,right)
        quick(list,left,key-1)
        quick(list,key+1,right)

def cut(list,left,right):
    mid = (left + right) // 2
    #确定分割点并与最后一项进行交换
    key = list[mid]
    list[mid] = list[right]
    list[right] = key
    #将边界调整至第一项
    boundary = left
    #进行比较，小于分割值的前移
    for index in range(left,right):
        if list[index] < key:
            exchange(list,index,boundary)
            boundary += 1
    #交换key和边界
    exchange(list,right,boundary)
    return boundary

import random

def main(size = 50,sort = start):
    list = []
    for count in range(size):
        list.append(random.randint(-100,100))

    print(list)
    sort(list)
    print(list)

if __name__ == '__main__':
    main()