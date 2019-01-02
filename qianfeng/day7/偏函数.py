import functools


print(int('1010',base = 2))


def int2(str,base = 2):
    return int(str,base)

print(int2('1011'))

int3 = functools.partial(int, base = 2)
print(int3('111'))