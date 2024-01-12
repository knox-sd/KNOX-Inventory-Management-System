from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl


class empClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x510+200+130")
        self.root.title("Employees")
        self.root.iconbitmap("resoures\interface.ico")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Define all variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()
        
        
        ## ===searchFram===
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Century Gothic", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x = 250, y = 7, width= 600, height= 60)

        # options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "EMP ID", "Name", "Email", "Contact"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_search.place(x=10, y=2, height=30,width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Century Gothic", 10), bg="lightyellow", relief=RIDGE).place(x=210, y=2, height=30, width=200)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=435, y=2, width=150, height=30)

        # title
        title = Label(self.root, text = "Employee Details", font= ("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=50, y=80, width=1000)

        #content ROW1
        lbl_empid = Label(self.root, text = "Emp ID", font= ("Century Gothic", 15), bg="white").place(x=50, y=120)
        lbl_gender = Label(self.root, text = "Gender", font= ("Century Gothic", 15), bg="white").place(x=350, y=120)
        lbl_contact = Label(self.root, text = "Contact", font= ("Century Gothic", 15), bg="white").place(x=750, y=120)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font= ("Century Gothic", 15), bg="lightyellow").place(x=150, y=120, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Others"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_gender.place(x=500, y=120, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font= ("Century Gothic", 15), bg="lightyellow").place(x=850, y=120, width=180)
        # contact ROW2
        lbl_name = Label(self.root, text = "Name", font= ("Century Gothic", 15), bg="white").place(x=50, y=160)
        lbl_dob = Label(self.root, text = "D.O.B", font= ("Century Gothic", 15), bg="white").place(x=350, y=160)
        lbl_doj = Label(self.root, text = "D.O.J", font= ("Century Gothic", 15), bg="white").place(x=750, y=160)

        txt_name = Entry(self.root, textvariable=self.var_name, font= ("Century Gothic", 15), bg="lightyellow").place(x=150, y=160, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font= ("Century Gothic", 15), bg="lightyellow").place(x=500, y=160, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font= ("Century Gothic", 15), bg="lightyellow").place(x=850, y=160, width=180)

        # contact ROW3
        lbl_email = Label(self.root, text = "Email", font= ("Century Gothic", 15), bg="white").place(x=50, y=200)
        lbl_pswd = Label(self.root, text = "Password", font= ("Century Gothic", 15), bg="white").place(x=350, y=200)
        lbl_utype = Label(self.root, text = "User Type", font= ("Century Gothic", 15), bg="white").place(x=750, y=200)

        txt_email = Entry(self.root, textvariable=self.var_email, font= ("Century Gothic", 15), bg="lightyellow").place(x=150, y=200, width=180)
        txt_pswd = Entry(self.root, textvariable=self.var_pass, font= ("Century Gothic", 15), bg="lightyellow").place(x=500, y=200, width=180)
        # txt_utype = Entry(self.root, textvariable=self.var_utype, font= ("Century Gothic", 15), bg="lightyellow").place(x=850, y=200, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_utype.place(x=850, y=200, width=180)
        cmb_utype.current(0)

        # contact ROW4
        lbl_address = Label(self.root, text = "Address", font= ("Century Gothic", 15), bg="white").place(x=50, y=240)
        lbl_salary = Label(self.root, text = "Salary", font= ("Century Gothic", 15), bg="white").place(x=500, y=240)

        self.txt_address = Text(self.root, font= ("Century Gothic", 12), bg="lightyellow")
        self.txt_address.place(x=150, y=240, width=300, height=70)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font= ("Century Gothic", 15), bg="lightyellow").place(x=600, y=240, width=180)

        # Button function
        btn_save = Button(self.root, text="Save",command=self.add, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=500, y=280, width=100, height=30)
        btn_udpate = Button(self.root, text="Update",command=self.update, font=("Century Gothic", 12), bg="darkblue", fg="white", cursor="hand2").place(x=610, y=280, width=100, height=30)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("Century Gothic", 12), bg="darkred", fg="white", cursor="hand2").place(x= 720, y=280, width=100, height=30)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("Century Gothic", 12), bg="darkgray", fg="white", cursor="hand2").place(x=830, y=280, width=100, height=30)
        btn_export = Button(self.root, text="Export",command=self.export_data, font=("Century Gothic", 12), bg="#2596be", fg="white", cursor="hand2").place(x=940, y=280, width=100, height=30)

        #Employee Table details box
        emp_frame = Frame(self.root, bd =3, relief= RIDGE)
        emp_frame.place(x=0, y=325, relwidth=1, height=185)
        
        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)
                
        # add filled in Emp table
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "gender", "contact", "email", "dob", "doj", "passw", "utype", "address", "salary"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("email", text="E-mail")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("passw", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable["show"] = "headings"
        
        # emp filled resize
        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("passw", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)        

        self.EmployeeTable.pack(fill= BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data) # show data on field from table

        self.show()

## Add data in database ##

    def add(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be Requried", parent = self.root)
            else:
                cur.execute("Select * from employee where eid = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID already exists, try diffrent ID",  parent = self.root)
                else:
                    cur.execute("Insert into employee (eid, name, gender, contact, email, dob, doj, passw, utype, address, salary) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                    self.var_emp_id.get(),
                                    self.var_name.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def show(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def get_data(self, ev): # show data function
        data = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(data))
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_contact.set(row[3])
        self.var_email.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from employee where eid = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID",  parent = self.root)
                else:
                    cur.execute("Update employee set name=?, gender=?, contact=?, email=?, dob=?, doj=?, passw=?, utype=?, address=?, salary=? where eid = ?",(
                                    self.var_name.get(),
                                    self.var_gender.get(),
                                    self.var_contact.get(),
                                    self.var_email.get(),
                                    self.var_dob.get(),
                                    self.var_doj.get(),
                                    self.var_pass.get(),
                                    self.var_utype.get(),
                                    self.txt_address.get('1.0',END),
                                    self.var_salary.get(),
                                    self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def delete(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from employee where eid = ?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID",  parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent = self.root)
                        # self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)
        con.close()

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        
        self.show()

    def export_data(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()

        cur.execute("Select * from employee")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns = [ desc[0] for desc in cur.description])
        data = df.to_excel('employee_data.xlsx', index=False)

        messagebox.showinfo("Success", "Export Successfully", parent = self.root)
        self.show()


    def search(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option!", parent = self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search Input Requried!", parent = self.root)
            else:
                cur.execute("Select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() +"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

if __name__=="__main__":
    root=Tk()
    obj = empClass(root)
    root.mainloop()