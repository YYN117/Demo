import tkinter

win = tkinter.Tk()
win.title('yyn')
win.geometry('400x400+200+20')

'''
文本控件，用于显示多行文本
'''
#height表示显示的行数
text = tkinter.Text(win,width=30,height=4)
text.pack()
str = 'Today we continue a never-ending journey, to bridge the meaning of those words with the realities of our time. For history tells us that while these truths may be self-evident, they have never been self-executing; that while freedom is a gift from God, it must be secured by His people here on Earth. The patriots of 1776 did not fight to replace the tyranny of a king with the privileges of a few or the rule of a mob. They gave to us a Republic, a government of, and by, and for the people, entrusting each generation to keep safe our founding creed.'
text.insert(tkinter.INSERT, str)
win.mainloop()