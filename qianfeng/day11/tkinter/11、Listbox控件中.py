import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#绑定变量
lbv =tkinter.StringVar()
#与BORWSE相似，但不支持鼠标按下后移动选中
lb = tkinter.Listbox(win , selectmode = tkinter.SINGLE,listvariable = lbv)
lb.pack()
for item in ['good','nice','handsome','vg','vn']:
    #按顺序添加
    lb.insert(tkinter.END,item)

#打印当前列表中选项
print(lbv.get())


#绑定事件  1表示鼠标左键
def myPrint(event):
    print(lb.get(lb.curselection()))

lb.bind('<Double-Button -1>',myPrint)

win.mainloop()