import tkinter

def func():
    print('sunck')

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#创建按钮
button1= tkinter.Button(win,text = '按钮',command = func,width = 10,height = 10)
button1.pack()

button2 = tkinter.Button(win,text = '按钮',command = lambda : print('yyn is a nice man'))
button2.pack()


win.mainloop()