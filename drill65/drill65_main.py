import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

import drill65_func
import drill65_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(700,200) #(width, height)
        self.master.maxsize(700,200)
        self.master.title("Drill 65")
        self.master.configure(bg="#F0F0F0")
        arg = self.master
        drill65_gui.load_gui(self)

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
