import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#<B1-Motion>表示左键移动
label = tkinter.Label(win, text = 'sunck is a fucker')
label.pack()

def func(event):
    print(event.x,event.y)
label.bind('<B1-Motion>',func)

win.mainloop()