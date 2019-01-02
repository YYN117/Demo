import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#<Enter>鼠标光标进入控件时触发
#<leave>鼠标光标离开。。。
label = tkinter.Label(win,text='sunck is a fucker', bg = 'red')
label.pack()
def func(event):
    print(event.x,event.y)
label.bind('<Enter>',func)


win.mainloop()