import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert('',0,'中国',text = 'Chi',values = ('F1'))
treeF2 = tree.insert('',1,'美国',text = 'USA',values = ('F2'))
treeF3 = tree.insert('',2,'英国',text = 'ENG',values = ('F3'))

#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,'黑龙江',text='中黑',values=('F1_1'))
treeF1_2 = tree.insert(treeF1,1,'吉林',text='中吉',values=('F1_2'))
treeF1_3 = tree.insert(treeF1,2,'辽宁',text='中辽',values=('F1_3'))

#三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,'哈尔滨',text = '黑龙江哈尔滨')
treeF1_1_2 = tree.insert(treeF1_1,1,'五常',text = '黑龙江五常')

win.mainloop()