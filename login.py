from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("265x160+550+300")
        self.root.title("Log In")
        self.root.iconbitmap("resoures\mainlogo.ico")
        self.root.config(bg="gray")
        self.root.resizable(False, False)

        self.var_empid = StringVar()
        self.var_passw = StringVar()

        login_frame = Frame(self.root, bd=2,relief=RIDGE, bg="white")
        login_frame.place(x=6, y=5, width=250, height=150)

        title = Label(login_frame, text="USER LOGIN", font=("goudy old style", 12, "bold"), bg="white").place(x=80, y=0)

        lbl_user = Label(login_frame, text="User ID", font=("Arial", 10, "bold"), bg="white").place(x=2, y=30)
        txt_user = Entry(login_frame, textvariable=self.var_empid, font=("Arial", 10), bg="lightgray").place(x=80, y=30)

        lbl_passw = Label(login_frame, text="Password", font=("Arial", 10, "bold"), bg="white").place(x=2, y=60)
        txt_passw = Entry(login_frame, textvariable=self.var_passw, show='*',font=("Arial", 10), bg="lightgray").place(x=80, y=60)

        btn_login = Button(login_frame, text="Login",command=self.Log_in, font=("calibri", 9), bd=2, bg="#A2D9CE", width=6).place(x=120, y=90)
        btn_cancel = Button(login_frame, text="Cancel",command=self.cancel_win, font=("calibri", 9), bd=2, bg="#A2D9CE", width=6).place(x=175, y=90)


    def Log_in(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_empid.get() == "" or self.var_passw.get()=="":
                messagebox.showerror('Error', "User ID and Password requried", parent = self.root)
            else:
                cur.execute("select utype from employee where eid = ? AND passw = ?",(self.var_empid.get(),self.var_passw.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror('Error', "Invalid User/ Password", parent = self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python main.py")
                        # print(user)
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                    
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def forget_window(self):
        if self.var_empid.get() == "":
            pass
##23 min

    def cancel_win(self):
        self.root.destroy()
        os.system("Exit")

if __name__=="__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()