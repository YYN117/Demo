import  itertools
import time

passwd = (''.join(x) for x in itertools.product('0123456789',repeat=4))
# mylist = list(itertools.combinations([1,2,3,4,5],4))
# print(mylist)
# print(len(mylist))
while True:
    try:
        # time.sleep(0.5)
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break