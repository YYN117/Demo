import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input('输入数据：')
    client.sendto(data.encode('utf-8'),('10.164.26.96',8900))
    info = client.recv(1024).decode('utf-8')
    print('服务器：',info)