'''
try.....except.....finally
'''

try:
    print(1/0)
except ZeroDivisionError as e:
    print('为0')
finally:
    print('甘霖娘')