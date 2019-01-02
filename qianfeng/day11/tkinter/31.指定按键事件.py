import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#<Key>响应所有的按键
label = tkinter.Label(win,text='sunck is a fucker', bg = 'red')
#设置焦点
label.focus_set()
label.pack()

def func(event):
    print('event.chr = ',event.char)
    print('event.keycode = ', event.keycode)
label.bind('a',func) #只能响应a


win.mainloop()