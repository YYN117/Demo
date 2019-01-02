def findSmallest(lst):
    smallest = lst[0]
    smallest_index = 0
    for i in range(1,len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index

def sortLst(lst):
    new = []
    for i in range(len(lst)):
        smallest_index = findSmallest(lst)
        new.append(lst.pop(smallest_index))
    print(new)

if __name__ == '__main__':
    L = [5,3,1,2,4,0,-1]
    sortLst(L)
