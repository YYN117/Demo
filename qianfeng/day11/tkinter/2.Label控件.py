import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

'''
Label:标签控件可以显示文本
'''
#win 父窗体
#text : 显示的文本内容
#bg ：背景色
#fg : 字体颜色
#font : 字体和大小
#wraplength : 指定宽度后进行换行
#justify : 设置换行后的对齐方式
#anchor ：位置 n北 e东 s南 w西 center居中 ne se sw nw......
label = tkinter.Label(win,text = 'sunck is a good man',bg = 'pink',fg = 'red',font = ('黑体',20),width = 10,height = 10,wraplength = 30, justify = 'left', anchor = 'ne')
#显示出来
label.pack()

win.mainloop()