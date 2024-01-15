from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import pandas as pd
import openpyxl

class itemClass: ## NEED TO ASSIGN SUPPLIER IN ITEM CODE
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x550+100+100")
        self.root.title("Items")
        self.root.iconbitmap("resoures\menu.ico")
        self.root.config(bg="white")
        self.root.focus_force()

        #define all variable
        self.var_item_id = StringVar()
        self.var_item_desc = StringVar()
        self.var_item_div = StringVar()
        self.var_item_brnd = StringVar()
        self.var_item_prod = StringVar()
        self.var_item_cat = StringVar()
        self.var_item_subcat = StringVar()
        self.var_item_size = StringVar()
        self.var_item_model = StringVar()
        self.var_item_price = StringVar()
        self.var_item_qty = StringVar()
        self.var_item_barc= StringVar()
        self.var_item_status= StringVar()
        self.var_supp = StringVar()
        self.supp_list=[]
        self.fetch_supp()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        title = Label(self.root, text="Items Creation and Details", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=40, y=10, width=1000)

        #content COL1
        lbl_itemid = Label(self.root, text="Item Code", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=85)
        txt_itemid = Entry(self.root, textvariable=self.var_item_id, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=85, width=350, height=30)

        lbl_desc = Label(self.root, text="Descriptions", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=120)
        txt_desc = Entry(self.root, textvariable=self.var_item_desc, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=120, width=350, height=30)

        lbl_div = Label(self.root, text="Division", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=155)
        txt_div = Entry(self.root, textvariable=self.var_item_div, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=155, width=350, height=30)

        lbl_brand = Label(self.root, text="Brand", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=190)
        txt_brand = Entry(self.root, textvariable=self.var_item_brnd, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=190, width=350, height=30)

        lbl_product = Label(self.root, text="Product", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=225)
        txt_product = Entry(self.root, textvariable=self.var_item_prod, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=225, width=350, height=30)

        lbl_cat = Label(self.root, text="Category", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=260)
        txt_cat = Entry(self.root, textvariable=self.var_item_cat, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=260, width=350, height=30)

        lbl_subcat= Label(self.root, text="Sub Category", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=295)
        txt_subcat = Entry(self.root, textvariable=self.var_item_subcat, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=295, width=350, height=30)

        lbl_size= Label(self.root, text="Size", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=330)
        txt_size = Entry(self.root, textvariable=self.var_item_size, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=330, width=350, height=30)

        lbl_model= Label(self.root, text="Model", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=365)
        txt_model = Entry(self.root, textvariable=self.var_item_model, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=365, width=350, height=30)

        lbl_price= Label(self.root, text="Price", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=400)
        txt_price = Entry(self.root, textvariable=self.var_item_price, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=400, width=350, height=30)

        lbl_barc= Label(self.root, text="Barcode", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=435)
        txt_barc = Entry(self.root, textvariable=self.var_item_barc, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=435, width=350, height=30)

        lbl_supp= Label(self.root, text="Assign Supplier", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=50)
        # txt_supp = Entry(self.root, textvariable=self.var_item_barc, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=445, width=300)
        cmb_supp = ttk.Combobox(self.root, textvariable=self.var_supp, values=self.supp_list, state='readonly', justify=LEFT, font=("Century Gothic", 12))
        cmb_supp.place(x=180, y=50, width=300, height=30)
        cmb_supp.current(0)

        lbl_quantity= Label(self.root, text="Quantity", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=470)
        txt_quantity= Entry(self.root, textvariable=self.var_item_qty, font=("Century Gothic", 12,), bg="lightyellow").place(x=180, y=470, width=300, height=30)

        lbl_status= Label(self.root, text="Status", font=("Century Gothic", 12, "bold"), bg="white").place(x=30, y=505)
        cmb_status = ttk.Combobox(self.root, textvariable=self.var_item_status, values=("Active", "Inactive"), state='readonly', justify=LEFT, font=("Century Gothic", 12))
        cmb_status.place(x=180, y=505, width=300, height=30)
        cmb_status.current(0)

        # Button function
        btn_save = Button(self.root, text="Save",command=self.add, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=520, y=505, width=100, height=30)
        btn_udpate = Button(self.root, text="Update",command=self.update, font=("Century Gothic", 12), bg="darkblue", fg="white", cursor="hand2").place(x=630, y=505, width=100, height=30)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("Century Gothic", 12), bg="darkred", fg="white", cursor="hand2").place(x= 740, y=505, width=100, height=30)
        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("Century Gothic", 12), bg="darkgray", fg="white", cursor="hand2").place(x=850, y=505, width=100, height=30)
        btn_export = Button(self.root, text="Export",command=self.export_data, font=("Century Gothic", 12), bg="#2596be", fg="white", cursor="hand2").place(x=960, y=505, width=100, height=30)

        ## ===searchFram===
        SearchFrame = LabelFrame(self.root, text="Search Items", font=("Century Gothic", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x = 550, y = 40, width= 520, height= 60)

        ## options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "item_code", "Description", "Model"), state='readonly', justify=CENTER, font=("Century Gothic", 12))
        cmb_search.place(x=10, y=1, height=30,width=140)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Century Gothic", 12), bg="lightyellow", relief=RIDGE).place(x=165, y=1, width=230, height=30)
        btn_search = Button(SearchFrame, text="Search",command=self.search, font=("Century Gothic", 12), bg="darkgreen", fg="white", cursor="hand2").place(x=410, y=1, width=100, height=30)


        # Supplier Table details box
        item_frame = Frame(self.root, bd=3, relief=RIDGE)
        item_frame.place(x=550, y=100, width=520, height=400)

        scrolly = Scrollbar(item_frame, orient=VERTICAL)
        scrollx = Scrollbar(item_frame, orient=HORIZONTAL)

        ## Add field into Supplier Table
        self.ItemTable = ttk.Treeview(item_frame, columns=("item_code", "description", "division", "brand", "product", "category", "subcategory", "size", "model", "price", "barcode", "supplier", "quantity", "status"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ItemTable.xview)
        scrolly.config(command=self.ItemTable.yview)

        self.ItemTable.heading("item_code", text="Item Code")
        self.ItemTable.heading("description", text= "Description") 
        self.ItemTable.heading("division", text="Division")
        self.ItemTable.heading("brand", text="Brand")
        self.ItemTable.heading("product", text="Product")
        self.ItemTable.heading("category", text="Category")
        self.ItemTable.heading("subcategory", text= "Sub Category")
        self.ItemTable.heading("size", text="Size")
        self.ItemTable.heading("model",text="Model")
        self.ItemTable.heading("price", text="Price") 
        self.ItemTable.heading("barcode", text="Barcode")
        self.ItemTable.heading("supplier", text="Supplier")
        self.ItemTable.heading("quantity", text="Quantity")        
        self.ItemTable.heading("status", text="Status")
        self.ItemTable["show"] = "headings"

        #supplyer filled size
        self.ItemTable.column("item_code", width=100)
        self.ItemTable.column("description", width=200)
        self.ItemTable.column("division", width=100)
        self.ItemTable.column("brand", width=100)
        self.ItemTable.column("product", width=100)
        self.ItemTable.column("category", width=100)
        self.ItemTable.column("subcategory", width=100)
        self.ItemTable.column("size", width=100)
        self.ItemTable.column("model", width=100)
        self.ItemTable.column("price", width=100) 
        self.ItemTable.column("barcode", width=100)
        self.ItemTable.column("supplier", width=100)
        self.ItemTable.column("quantity", width=100)         
        self.ItemTable.column("status", width=100)

        self.ItemTable.pack(fill=BOTH, expand=1)
        self.ItemTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

## Add data in data base

    def add(self):
        con = sqlite3.connect(database=r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() =="" or self.var_supp.get()=="":
                messagebox.showerror("Error", "Item Code Must be Requried", parent = self.root)
            else:
                cur.execute("Select * from items where item_code = ?", (self.var_item_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Item Code already exists, try different Item Code", parent  = self.root)
                else:
                    cur.execute("Insert into items (item_code, description, division, brand, product, category, subcategory, size, model, price, barcode, supplier, quantity, status) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(
                                    self.var_item_id.get(),
                                    self.var_item_desc.get(),
                                    self.var_item_div.get(),
                                    self.var_item_brnd.get(),
                                    self.var_item_prod.get(),
                                    self.var_item_cat.get(),
                                    self.var_item_subcat.get(),
                                    self.var_item_size.get(),
                                    self.var_item_model.get(),
                                    self.var_item_price.get(),
                                    self.var_item_barc.get(),
                                    self.var_supp.get(),
                                    self.var_item_qty.get(),
                                    self.var_item_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Item Code Added Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def show(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from items")
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def get_data(self, ev): # show data function
        data = self.ItemTable.focus()
        content = (self.ItemTable.item(data))
        row = content['values']
        # print(row)
        self.var_item_id.set(row[0]),
        self.var_item_desc.set(row[1]),
        self.var_item_div.set(row[2]),
        self.var_item_brnd.set(row[3]),
        self.var_item_prod.set(row[4]),
        self.var_item_cat.set(row[5]),
        self.var_item_subcat.set(row[6]),
        self.var_item_size.set(row[7]),
        self.var_item_model.set(row[8]),
        self.var_item_price.set(row[9]),
        self.var_item_barc.set(row[10]),
        self.var_supp.set(row[11]),
        self.var_item_qty.set(row[12]),
        self.var_item_status.set(row[13]),


    def update(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() == "":
                messagebox.showerror("Error", "Item Code Must be requried", parent = self.root)
            else:
                cur.execute("Select * from items where item_code = ?", (self.var_item_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Item Code",  parent = self.root)
                else:
                    cur.execute("Update items set description=?, division=?, brand=?, product=?, category=?, subcategory=?, size=?, model=?, price=?, barcode=?, supplier=?, quantity=?, status=? where item_code=?",(
                                    self.var_item_desc.get(),
                                    self.var_item_div.get(),
                                    self.var_item_brnd.get(),
                                    self.var_item_prod.get(),
                                    self.var_item_cat.get(),
                                    self.var_item_subcat.get(),
                                    self.var_item_size.get(),
                                    self.var_item_model.get(),
                                    self.var_item_price.get(),
                                    self.var_item_barc.get(),
                                    self.var_supp.get(),
                                    self.var_item_qty.get(),
                                    self.var_item_status.get(),
                                    self.var_item_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Item Code Updated Successfully", parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def delete(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_item_id.get() == "":
                messagebox.showerror("Error", "Item Code Must be requried", parent = self.root)
            else:
                cur.execute("Select * from items where item_code = ?", (self.var_item_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Item Code",  parent = self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from items where item_code=?",(self.var_item_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Item Code Deleted Successfully", parent = self.root)
                        # self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)
        con.close()

    def clear(self):
        self.var_item_id.set(""),    
        self.var_item_desc.set(""),
        self.var_item_div.set(""),
        self.var_item_brnd.set(""),
        self.var_item_prod.set(""),
        self.var_item_cat.set(""),
        self.var_item_subcat.set(""),
        self.var_item_size.set(""),
        self.var_item_model.set(""),
        self.var_item_price.set(""),
        self.var_item_barc.set(""),
        self.var_supp.set("Select"),
        self.var_item_qty.set(""),
        self.var_item_status.set(""),        
        
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")

        self.show()

    def export_data(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()

        cur.execute("Select * from items")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns = [ desc[0] for desc in cur.description])
        data = df.to_excel('itemlist_data.xlsx', index=False)

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
                cur.execute("Select * from items where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() +"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ItemTable.delete(*self.ItemTable.get_children())
                    for row in rows:
                        self.ItemTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()
    
    def fetch_supp(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from supplier")
            supp = cur.fetchall()
            self.supp_list.append("Empty")
            if len(supp)>0:
                del self.supp_list[:]
                self.supp_list.append("Select")
                for i in supp:
                    self.supp_list.append(i[0])        
        
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = itemClass(root)
    root.mainloop()