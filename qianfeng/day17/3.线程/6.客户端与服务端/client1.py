import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('10.164.26.96',8081))


while True:
    data = input('输入给服务器发送的数据：')
    client.send(data.encode('utf-8'))
    info = client.recv(1024)
    print('服务器回应：',info.decode('UTF-8'))