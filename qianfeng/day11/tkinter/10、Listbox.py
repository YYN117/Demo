import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

'''
列表框控件，可以包含一个或多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''
#1、创建一个listbox，添加几个元素
lb = tkinter.Listbox(win,selectmode = tkinter.BROWSE)
lb.pack()
for item in ['good','nice','handsome','vg','vn']:
    #按顺序添加
    lb.insert(tkinter.END,item)
#在开始添加
lb.insert(tkinter.ACTIVE,'cool')
#将列表当成一个元素添加
# lb.insert(tkinter.END,['python'，‘C++’])
#删除 参数1为开始的索引，参数2为结束的索引，如果不指定参数2，则只删除第一个索引的内容
# lb.delete(1,3)
#选中 参数1为开始的索引，参数2为结束的索引，如果不指定参数2，则只选中第一个索引的内容
lb.select_set(2,4)
#取消选中
lb.select_clear(3)
#获取到列表中的元素个数
print(lb.size())
#从列表取值
print(lb.get(2,4))

#返回当前的索引项，不是item元素
print(lb.curselection())
#判断一个选项是否被选中
print(lb.selection_includes())
win.mainloop()