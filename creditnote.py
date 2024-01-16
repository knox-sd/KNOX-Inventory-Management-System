from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl

class creditnoteClass: ## NEED TO ASSIGN SUPPLIER IN ITEM CODE
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x550+100+100")
        self.root.title("Promotion | Credit Note")
        self.root.iconbitmap("resoures\menu.ico")
        self.root.config(bg="white")
        self.root.focus_force()


        title = Label(self.root, text="Promotion | Credit Note Registration", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=40, y=10, width=1000)





if __name__ == "__main__":
    root = Tk()
    obj = creditnoteClass(root)
    
    root.mainloop()


