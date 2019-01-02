endstr = 'end'
str = ''


for line in iter(input, endstr):
    str += line + '\n'
print(str)