# -*-coding:utf-8-*-

def insertSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    n = len(sorted_list)

    for i in range(1,n):
        pass


if __name__ == '__main__':
    input_list = list(eval(input('输入列表：')))
    print('排序前:', input_list)
    sorted_list = insertSort(input_list)
    print('排序后:', sorted_list)
