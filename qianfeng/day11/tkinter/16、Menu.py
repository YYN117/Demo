import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

#菜单条
menubar = tkinter.Menu(win)
win.config(menu = menubar)

def func():
    print('!!!')
#创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff = False)
#给菜单选项加内容
for item in ['python','PHP', 'C' ,'C++','Java','shell','JS','exit']:
    if item == 'exit':
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command = lambda :win.quit)
    else:
        menu1.add_command(label=item,command = func)
#向菜单条上加菜单
menubar.add_cascade(label = '语言',menu = menu1)
win.mainloop()