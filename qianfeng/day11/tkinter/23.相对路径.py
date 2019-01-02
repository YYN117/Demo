import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

label1 = tkinter.Label(win,text = 'good',bg = 'blue')
label2 = tkinter.Label(win,text = 'nice',bg = 'red')
label3 = tkinter.Label(win,text = 'gcool',bg = 'yellow')

#绝对布局,窗口变化对位置无变化
label2.place(x=50,y=50)
label3.place(x=100,y=100)

win.mainloop()