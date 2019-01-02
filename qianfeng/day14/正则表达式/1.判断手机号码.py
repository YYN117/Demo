'''
给一个字符串，判断是否是手机号码
'''
# def checkPhone(str):
#     if len(str) != 11:
#         return False
#     elif str[0] != 1:
#         return False
#     elif str[1:3] != '31'and str[1:3] != '39':
#         return False
#     for i in range(3,11):
#         if str[i] < '0' or str[i] > '9':
#             return False
#     return True
# print(checkPhone(''))
import re
def checkPhone2(str):
    pat = r'^1(([3578]\d)|(47)){8}$'
    res = re.match(pat,str)
    print(res)