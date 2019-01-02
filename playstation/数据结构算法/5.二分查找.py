# coding:utf-8
def binary_search(ls, key):
    low, high = 0, len(ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if ls[mid] == key:
            return mid
        elif ls[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#递归
def binary_digui(ls, low, high, key):
    while low <= high:
        mid = low + ((high - low) >> 1)
        if ls[mid] == key:
            return mid
        elif ls[mid] < key:
            return binary_digui(ls, mid + 1, high, key)
        else:
            return binary_digui(ls, low, mid - 1, key)
    return -1

print(binary_digui([-12,6,2,3,4,5,6,7,8,9,14,90],0,11,6))