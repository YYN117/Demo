import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

'''
数值范围控件
'''
def updata():
    print(v.get())
#绑定变量
v = tkinter.StringVar()
#increment  步长 默认为1
#values 最好不要与from_=0 to=100 同时使用
#comman 只要值改变就会执行相应的方法
sp = tkinter.Spinbox(win, from_=0, to =100, increment = 1, textvariable = v, command = updata)
sp.pack()

#设置值
v.set(20)
#取值
print(v.get())
win.mainloop()