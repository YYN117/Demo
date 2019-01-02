import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title('117')
win.geometry('600x400+200+50')

path = r'C:\Users\Jhon117\Desktop\demo'
treeWin = TreeWindows(win,path)
infoWin = InfoWindows(win)

win.mainloop()