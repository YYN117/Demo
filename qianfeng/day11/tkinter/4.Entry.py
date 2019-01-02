import tkinter


win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')


'''
输入控件
用于显示简单的文本内容
'''

#绑定变量
e = tkinter.Variable()
#show是密文显示
entry = tkinter.Entry(win,textvariable = e)
entry.pack()

#e代表输入框这个对象
#设置值
e.set('sunck is a big guy')
#取值
print(e.get())
print(entry.get())
win.mainloop()