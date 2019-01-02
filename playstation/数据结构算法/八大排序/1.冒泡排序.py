# -*-coding:utf-8-*-

def bubbleSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for j in range(len(sorted_list)):
        for i in range(j+1,len(sorted_list)):
            if sorted_list[i] < sorted_list[j]:
                sorted_list[i],sorted_list[j] = sorted_list[j],sorted_list[i]

    return sorted_list
    # sorted_list = input_list
    # n = len(sorted_list)
    # for i in range(n-1):
    #     print('第{}次排序'.format(i+1))
    #     for j in range(n-1):
    #         if sorted_list[j+1] < sorted_list[j]:
    #             sorted_list[j+1],sorted_list[j] = sorted_list[j],sorted_list[j+1]
    #         print(sorted_list)
    # return  sorted_list

if __name__ == '__main__':
    input_list = list(eval(input('请输入列表：')))
    print('排序前：',input_list)
    sorted_list = bubbleSort(input_list)
    print('排序后：',sorted_list)