from tkinter import *
# from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl

class salesClass: ## NEED TO ASSIGN SUPPLIER IN ITEM CODE
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x510+200+130")
        self.root.title("Sales")
        self.root.iconbitmap("resoures\checklist.ico")
        self.root.config(bg="white")
        self.root.focus_force()




        title = Label(self.root, text="Customer Sales Invoices", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=50, y=10, width=1000)






if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()