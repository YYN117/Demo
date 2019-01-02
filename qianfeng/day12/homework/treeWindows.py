import tkinter
from tkinter import ttk
import os

class  TreeWindows(tkinter.Frame):
    def __init__(self,master,path):
        frame = tkinter.Frame(master)
        frame.pack()

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side = tkinter.LEFT,fill = tkinter.Y)
        # print(os.path.splitext(path))

        root = self.tree.insert('','end',text = self.getLastPath(path) , open = True)
        self.loadTree(root,path)

        #添加滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side = tkinter.RIGHT,fill = tkinter.Y)
        self.sy.config(command = self.tree.yview)
        self.tree.config(yscrollcommand = self.sy.set)

    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            #插入树枝
            treey = self.tree.insert(parent,'end',text = self.getLastPath(absPath))
            #判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey , absPath)

    def getLastPath(self,path):
        pathList = os.path.split(path)
        return pathList[-1]

        return