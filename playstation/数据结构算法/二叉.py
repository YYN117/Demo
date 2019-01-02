'''
索引0到9，包含值20,44,48,55,62,66,74,88,93,99
搜索90,44
'''
def binarySearch():
    L = eval(input('输入列表：'))
    target = eval(input('输入查找值：'))
    left = 0
    right = len(L)-1
    while left <= right:
        mid = (left + right)//2
        print('左{}，右{}，中{}'.format(left,right,mid))
        if target == L[mid]:
            return mid
        elif target < L[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == '__main__':
    binarySearch()
