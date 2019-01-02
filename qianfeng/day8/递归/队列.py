import collections

#创建一个队列
queue = collections.deque()
print(queue)

#进队
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

#出队
res1 = queue.popleft()
print('res1 = ',res1)
print(queue)
res2 = queue.popleft()
print('res2 =',res2)
print(queue)
