import tkinter
from tkinter import ttk
import os

class InfoWindows(tkinter.Frame):
    def __init__(self,master):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1)

        self.entry = tkinter.Entry(frame)
        self.entry.pack()

        self.txt = tkinter.Text(frame)
        self.txt.pack()