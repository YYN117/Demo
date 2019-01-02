from typing import List
def merge(left:List[int],right:List[int]):
    i,j = 0,0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    tmp += left[i:]
    tmp += right[j:]
    return tmp
def merge_sort(a:List[int]):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left,right)

print(merge_sort([4,5,7,-10,21,432,-121,23,90,7,5]))