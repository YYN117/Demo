'''
描述:
一年有多少天，这是个大问题，很值得思考。现在给你一个年份year(year为四位数字的字符串，如"2008","0012"),
你输出这一年的天数。如year="2013", 则输出365。

*********
一、闰年的计算方法
如果是世纪年，如1900，2000等可以被100整除的年份，只有可以被400整除的年份是闰年，其他年份是平年；
其他不是世纪年的年份可以被4整除的就是闰年，否则就是平年。
'''

def is_leap_year(year):
    if (year) % 1000 == 0:
        if (year) % 400 == 0:
            print(366)
        else:
            print(365)
    else:
        if year % 4 == 0:
            print(366)
        else:
            print(365)
year = int(input('输入:'))
is_leap_year(year)