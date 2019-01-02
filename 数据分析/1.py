# coding:utf-8
'''
import numpy
#创建一维数组格式
# numpy.array(['元素1','元素2',...,'元素n'])
x = numpy.array(['a','9',1,10])
print(x)
print(x[3])
print(type(x[3]))

#创建二维数组
#numpy.array([[],[],[],...,[]])
y = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(y)

#排序sort()
x.sort()
print(x)
print(type(x))
print('************')
x=sorted(x)
print(x)
print(type(x))
'''

'''pandas'''
import pandas as pda
'''
Series、DataFrame
'''
a = pda.Series([8,9,2,1])
print(a)
b = pda.Series([8,9,2,1],index=['one','two','three','four'])
print(b)
c = pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]]) #数据框
print(c)
d = pda.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]],columns=["one",'two','three','four'],index=['I','II','III'])
print(d)
e = pda.DataFrame({
    'one':4,'two':[6,2,3],'three':list(str(982))
})
print(e)
d.head() #调取头部数据，默认是前5行
print(d.head(2))
d.tail() #尾部数据，默认后5行
print(d.tail(2))
print(d.describe()) #按列统计
#转置
print(d.T)