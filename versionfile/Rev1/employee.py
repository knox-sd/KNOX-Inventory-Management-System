from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk
class empClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x510+200+130")
        self.root.title("KNOX Enterprise Management System | v.1")
        self.root.iconbitmap("")
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
        btn_search = Button(SearchFrame, text="Search", font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=435, y=2, width=150, height=30)

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
        btn_save = Button(self.root, text="Save", font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=500, y=280, width=100, height=30)
        btn_udpate = Button(self.root, text="Update", font=("Century Gothic", 12), bg="blue", fg="white", cursor="hand2").place(x=620, y=280, width=100, height=30)
        btn_delete = Button(self.root, text="Delete", font=("Century Gothic", 12), bg="orange", fg="white", cursor="hand2").place(x= 740, y=280, width=100, height=30)
        btn_clear = Button(self.root, text="Clear", font=("Century Gothic", 12), bg="gray", fg="white", cursor="hand2").place(x=860, y=280, width=100, height=30)

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

if __name__=="__main__":
    root=Tk()
    obj = empClass(root)
    root.mainloop()