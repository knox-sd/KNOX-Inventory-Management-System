from tkinter import *
# from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl

class suppClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x510+200+130")
        self.root.title("Suppliers")
        self.root.iconbitmap("resoures\checklist.ico")
        self.root.config(bg="white")
        self.root.focus_force()

        #define all variable
        self.var_sup_id = StringVar()
        self.var_sup_name = StringVar()
        self.var_sup_contact = StringVar()
        self.var_sup_fax = StringVar()
        self.var_sup_pobox = StringVar()
        self.var_sup_email = StringVar()
        self.var_sup_contactper = StringVar()
        self.var_sup_designation = StringVar()
        self.var_sup_address = StringVar()
        self.var_sup_description = StringVar()
        self.var_sup_bankname = StringVar()
        self.var_sup_acname = StringVar()
        self.var_sup_acnumber = StringVar()
        self.var_sup_swiftcode = StringVar()
        self.var_sup_bankaddress = StringVar()
        self.var_sup_paymenterm = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        title = Label(self.root, text="Suppliers Registration and Details", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=50, y=10, width=1000)

        #content COL1
        lbl_supid = Label(self.root, text="Supplier ID", font=("Century Gothic", 15), bg="white").place(x=20, y=60)
        txt_supid = Entry(self.root, textvariable=self.var_sup_id, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=60, width=180)

        lbl_name = Label(self.root, text="Supplier Name", font=("Century Gothic", 15), bg="white").place(x=20, y=100)
        txt_name = Entry(self.root, textvariable=self.var_sup_name, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=100, width=180)

        lbl_contact = Label(self.root, text="Contact No.", font=("Century Gothic", 15), bg="white").place(x=20, y=140)
        txt_contact = Entry(self.root, textvariable=self.var_sup_contact, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=140, width=180)

        lbl_fax = Label(self.root, text="Fax No.", font=("Century Gothic", 15), bg="white").place(x=20, y=180)
        txt_fax = Entry(self.root, textvariable=self.var_sup_fax, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=180, width=180)

        lbl_pobox = Label(self.root, text="P.O. BOX No.", font=("Century Gothic", 15), bg="white").place(x=20, y=220)
        txt_pobox = Entry(self.root, textvariable=self.var_sup_pobox, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=220, width=180)

        lbl_email = Label(self.root, text="Email Address", font=("Century Gothic", 15), bg="white").place(x=20, y=260)
        txt_email = Entry(self.root, textvariable=self.var_sup_email, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=260, width=180)

        lbl_contactper= Label(self.root, text="Contact Name", font=("Century Gothic", 15), bg="white").place(x=20, y=300)
        txt_contactper = Entry(self.root, textvariable=self.var_sup_contactper, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=300, width=180)

        lbl_designation= Label(self.root, text="Designation", font=("Century Gothic", 15), bg="white").place(x=20, y=340)
        txt_designation = Entry(self.root, textvariable=self.var_sup_designation, font=("Century Gothic", 15,), bg="lightyellow").place(x=180, y=340, width=180)

        lbl_address = Label(self.root, text="Address", font=("Century Gothic", 15), bg="white").place(x=20, y=380)
        self.txt_address = Text(self.root, font=("Century Gothic", 15,), bg="lightyellow")
        self.txt_address.place(x=180, y=380, width=300, height=55)

        lbl_desc = Label(self.root, text="Description", font=("Century Gothic", 15), bg="white").place(x=20, y=445)
        self.txt_desc = Text(self.root, font=("Century Gothic", 15,), bg="lightyellow")
        self.txt_desc.place(x=180, y=445, width=300, height=55)

        #COL2
        lbl_bankname= Label(self.root, text="Bank Name", font=("Century Gothic", 15), bg="white").place(x=380, y=60)
        txt_bankname = Entry(self.root, textvariable=self.var_sup_bankname, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=60, width=180)

        lbl_acname= Label(self.root, text="A/C Name", font=("Century Gothic", 15), bg="white").place(x=380, y=100)
        txt_acname = Entry(self.root, textvariable=self.var_sup_acname, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=100, width=180)

        lbl_acnumber= Label(self.root, text="A/C Number", font=("Century Gothic", 15), bg="white").place(x=380, y=140)
        txt_acnumber = Entry(self.root, textvariable=self.var_sup_acnumber, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=140, width=180)

        lbl_swiftcode= Label(self.root, text="SWIFT Code", font=("Century Gothic", 15), bg="white").place(x=380, y=180)
        txt_swiftcode = Entry(self.root, textvariable=self.var_sup_swiftcode, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=180, width=180)

        lbl_bnkadd = Label(self.root, text="Bank Address", font=("Century Gothic", 15), bg="white").place(x=380, y=220)
        self.txt_bnkadd = Text(self.root, font=("Century Gothic", 12), bg="lightyellow")
        self.txt_bnkadd.place(x=550, y=220, width=180, height=110)

        lbl_paymenterm= Label(self.root, text="Payment Terms", font=("Century Gothic", 15), bg="white").place(x=380, y=340)
        # txt_paymenterm = Entry(self.root, textvariable=self.var_sup_paymenterm, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=340, width=180)
        cmb_pterm = ttk.Combobox(self.root, textvariable=self.var_sup_paymenterm, values=("Select", "Cash on Delivery", "15 Days", "30 Days", "45 Days", "60 Days", "90 Days", "120 Days"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_pterm.place(x=550, y=340, width=180)
        cmb_pterm.current(0)

        # Button function
        btn_save = Button(self.root, text="Save",command=self.add, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=500, y=470, width=100, height=30)
        btn_udpate = Button(self.root, text="Update",command=self.update, font=("Century Gothic", 12), bg="darkblue", fg="white", cursor="hand2").place(x=610, y=470, width=100, height=30)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("Century Gothic", 12), bg="darkred", fg="white", cursor="hand2").place(x= 720, y=470, width=100, height=30)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("Century Gothic", 12), bg="darkgray", fg="white", cursor="hand2").place(x=830, y=470, width=100, height=30)
        btn_export = Button(self.root, text="Export",command=self.export_data, font=("Century Gothic", 12), bg="#2596be", fg="white", cursor="hand2").place(x=940, y=470, width=100, height=30)

        ## ===searchFram===
        SearchFrame = LabelFrame(self.root, text="Search Suppliers", font=("Century Gothic", 10, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x = 740, y = 40, width= 330, height= 55)

        ## options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "SUPP ID", "Name", "Email", "Contact"), state='readonly', justify=CENTER, font=("Century Gothic", 10))
        cmb_search.place(x=10, y=1, height=30,width=100)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Century Gothic", 10), bg="lightyellow", relief=RIDGE).place(x=115, y=1, width=140, height=30)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("Century Gothic", 10), bg="darkgreen", fg="white", cursor="hand2").place(x=260, y=1, width=60, height=30)


        # Supplier Table details box
        sup_frame = Frame(self.root, bd=3, relief=RIDGE)
        sup_frame.place(x=740, y=95, width=330, height=360)

        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)

        ## Add field into Supplier Table
        self.SupplierTable = ttk.Treeview(sup_frame, columns=("sid", "name", "contact", "fax", "pobox", "email", "cpersion", "designa", "address", "descript", "bankname", "acname", "acnumber", "swift", "bankadd", "pterms"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("sid", text="SUPP ID")
        self.SupplierTable.heading("name", text= "Name") 
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("fax", text="Fax No.")
        self.SupplierTable.heading("pobox", text="PO Box No.")
        self.SupplierTable.heading("email", text="E-mail")
        self.SupplierTable.heading("cpersion", text= "Contact Persion")
        self.SupplierTable.heading("designa", text="Designation")
        self.SupplierTable.heading("address",text="Address")
        self.SupplierTable.heading("descript", text="Description") 
        self.SupplierTable.heading("bankname", text="Bank Name")
        self.SupplierTable.heading("acname", text="Account Name")
        self.SupplierTable.heading("acnumber", text="Account Number")
        self.SupplierTable.heading("swift", text="SWIFT Code")
        self.SupplierTable.heading("bankadd", text="Bank Address")
        self.SupplierTable.heading("pterms", text="Payment Terms")
        self.SupplierTable["show"] = "headings"

        #supplyer filled size
        self.SupplierTable.column("sid", width=90)
        self.SupplierTable.column("name", width=100) 
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("fax", width=100)
        self.SupplierTable.column("pobox", width=100)
        self.SupplierTable.column("email", width=100)
        self.SupplierTable.column("cpersion", width=100)
        self.SupplierTable.column("designa", width=100)
        self.SupplierTable.column("address", width=100)
        self.SupplierTable.column("descript", width=100) 
        self.SupplierTable.column("bankname", width=100)
        self.SupplierTable.column("acname", width=100)
        self.SupplierTable.column("acnumber", width=100)
        self.SupplierTable.column("swift", width=100)
        self.SupplierTable.column("bankadd", width=100)
        self.SupplierTable.column("pterms", width=100)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

## Add data in data base

    def add(self):
        con = sqlite3.connect(database=r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() =="":
                messagebox.showerror("Error", "Supplier ID Must be Requried", parent = self.root)
            else:
                cur.execute("Select * from supplier where sid = ?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Supplier ID already exists, try different ID", parent  = self.root)
                else:
                    cur.execute("Insert into supplier (sid, name, contact, fax, pobox, email, cpersion, designa, address, descript, bankname, acname, acnumber, swift, bankadd, pterms) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                    self.var_sup_id.get(),
                                    self.var_sup_name.get(),
                                    self.var_sup_contact.get(),
                                    self.var_sup_fax.get(),
                                    self.var_sup_pobox.get(),
                                    self.var_sup_email.get(),
                                    self.var_sup_contactper.get(),
                                    self.var_sup_designation.get(),
                                    self.txt_address.get('1.0',END),
                                    self.txt_desc.get('1.0',END),
                                    self.var_sup_bankname.get(),
                                    self.var_sup_acname.get(),
                                    self.var_sup_acnumber.get(),
                                    self.var_sup_swiftcode.get(),
                                    self.txt_bnkadd.get('1.0', END),
                                    self.var_sup_paymenterm.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def show(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def get_data(self, ev): # show data function
        data = self.SupplierTable.focus()
        content = (self.SupplierTable.item(data))
        row = content['values']
        # print(row)
        self.var_sup_id.set(row[0]),
        self.var_sup_name.set(row[1]),
        self.var_sup_contact.set(row[2]),
        self.var_sup_fax.set(row[3]),
        self.var_sup_pobox.set(row[4]),
        self.var_sup_email.set(row[5]),
        self.var_sup_contactper.set(row[6]),
        self.var_sup_designation.set(row[7]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END, row[8]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END, row[9]),
        self.var_sup_bankname.set(row[10]),
        self.var_sup_acname.set(row[11]),
        self.var_sup_acnumber.set(row[12]),
        self.var_sup_swiftcode.set(row[13]),
        self.txt_bnkadd.delete('1.0', END),
        self.txt_bnkadd.insert(END, row[14]),
        self.var_sup_paymenterm.set(row[15]),


    def update(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error", "Supplier ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from supplier where sid = ?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Supplier ID",  parent = self.root)
                else:
                    cur.execute("Update supplier set name=?, contact=?, fax=?, pobox=?, email=?, cpersion=?, designa=?, address=?, descript=?, bankname=?, acname=?, acnumber=?, swift=?, bankadd=?, pterms=? where sid = ?",(
                                    self.var_sup_name.get(),
                                    self.var_sup_contact.get(),
                                    self.var_sup_fax.get(),
                                    self.var_sup_pobox.get(),
                                    self.var_sup_email.get(),
                                    self.var_sup_contactper.get(),
                                    self.var_sup_designation.get(),
                                    self.txt_address.get('1.0',END),
                                    self.txt_desc.get('1.0',END),
                                    self.var_sup_bankname.get(),
                                    self.var_sup_acname.get(),
                                    self.var_sup_acnumber.get(),
                                    self.var_sup_swiftcode.get(),
                                    self.txt_bnkadd.get('1.0', END),
                                    self.var_sup_paymenterm.get(),
                                    self.var_sup_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def delete(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error", "Supplier ID Must be requried", parent = self.root)
            else:
                cur.execute("Select * from supplier where sid = ?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Supplier ID",  parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from supplier where sid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent = self.root)
                        # self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)
        con.close()

    def clear(self):
        self.var_sup_id.set(""),    
        self.var_sup_name.set(""),
        self.var_sup_contact.set(""),
        self.var_sup_fax.set(""),
        self.var_sup_pobox.set(""),
        self.var_sup_email.set(""),
        self.var_sup_contactper.set(""),
        self.var_sup_designation.set(""),
        self.txt_address.delete('1.0',END),
        self.txt_desc.delete('1.0',END),
        self.var_sup_bankname.set(""),
        self.var_sup_acname.set(""),
        self.var_sup_acnumber.set(""),
        self.var_sup_swiftcode.set(""),
        self.txt_bnkadd.delete('1.0', END),
        self.var_sup_paymenterm.set("Select"),
        
        self.var_searchby.set("Select")
        self.var_searchtxt.set("Select")

        self.show()

    def export_data(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()

        cur.execute("Select * from supplier")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns = [ desc[0] for desc in cur.description])
        data = df.to_excel('supplier_data.xlsx', index=False)

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
                cur.execute("Select * from supplier where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() +"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = suppClass(root)
    root.mainloop()