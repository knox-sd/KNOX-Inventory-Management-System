from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("265x160+550+300")
        self.root.title("Log In")
        self.root.iconbitmap("resoures\mainlogo.ico")
        self.root.config(bg="#00997a")
        self.root.resizable(False, False)

        self.var_user = StringVar()
        self.var_passw = StringVar()

        login_frame = Frame(self.root, bd=2,relief=RIDGE, bg="white")
        login_frame.place(x=6, y=5, width=250, height=150)

        title = Label(login_frame, text="USER LOGIN", font=("goudy old style", 12, "bold"), bg="white").place(x=80, y=0)

        lbl_user = Label(login_frame, text="User ID", font=("Arial", 10, "bold"), bg="white").place(x=2, y=30)
        txt_user = Entry(login_frame, textvariable=self.var_user, font=("Arial", 10), bg="lightgray").place(x=80, y=30)

        lbl_passw = Label(login_frame, text="Password", font=("Arial", 10, "bold"), bg="white").place(x=2, y=60)
        txt_passw = Entry(login_frame, textvariable=self.var_passw, font=("Arial", 10), bg="lightgray").place(x=80, y=60)

        btn_login = Button(login_frame, text="Login",command=self.Log_in, font=("calibri", 9), bd=2, bg="#A2D9CE", width=6).place(x=120, y=90)
        btn_cancel = Button(login_frame, text="Cancel", font=("calibri", 9), bd=2, bg="#A2D9CE", width=6).place(x=175, y=90)


    def Log_in(self):
        if self.var_user.get() == "" or self.var_passw.get()=="":
                messagebox.showerror("Error", "User ID and Password requried", parent = self.root)
        
        # else:
        # else:
        #     cur.execute("Select item_code, description, price, quantity, status from items where description LIKE '%" + self.var_search.get() +"%' and status = 'Active'")
        #     rows = cur.fetchall()
        #     if len(rows) != 0:
        #         self.items_Table.delete(*self.items_Table.get_children())
        #         for row in rows:
        #             self.items_Table.insert('', END, values=row)
        #     else:
        #         messagebox.showerror("Error", "No record found!!", parent = self.root)

    def Cancel(self):
        self.var_user

if __name__=="__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()