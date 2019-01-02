import tkinter
import socket
import threading

win = tkinter.Tk()
win.title('QQ服务器')
win.geometry('400x400+200+20')

users = {}

def run(ck,ca):
    userName = ck.recv(1024)
    users[userName] = ck
    printStr = userName + '连接'
    text.insert(tkinter.INSERT, printStr)

def start():
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)
    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))
        t.start()

def startSever():
    s = threading.Thread(target=start)
    s.start()

    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)
    printStr = '服务器启动'
    text.insert(tkinter.INSERT, printStr)

    while True:
        ck,ca= server.accept()
        t = threading.Thread(target=run, args=(ck,ca))
        t.start()

lalbeIp = tkinter.Label(win,text = 'ip').grid(row = 0,column = 0)
lablePort = tkinter.Label(win,text = 'port').grid(row = 1,column = 0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable = eip).grid(row = 0,column = 1)
entryPort = tkinter.Entry(win,textvariable = eport).grid(row = 1,column = 1)
button= tkinter.Button(win,text = '启动',command = startSever).grid(row = 2,column = 0)
text = tkinter.Text(win,width=30,height=10)
text.grid(row = 3,column = 0)

win.mainloop()