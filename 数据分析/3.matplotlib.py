 # coding:utf-8
#折线图，散点图 plot
import matplotlib.pylab as pyl
import numpy as npy
x = [1,2,3,4,8]
y = [5,7,2,1,5]
# pyl.plot(x,y) plot(x轴，y轴，展现的形式)  默认是折线图
# pyl.show()  折线图
# pyl.plot(x,y,'o')  #设置为o，绘制散点图
# pyl.show()
# pyl.plot(x,y,'om')   #设置散点图的颜色
# pyl.show()
'''
c   cyan    青色
r   red     红色
m   magenta     品红
g   green
b   blue
y   yellow
k   black
w   white
'''
#线条样式
'''
-   普通直线
--  虚线
-.  -.形式
:   细小虚线
'''
# pyl.plot(x,y,'og:')
# pyl.show()

'''
点的样式
s   方形
h   六角形
H   六角形
*   星形
+   加号
x   x形
d   菱形
D   菱形
p   五角形
'''
# pyl.plot(x,y,'D')
# pyl.show()

#加标题
# pyl.plot(x,y)
#同一区域绘制多条线段
x2 = [1,3,6,8,10,12,19]
y2 = [1,6,9,10,19,18,15]
# pyl.plot(x2,y2,':')
# pyl.title('show')
# pyl.xlabel('ages')
# pyl.ylabel('temp')
# #定义x轴和y轴的范围
# pyl.xlim(0,20)
# pyl.ylim(0,20)
# pyl.show()

#生成随机数
data = npy.random.random_integers(1,20,1000) #生成整数的随机数(最小值，最大值，个数)
#生成正态分布的随机数
data2 = npy.random.normal(5.0,2.0,10)     #(均数，西格玛(越小越陡峭，越大越平缓)，个数)
print(data2)

#直方图 hist
data3 = npy.random.normal(10.0,1.0,10000)
# pyl.hist(data3)
# pyl.show()
data4 = npy.random.random_integers(1,25,1000)
# pyl.hist(data4)
#设置上下限
sty = npy.arange(2,19,2)   #（起点，终点，步长）
# pyl.hist(data4,sty,histtype='stepfilled')     #histtype设置轮廓
# pyl.show()

#子图
# pyl.subplot(2,2,3)   #行，列，当前区域
# pyl.show()
pyl.subplot(2,2,1)
x1 = [1,2,3,4,5]
y1 = [5,3,5,23,5]
pyl.plot(x1,y1)

pyl.subplot(2,2,2)
x2 = [5,2,3,8,6]
y2 = [7,9,12,12,3]
pyl.plot(x2,y2)

pyl.subplot(2,1,2)
x3 = [5,6,7,10,19,20,29]
y3 = [6,2,4,21,5,1,5]
pyl.plot(x3,y3)
pyl.show()