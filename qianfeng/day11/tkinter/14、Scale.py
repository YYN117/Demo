import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')
'''
供用户通过拖拽指示器改变变量的值，可以水平(tkinter.HORIZONTA)，也可以竖直(tkinter.VERTICAL)
length 水平时表示宽度，竖直时表示高度
tickinterval 选择值会为该值的倍数
'''

scale1 = tkinter.Scale(win,from_=0, to = 100,orient = tkinter.HORIZONTAL, tickinterval =10 ,length =200)

scale1.pack()
def showNum():
    print(scale1.get())
tkinter.Button(win,text = '按钮',command = showNum ).pack()

win.mainloop()