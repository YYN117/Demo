#排序：冒泡，选择    快速，插入，计数器

#普通排序
list1 = [4,7,2,6,3]
list2 = sorted(list1) #默认升序排序
print(list1)
print(list2)

#按绝对值大小
list3 = [4,-7,2,6,-3]
#key接收函数来实现自定义排序规则
list4 = sorted(list3,key=abs)#默认升序排序
print(list3)
print(list4)

#降序
list5 = [4,7,2,6,3]
list6 = sorted(list5,reverse=True)
print(list5)
print(list6)


list7 = ['b333','a11111111','c22','d5554']
def myLen(str):
    return len(str)
list8 = sorted(list7,key=myLen) #默认升序排序
print(list7)
print(list8)