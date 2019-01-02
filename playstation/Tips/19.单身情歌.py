import re
a = input('输入：')
b = re.search('love',a,flags = re.I)
if bool(b) == True:
    print('LOVE')
else:
    print('SINGLE')