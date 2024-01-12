from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3

class suppClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x510+200+130")
        self.root.title("Suppliers")
        self.root.iconbitmap("")
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
        txt_paymenterm = Entry(self.root, textvariable=self.var_sup_paymenterm, font=("Century Gothic", 15,), bg="lightyellow").place(x=550, y=340, width=180)

        # Button function
        btn_save = Button(self.root, text="Save", font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=500, y=470, width=100, height=30)
        btn_udpate = Button(self.root, text="Update", font=("Century Gothic", 12), bg="darkblue", fg="white", cursor="hand2").place(x=610, y=470, width=100, height=30)
        btn_delete = Button(self.root, text="Delete", font=("Century Gothic", 12), bg="darkred", fg="white", cursor="hand2").place(x= 720, y=470, width=100, height=30)
        btn_clear = Button(self.root, text="Clear", font=("Century Gothic", 12), bg="darkgray", fg="white", cursor="hand2").place(x=830, y=470, width=100, height=30)
        btn_export = Button(self.root, text="Export", font=("Century Gothic", 12), bg="#2596be", fg="white", cursor="hand2").place(x=940, y=470, width=100, height=30)

## ===searchFram===
        SearchFrame = LabelFrame(self.root, text="Search Suppliers", font=("Century Gothic", 10, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x = 740, y = 40, width= 330, height= 55)

        # # options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "SUPP ID", "Name", "Email", "Contact"), state='readonly', justify=CENTER, font=("Century Gothic", 10))
        cmb_search.place(x=10, y=1, height=30,width=100)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Century Gothic", 10), bg="lightyellow", relief=RIDGE).place(x=115, y=1, width=140, height=30)
        btn_search = Button(SearchFrame, text="Search", font=("Century Gothic", 10), bg="darkgreen", fg="white", cursor="hand2").place(x=260, y=1, width=60, height=30)



        # Supplier Table details box
        supp_frame = Frame(self.root, bd=3, relief=RIDGE)
        supp_frame.place(x=740, y=95, relwidth=1, height=360)
        
        scrolly = Scrollbar(supp_frame, orient=VERTICAL)
        scrollx = Scrollbar(supp_frame, orient=VERTICAL)

        
'''supplier ID
    -supplier name
    -supplier contact no
    -suppleir fax no
    -supplier email address
    -supplier Address
    -supplier point of contact name and title
    -supplier Paymnet Terms
    -Descriptions
    -Registration date
    -----------------------
    -bank name
    -beneficiary name
    -account number
    -SWIFT code
    -Bank Address
'''



if __name__ == "__main__":
    root = Tk()
    obj = suppClass(root)
    root.mainloop()