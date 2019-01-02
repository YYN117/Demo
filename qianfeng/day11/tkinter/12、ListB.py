import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#EXTENDED 可以使；Listbox支持shift和control
lb = tkinter.Listbox(win , selectmode = tkinter.EXTENDED)
lb.pack()
for item in ['good','nice','handsome','vg','vn']:
    #按顺序添加
    lb.insert(tkinter.END,item)

#按住shift可以实现连选
#按住control可以实现多选

win.mainloop()