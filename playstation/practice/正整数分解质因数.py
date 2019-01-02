import time
n = int(input(':'))
start_time = time.time()
while n != 1:
    for i in range(2,n+1):
        if n % i == 0:
            n //= i
            if n==1:
                print('{}'.format(i))
            else:
                print('{}*'.format(i),end='')
            break
end_time = time.time()
print('耗时{}秒'.format(end_time-start_time))