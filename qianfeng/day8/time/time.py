'''
UTC(世界协调时间)
DST(夏令时)

时间的表示形式：
1、时间戳   以整型或浮点型表示时间的一个以秒为单位的时间间隔。时间间隔的基础值从1970年1月1日0点算
2、元组   一种pythond的数据结构表示，元组有9个整型内容
          year  month day hours minutes seconds weekd Julia-day  flag（1或-1或0）
3、格式化字符串

'''
import time
#返回当前时间的时间戳，浮点数形式，无需参数
c = time.time()
print(c)

#将时间戳作为UTC时间元祖
t = time.gmtime(c)
print(t)
#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)

#将本地时间元组转为时间戳
m = time.mktime(b)
print(m)

#将时间元祖转成字符串
s = time.asctime(b)
print(s)

#将时间戳转为字符串
p = time.ctime(c)
print(p)

#将时间元祖转成给定格式的字符串，参数2为时间元组，无参数2则为当前时间
q = time.strftime('%Y-%m-%d  %H:%M:%S',b)
print(q)

#将时间字符串转为时间元组
w = time.strptime(q,'%Y-%m-%d %X')
print(w)

#延迟时间，整型或浮点
time.sleep(1)

#返回当前程序的cpu时间
#Unix返回全部运行时间
#windows从第二次开始，都是以第一个调用此函数的时间戳作为基数
y1 = time.clock()
print('%d'% y1)
time.sleep(2)
y2 = time.clock()
print('%d'% y2)