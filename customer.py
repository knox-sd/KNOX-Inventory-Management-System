from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl

class cusClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x550+100+100")
        self.root.title("Customers")
        self.root.iconbitmap("resoures\checklist.ico")
        self.root.config(bg="white")
        self.root.focus_force()

        #define all variable
        self.var_cus_id = StringVar()
        self.var_cus_name = StringVar()
        self.var_cus_contact = StringVar()
        self.var_cus_fax = StringVar()
        self.var_cus_pobox = StringVar()
        self.var_cus_email = StringVar()
        self.var_cus_contactper = StringVar()
        self.var_cus_designation = StringVar()
        self.var_cus_address = StringVar()
        self.var_cus_description = StringVar()
        self.var_cus_bankname = StringVar()
        self.var_cus_acname = StringVar()
        self.var_cus_acnumber = StringVar()
        self.var_cus_swiftcode = StringVar()
        self.var_cus_bankaddress = StringVar()
        self.var_cus_paymenterm = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        title = Label(self.root, text="Customer Registration and Details", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=35, y=10, width=1000)

        #content COL1
        lbl_supid = Label(self.root, text="Customer ID", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=60)
        txt_supid = Entry(self.root, textvariable=self.var_cus_id, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=60, width=350, height=30)


        lbl_name = Label(self.root, text="Customer Name", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=100)
        txt_name = Entry(self.root, textvariable=self.var_cus_name, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=100, width=350, height=30)

        lbl_contact = Label(self.root, text="Contact No.", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=140)
        txt_contact = Entry(self.root, textvariable=self.var_cus_contact, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=140, width=350, height=30)

        lbl_fax = Label(self.root, text="Fax No.", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=180)
        txt_fax = Entry(self.root, textvariable=self.var_cus_fax, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=180, width=350, height=30)

        lbl_pobox = Label(self.root, text="P.O. BOX No.", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=220)
        txt_pobox = Entry(self.root, textvariable=self.var_cus_pobox, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=220, width=350, height=30)

        lbl_email = Label(self.root, text="Email Address", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=260)
        txt_email = Entry(self.root, textvariable=self.var_cus_email, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=260, width=350, height=30)

        lbl_contactper= Label(self.root, text="Contact Name", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=300)
        txt_contactper = Entry(self.root, textvariable=self.var_cus_contactper, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=300, width=350, height=30)

        lbl_designation= Label(self.root, text="Designation", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=340)
        txt_designation = Entry(self.root, textvariable=self.var_cus_designation, font=("Century Gothic", 12,), bg="lightyellow").place(x=170, y=340, width=350, height=30)

        lbl_address = Label(self.root, text="Address", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=380)
        self.txt_address = Text(self.root, font=("Century Gothic", 12,), bg="lightyellow")
        self.txt_address.place(x=170, y=380, width=350, height=70)

        lbl_desc = Label(self.root, text="Description", font=("Century Gothic", 12, "bold"), bg="white").place(x=20, y=460)
        self.txt_desc = Text(self.root, font=("Century Gothic", 12,), bg="lightyellow")
        self.txt_desc.place(x=170, y=460, width=350, height=70)

        #COL2
        lbl_bankname= Label(self.root, text="Bank Name", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=60)
        txt_bankname = Entry(self.root, textvariable=self.var_cus_bankname, font=("Century Gothic", 12,), bg="lightyellow").place(x=700, y=60, width=350, height=30)

        lbl_acname= Label(self.root, text="A/C Name", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=100)
        txt_acname = Entry(self.root, textvariable=self.var_cus_acname, font=("Century Gothic", 12,), bg="lightyellow").place(x=700, y=100, width=350, height=30)

        lbl_acnumber= Label(self.root, text="A/C Number", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=140)
        txt_acnumber = Entry(self.root, textvariable=self.var_cus_acnumber, font=("Century Gothic", 12,), bg="lightyellow").place(x=700, y=140, width=350, height=30)

        lbl_swiftcode= Label(self.root, text="SWIFT Code", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=180)
        txt_swiftcode = Entry(self.root, textvariable=self.var_cus_swiftcode, font=("Century Gothic", 12,), bg="lightyellow").place(x=700, y=180, width=350, height=30)

        lbl_bnkadd = Label(self.root, text="Bank Address", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=220)
        self.txt_bnkadd = Text(self.root, font=("Century Gothic", 12), bg="lightyellow")
        self.txt_bnkadd.place(x=700, y=220, height=46, width=350)

        lbl_paymenterm= Label(self.root, text="Payment Terms", font=("Century Gothic", 12, "bold"), bg="white").place(x=550, y=275)
        # txt_paymenterm = Entry(self.root, textvariable=self.var_cus_paymenterm, font=("Century Gothic", 12,), bg="lightyellow").place(x=550, y=340, width=180)
        cmb_pterm = ttk.Combobox(self.root, textvariable=self.var_cus_paymenterm, values=("Select", "Cash on Delivery", "12 Days", "30 Days", "45 Days", "60 Days", "90 Days", "120 Days"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_pterm.place(x=700, y=275, width=180)
        cmb_pterm.current(0)

        # Button function
        btn_save = Button(self.root, text="Save",command=self.add, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=550, y=505, width=90, height=30)
        btn_udpate = Button(self.root, text="Update",command=self.update, font=("Century Gothic", 12), bg="darkblue", fg="white", cursor="hand2").place(x=650, y=505, width=90, height=30)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("Century Gothic", 12), bg="darkred", fg="white", cursor="hand2").place(x= 750, y=505, width=90, height=30)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("Century Gothic", 12), bg="darkgray", fg="white", cursor="hand2").place(x=850, y=505, width=90, height=30)
        btn_export = Button(self.root, text="Export",command=self.export_data, font=("Century Gothic", 12), bg="#2596be", fg="white", cursor="hand2").place(x=950, y=505, width=90, height=30)

        # ## ===searchFram===
        SearchFrame = LabelFrame(self.root, text="Search Customers", font=("Century Gothic", 10, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x = 550, y = 305, width= 330, height= 45)

        ## options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "cus_id", "cus_name", "cus_email", "cus_contact"), state='readonly', justify=LEFT, font=("Century Gothic", 8))
        cmb_search.place(x=10, y=1, height=20,width=100)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Century Gothic", 8), bg="lightyellow", relief=RIDGE).place(x=115, y=1, width=140, height=20)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("Century Gothic", 10), bg="darkgreen", fg="white", cursor="hand2").place(x=260, y=1, width=60, height=20)


        # Customer Table details box
        cus_frame = Frame(self.root, bd=3, relief=RIDGE)
        cus_frame.place(x=550, y=350, width=500, height=150)

        scrolly = Scrollbar(cus_frame, orient=VERTICAL)
        scrollx = Scrollbar(cus_frame, orient=HORIZONTAL)

        ## Add field into Supplier Table
        self.CustomerTable = ttk.Treeview(cus_frame, columns=("cus_id", "cus_name", "cus_contact", "cus_fax", "cus_pobox", "cus_email", "cus_contpersion", "cus_designa", "cus_address", "cus_description", "cus_bankname", "cus_acname", "cus_acnumber", "cus_swift", "cus_bankadd", "cus_pterms"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CustomerTable.xview)
        scrolly.config(command=self.CustomerTable.yview)

        self.CustomerTable.heading("cus_id", text="CUS ID")
        self.CustomerTable.heading("cus_name", text= "Customer Name") 
        self.CustomerTable.heading("cus_contact", text="Contact")
        self.CustomerTable.heading("cus_fax", text="Fax No.")
        self.CustomerTable.heading("cus_pobox", text="PO Box No.")
        self.CustomerTable.heading("cus_email", text="E-mail")
        self.CustomerTable.heading("cus_contpersion", text= "Contact Persion")
        self.CustomerTable.heading("cus_designa", text="Designation")
        self.CustomerTable.heading("cus_address",text="Address")
        self.CustomerTable.heading("cus_description", text="Description") 
        self.CustomerTable.heading("cus_bankname", text="Bank Name")
        self.CustomerTable.heading("cus_acname", text="Account Name")
        self.CustomerTable.heading("cus_acnumber", text="Account Number")
        self.CustomerTable.heading("cus_swift", text="SWIFT Code")
        self.CustomerTable.heading("cus_bankadd", text="Bank Address")
        self.CustomerTable.heading("cus_pterms", text="Payment Terms")
        self.CustomerTable["show"] = "headings"

        #supplyer filled size
        self.CustomerTable.column("cus_id", width=70)
        self.CustomerTable.column("cus_name", width=150) 
        self.CustomerTable.column("cus_contact", width=100)
        self.CustomerTable.column("cus_fax", width=100)
        self.CustomerTable.column("cus_pobox", width=100)
        self.CustomerTable.column("cus_email", width=100)
        self.CustomerTable.column("cus_contpersion", width=100)
        self.CustomerTable.column("cus_designa", width=100)
        self.CustomerTable.column("cus_address", width=100)
        self.CustomerTable.column("cus_description", width=100) 
        self.CustomerTable.column("cus_bankname", width=100)
        self.CustomerTable.column("cus_acname", width=100)
        self.CustomerTable.column("cus_acnumber", width=100)
        self.CustomerTable.column("cus_swift", width=100)
        self.CustomerTable.column("cus_bankadd", width=100)
        self.CustomerTable.column("cus_pterms", width=100)

        self.CustomerTable.pack(fill=BOTH, expand=1)
        self.CustomerTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

## Add data in data base

    def add(self):
        con = sqlite3.connect(database=r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_cus_id.get() =="":
                messagebox.showerror("Error", "Customer ID Must be Requried", parent = self.root)
            else:
                cur.execute("Select * from customer where cus_id = ?", (self.var_cus_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Customer ID already exists, try different ID", parent  = self.root)
                else:
                    cur.execute("Insert into customer (cus_id, cus_name, cus_contact, cus_fax, cus_pobox, cus_email, cus_contpersion, cus_designa, cus_address, cus_description, cus_bankname, cus_acname, cus_acnumber, cus_swift, cus_bankadd, cus_pterms) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                    self.var_cus_id.get(),
                                    self.var_cus_name.get(),
                                    self.var_cus_contact.get(),
                                    self.var_cus_fax.get(),
                                    self.var_cus_pobox.get(),
                                    self.var_cus_email.get(),
                                    self.var_cus_contactper.get(),
                                    self.var_cus_designation.get(),
                                    self.txt_address.get('1.0',END),
                                    self.txt_desc.get('1.0',END),
                                    self.var_cus_bankname.get(),
                                    self.var_cus_acname.get(),
                                    self.var_cus_acnumber.get(),
                                    self.var_cus_swiftcode.get(),
                                    self.txt_bnkadd.get('1.0', END),
                                    self.var_cus_paymenterm.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Customer Added Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def show(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from customer")
            rows = cur.fetchall()
            self.CustomerTable.delete(*self.CustomerTable.get_children())
            for row in rows:
                self.CustomerTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def get_data(self, ev): # show data function
        data = self.CustomerTable.focus()
        content = (self.CustomerTable.item(data))
        row = content['values']
        # print(row)
        self.var_cus_id.set(row[0]),
        self.var_cus_name.set(row[1]),
        self.var_cus_contact.set(row[2]),
        self.var_cus_fax.set(row[3]),
        self.var_cus_pobox.set(row[4]),
        self.var_cus_email.set(row[5]),
        self.var_cus_contactper.set(row[6]),
        self.var_cus_designation.set(row[7]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END, row[8]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END, row[9]),
        self.var_cus_bankname.set(row[10]),
        self.var_cus_acname.set(row[11]),
        self.var_cus_acnumber.set(row[12]),
        self.var_cus_swiftcode.set(row[13]),
        self.txt_bnkadd.delete('1.0', END),
        self.txt_bnkadd.insert(END, row[14]),
        self.var_cus_paymenterm.set(row[15]),


    def update(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_cus_id.get() == "":
                messagebox.showerror("Error", "Customer ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from customer where cus_id = ?", (self.var_cus_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Customer ID",  parent = self.root)
                else:
                    cur.execute("Update customer set cus_name=?, cus_contact=?, cus_fax=?, cus_pobox=?, cus_email=?, cus_contpersion=?, cus_designa=?, cus_address=?, cus_description=?, cus_bankname=?, cus_acname=?, cus_acnumber=?, cus_swift=?, cus_bankadd=?, cus_pterms=? where cus_id = ?",(
                                    self.var_cus_name.get(),
                                    self.var_cus_contact.get(),
                                    self.var_cus_fax.get(),
                                    self.var_cus_pobox.get(),
                                    self.var_cus_email.get(),
                                    self.var_cus_contactper.get(),
                                    self.var_cus_designation.get(),
                                    self.txt_address.get('1.0',END),
                                    self.txt_desc.get('1.0',END),
                                    self.var_cus_bankname.get(),
                                    self.var_cus_acname.get(),
                                    self.var_cus_acnumber.get(),
                                    self.var_cus_swiftcode.get(),
                                    self.txt_bnkadd.get('1.0', END),
                                    self.var_cus_paymenterm.get(),
                                    self.var_cus_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Customer Updated Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def delete(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_cus_id.get() == "":
                messagebox.showerror("Error", "Customer ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from customer where cus_id = ?", (self.var_cus_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Customer ID",  parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from customer where cus_id=?",(self.var_cus_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Customer Deleted Successfully", parent = self.root)
                        self.show()
                        # self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)
        con.close()

    def clear(self):
        self.var_cus_id.set(""),    
        self.var_cus_name.set(""),
        self.var_cus_contact.set(""),
        self.var_cus_fax.set(""),
        self.var_cus_pobox.set(""),
        self.var_cus_email.set(""),
        self.var_cus_contactper.set(""),
        self.var_cus_designation.set(""),
        self.txt_address.delete('1.0',END),
        self.txt_desc.delete('1.0',END),
        self.var_cus_bankname.set(""),
        self.var_cus_acname.set(""),
        self.var_cus_acnumber.set(""),
        self.var_cus_swiftcode.set(""),
        self.txt_bnkadd.delete('1.0', END),
        self.var_cus_paymenterm.set("Select"),

        self.show()

    def export_data(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()

        cur.execute("Select * from customer")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns = [ desc[0] for desc in cur.description])
        data = df.to_excel('customers_data.xlsx', index=False)

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
                cur.execute("Select * from customer where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() +"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.CustomerTable.delete(*self.CustomerTable.get_children())
                    for row in rows:
                        self.CustomerTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = cusClass(root)
    root.mainloop()