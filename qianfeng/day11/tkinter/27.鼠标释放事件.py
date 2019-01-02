import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#<ButtonRelease-1> 释放鼠标左键
label = tkinter.Label(win,text='sunck is a fucker', bg = 'red')
label.pack()
def func(event):
    print(event.x,event.y)
label.bind('<ButtonRelease-1>',func)

win.mainloop()