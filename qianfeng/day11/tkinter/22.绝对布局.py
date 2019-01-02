import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

label1 = tkinter.Label(win,text = 'good',bg = 'blue')
label2 = tkinter.Label(win,text = 'nice',bg = 'red')
label3 = tkinter.Label(win,text = 'gcool',bg = 'yellow')

#相对布局，窗体改动有影响
#tkinter.BOTH
label1.pack(fill = tkinter.Y , side = tkinter.LEFT)
label2.pack(fill = tkinter.X , side = tkinter.TOP)

label3.pack()

win.mainloop()