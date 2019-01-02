import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')


'''
框架控件
在屏幕上显示一个矩形区，多作为容器控件
'''

frm = tkinter.Frame(win)
frm.pack()

#left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l,text = '左上',bg = 'pink').pack(side = tkinter.TOP)
tkinter.Label(frm_l,text = '左下',bg = 'blue').pack(side = tkinter.TOP)
frm_l.pack(side = tkinter.LEFT)

#Right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r,text = '右上',bg = 'red').pack(side = tkinter.TOP)
tkinter.Label(frm_r,text = '右下',bg = 'green').pack(side = tkinter.TOP)
frm_r.pack(side = tkinter.RIGHT)

win.mainloop()
