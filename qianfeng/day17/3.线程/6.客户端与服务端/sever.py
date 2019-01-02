import socket
import threading
#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP端口
server.bind(('10.164.26.96',8081))
server.listen(5)
def run(ck):
    data = clientSocket.recv(1024)
    print('客户端数据：'+data.decode('utf-8')  )
    # sendData = input('输入返回给客户端的数据：')
    clientSocket.send('I have a big dick'.encode('UTF-8'))

print('服务器启动，等待客户端连接')
while True:
    clientSocket, clientAddress = server.accept()
    t = threading.Thread(target=run,args=(clientSocket,))
    t.start()
    # print('%s ---- %s 连接成功' % (str(clientSocket), clientAddress))


# while True:
#     #等待客户端连接
#     clientSocket,clientAddress = server.accept()
#     #启动一个线程，将当前连接的clientSocket交给线程