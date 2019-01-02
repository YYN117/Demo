
def group_by_element(lst):
    a = [[]]
    l = len(lst)
    for i in range(l):
        if i<l-1:
            if lst[i] == lst[i+1]:
                a[-1].append(lst[i])
            else:
                a[-1].append(lst[i])
                a.append([])
    a[-1].append(lst[i])
    return a



if __name__ == '__main__':
    list = [0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 0, 0]
    group = group_by_element(list)
    print(group)