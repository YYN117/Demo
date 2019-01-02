def binary_search(target,lst):
    left = 0
    right = len(lst)-1
    while right >= left:
        # if right - left == 1:
        #     if target == lst[right] or target == lst[left]:
        #         return target
        #     else:
        #         print("can't find")
        mid = (left+right)//2
        if target == lst[mid]:
            print(mid)
        elif target < lst[mid]:
            print(mid)
            print(lst[mid])
            right = mid - 1
        else:
            print(mid)
            print(lst[mid])
            left = mid + 1
    return -1

binary_search(66,[20,44,48,55,62,66,74,88,93,99])