# coding:utf-8
import matplotlib.pylab as pyl
import numpy as npy
import pandas as pda
i = pda.read_excel(r'C:\Users\Jhon117\Desktop\demo\爬虫实战\京东苹果手机商品信息.xls')
print(i.describe())
# print(i.shape)
# print(i.values)
# print(i.values[0][1])
a = i.T
x1 = a.values[0]
y1 = a.values[1]
pyl.plot(x1,y1)
pyl.title('JD')
pyl.xlabel('Num')
pyl.ylabel('price')
pyl.show()



