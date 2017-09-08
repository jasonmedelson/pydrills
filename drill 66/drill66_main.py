import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3

import drill66_func
import drill66_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(700,220) #(width, height)
        self.master.maxsize(700,220)
        self.master.title("Drill 66")
        self.master.configure(bg="#F0F0F0")
        arg = self.master
        
        drill66_gui.load_gui(self)

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
