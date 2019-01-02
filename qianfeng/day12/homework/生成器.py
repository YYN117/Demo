def odds(start = 1):
    if start%2 == 0:
        start += 1
    while True:
        yield start
        print('#')
        print(start)
        print('!')
        start += 2

for n in odds():
    if n>7:
        break
    else:
        print(n)