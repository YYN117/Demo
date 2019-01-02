'''
TCP是建立可靠的连接，并且通信双方均可以流的形式发送数据，相对于TCP，UDP则是面向无连接的协议。

使用UDP时，不需要建立连接，只需要知道对方的IP地址和端口号即可直接发送数据包，但能否送达未知。

虽然UDP传输数据不可靠，但其优点是和TCP相比，速度快，对于要求不高的数据，可以使用UDP

'''
import time
import socket

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(('10.0.142',2425))
udp.send('大丁丁'.encode('utf-8'))
'''
while True:
    udp.send('大丁丁'.encode('utf-8'))
    time.sleep(1)
'''