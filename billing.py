from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import time
import sqlite3

class billClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("KNOX Inventory Management System | v.02")
        self.root.iconbitmap("resoures\mainlogo.ico")
        self.root.config(bg="gray")
        self.cart_list=[] ## empty list to add items in cart

        # -- User Status & CLOCK--
        self.lbl_clock=Label(self.root, text = "Welcome to KNOX Inventory Management System\t\t Date: DD:MM:YYY\t\t Time: HH:MM:SS", font= ("times new roman", 15), bg="#00997a", fg="white")
        self.lbl_clock.place(x=0, y=0, relwidth=1, height=30)

        ##Product Frame
        self.var_search = StringVar()
        
        ProductFrame = Frame(self.root, bd=4,relief=RIDGE, bg="white")
        ProductFrame.place(x=10, y=80, width=380, height=550)

        Product_Title = Label(ProductFrame, text="All Items List", font=("Century Gothic", 20, "bold"), bg="#000080", fg="white").pack(side=TOP, fill=X)

        ProductFrame2 = Frame(ProductFrame, bd=4,relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=370, height=90)

        lbl_search = Label(ProductFrame2, text="Search Product | By Name ",font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=2, y=5)

        lbl_name = Label(ProductFrame2,text="Product Name", font=("times new roman", 13, "bold"), bg="white").place(x=2, y=45)
        text_name = Entry(ProductFrame2,textvariable=self.var_search, font=("times new roman", 15), bg="lightyellow").place(x=120, y=45, width=150, height=28)

        btn_show_all = Button(ProductFrame2, text="Show All",command=self.show, font=("goudy old style", 15), bg="green", fg="white", cursor="hand2").place(x=275, y=7, width=85, height=28)
        btn_search = Button(ProductFrame2, text="Search",command=self.search, font=("goudy old style", 15), bg="#000080", fg="white", cursor="hand2").place(x=275, y=46, width=85, height=28)


        # Items Table details box
        ProductFrame3 = Frame(ProductFrame, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=370, height=380)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        ## Add field into Product Frame
        self.items_Table = ttk.Treeview(ProductFrame3, columns=("item_code", "description", "price", "quantity", "status"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        # self.items_Table = ttk.Treeview(ProductFrame3, columns=("item_code", "description", "division", "brand", "product", "category", "subcategory", "size", "model", "price", "barcode", "supplier", "quantity", "status"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.items_Table.xview)
        scrolly.config(command=self.items_Table.yview)

        self.items_Table.heading("item_code", text="Item Code")
        self.items_Table.heading("description", text= "Description") 
        # self.items_Table.heading("division", text="Division")
        # self.items_Table.heading("brand", text="Brand")
        # self.items_Table.heading("product", text="Product")
        # self.items_Table.heading("category", text="Category")
        # self.items_Table.heading("subcategory", text= "Sub Category")
        # self.items_Table.heading("size", text="Size")
        # self.items_Table.heading("model",text="Model")
        self.items_Table.heading("price", text="Price") 
        # self.items_Table.heading("barcode", text="Barcode")
        # self.items_Table.heading("supplier", text="Supplier")
        self.items_Table.heading("quantity", text="QTY")        
        self.items_Table.heading("status", text="Status")
        self.items_Table["show"] = "headings"

        #filled size
        self.items_Table.column("item_code", width=100)
        self.items_Table.column("description", width=200) 
        # self.items_Table.column("division", width=100)
        # self.items_Table.column("brand", width=100)
        # self.items_Table.column("product", width=100)
        # self.items_Table.column("category", width=100)
        # self.items_Table.column("subcategory", width=100)
        # self.items_Table.column("size", width=100)
        # self.items_Table.column("model", width=100)
        self.items_Table.column("price", width=70) 
        # self.items_Table.column("barcode", width=100)
        # self.items_Table.column("supplier", width=100)
        self.items_Table.column("quantity", width=50)         
        self.items_Table.column("status", width=70)

        self.items_Table.pack(fill=BOTH, expand=1)
        self.items_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        lbl_note = Label(ProductFrame, text="Note: 'Enter 0 Quantity to remove product from the Cart'", font=("goudy old style",11), anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)

        ## Customer Frame
        self.var_cusname = StringVar()
        self.var_cuscontact = StringVar()
        
        CustomerFrame = Frame(self.root, bd=4,relief=RIDGE, bg="white")
        CustomerFrame.place(x=390, y=80, width=530, height=100)        

        Customer_Title = Label(CustomerFrame, text="Customer Details", font=("Century Gothic", 20,"bold"), bg="lightgray", fg="black").pack(side=TOP, fill=X)

        lbl_cusname = Label(CustomerFrame,text="Name", font=("goudy old style", 15), bg="white").place(x=5, y=45)
        text_cusname = Entry(CustomerFrame,textvariable=self.var_cusname, font=("goudy old style", 15), bg="lightyellow").place(x=65, y=47, width=180, height=28)

        lbl_contact = Label(CustomerFrame,text="Contact No.", font=("goudy old style", 15), bg="white").place(x=260, y=45)
        text_contact = Entry(CustomerFrame,textvariable=self.var_cuscontact, font=("goudy old style", 15), bg="lightyellow").place(x=370, y=47, width=138, height=28)

        ##Main Frame for Cal_Cart
        Cal_Cart_Frame = Frame(self.root, bd=3,relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=390, y=180, width=530, height=350)        

        ## Calculator Frame
        self.var_cal_input = StringVar()
        
        Cal_Frame = Frame(Cal_Cart_Frame, bd=8,relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=270, height=330)        

        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=21, bd=10, relief=GROOVE, state='readonly', justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7 = Button(Cal_Frame, text='7', font=("arial", 15, "bold"), command=lambda:self.get_input(7), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', font=("arial", 15, "bold"),command=lambda:self.get_input(8), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9', font=("arial", 15, "bold"),command=lambda:self.get_input(9), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+', font=("arial", 15, "bold"),command=lambda:self.get_input('+'), bd=5, width=4, pady=10, cursor='hand2').grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4', font=("arial", 15, "bold"),command=lambda:self.get_input(4), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5', font=("arial", 15, "bold"),command=lambda:self.get_input(5), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6', font=("arial", 15, "bold"),command=lambda:self.get_input(6), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-', font=("arial", 15, "bold"),command=lambda:self.get_input('-'), bd=5, width=4, pady=10, cursor='hand2').grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1', font=("arial", 15, "bold"),command=lambda:self.get_input(1), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2', font=("arial", 15, "bold"),command=lambda:self.get_input(2), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3', font=("arial", 15, "bold"),command=lambda:self.get_input(3), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='x', font=("arial", 15, "bold"),command=lambda:self.get_input('*'), bd=5, width=4, pady=10, cursor='hand2').grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0', font=("arial", 15, "bold"),command=lambda:self.get_input(0), bd=5, width=4, pady=10, cursor='hand2').grid(row=4, column=0)
        btn_C = Button(Cal_Frame, text='C', font=("arial", 15, "bold"), command=self.clear_cal, bd=5, width=4, pady=10, cursor='hand2').grid(row=4, column=1)
        btn_eql = Button(Cal_Frame, text='=', font=("arial", 15, "bold"), command=self.perform_cal, bd=5, width=4, pady=10, cursor='hand2').grid(row=4, column=2)
        btn_mul = Button(Cal_Frame, text='/', font=("arial", 15, "bold"),command=lambda:self.get_input('/'), bd=5, width=4, pady=10, cursor='hand2').grid(row=4, column=3)


        # Cart_Frame
        CartFrame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE)
        CartFrame.place(x=280, y=10, width=240, height=330)

        self.cart_Title = Label(CartFrame, text="Cart \t Total Product: [0]", font=("goudy old style", 15), bg="lightgray", fg="black")
        self.cart_Title.pack(side=TOP, fill=X)

        scrolly = Scrollbar(CartFrame, orient=VERTICAL)
        scrollx = Scrollbar(CartFrame, orient=HORIZONTAL)

        ## Add field into Cart_Frame
        self.cart_Table = ttk.Treeview(CartFrame, columns=("item_code", "description", "price", "quantity"),yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        # self.cart_Table = ttk.Treeview(CartFrame, columns=("item_code", "description", "division", "brand", "product", "category", "subcategory", "size", "model", "price", "barcode", "supplier", "quantity", "status"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)

        # self.cart_Table.heading("no", text="NO.")
        self.cart_Table.heading("item_code", text="ITEM CODE")
        self.cart_Table.heading("description", text= "DESCRIPTION") 
        self.cart_Table.heading("price", text="PRICE") 
        self.cart_Table.heading("quantity", text="QTY")
        self.cart_Table["show"] = "headings"

        #filled size
        # self.cart_Table.column("no", width=40)
        self.cart_Table.column("item_code", width=100)
        self.cart_Table.column("description", width=200)
        self.cart_Table.column("price", width=90)      
        self.cart_Table.column("quantity", width=50)

        self.cart_Table.pack(fill=BOTH, expand=1)
        self.cart_Table.bind("<ButtonRelease-1>", self.get_data_cart) ##change getdata2
        self.show()


        ## ADD Card Buttom
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        
        Add_cartwidgets_Frame = Frame(self.root, bd=2,relief=RIDGE, bg="white")
        Add_cartwidgets_Frame.place(x=390, y=530, width=530, height=100)        

        lbl_p_name = Label(Add_cartwidgets_Frame, text="Product Name", font=("times new roman", 15), bg="white").place(x=5,y=5)
        txt_p_name = Entry(Add_cartwidgets_Frame, textvariable=self.var_pname , font=("times new roman", 11), bg="lightyellow", state='readonly').place(x=5,y=35, width=250, height=22)

        lbl_p_price = Label(Add_cartwidgets_Frame, text="Price Per Qty", font=("times new roman", 15), bg="white").place(x=260,y=5)
        txt_p_price = Entry(Add_cartwidgets_Frame, textvariable=self.var_price , font=("times new roman", 15), bg="lightyellow", state='readonly',justify=RIGHT).place(x=260,y=35, width=120, height=22)

        lbl_p_qty = Label(Add_cartwidgets_Frame, text="Quantity", font=("times new roman", 15), bg="white").place(x=410,y=5)
        txt_p_qty = Entry(Add_cartwidgets_Frame, textvariable=self.var_qty, font=("times new roman", 15), bg="lightyellow",justify=CENTER).place(x=410,y=35, width=100, height=20)

        self.lbl_instock = Label(Add_cartwidgets_Frame, text="In Stock ", font=("times new roman", 15), bg="white")
        self.lbl_instock.place(x=5,y=65)

        btn_clear_cart = Button(Add_cartwidgets_Frame, text="Clear",command=self.clear_cart, font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2").place(x=210, y=63, height=29, width=100)
        btn_add_cart = Button(Add_cartwidgets_Frame, text="Add | Update Cart",command=self.add_update_cart, font=("times new roman", 15, "bold"), bg="orange", cursor="hand2").place(x=320, y=63, height=29, width=190)

        # self.get_data()

        ###Billing Area
        billFrame= Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billFrame.place(x=920, y=80, height=450, width=360)

        Bill_Title = Label(billFrame, text="Customer Bill", font=("Century Gothic", 20,"bold"), bg="red", fg="white").pack(side=TOP, fill=X)
        scrolly = Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        
        self.txt_bill = Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill.yview)

        ##Billing Buttons
        bill_Menu_Frame= Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_Menu_Frame.place(x=920, y=530, width=360, height=140)

        self.lbl_amt = Label(bill_Menu_Frame, text='Bill Amount\n[0]', font=("goudy old style", 14, "bold"), bg="#00997a", fg="white")
        self.lbl_amt.place(x=2,y=6, width=120, height=60)

        self.lbl_dis = Label(bill_Menu_Frame, text='Discount\n[5%]', font=("goudy old style", 14, "bold"), bg="#00997a", fg="white")
        self.lbl_dis.place(x=128,y=6, width=100, height=60)

        self.lbl_netpay = Label(bill_Menu_Frame, text='Net Pay\n[0]', font=("goudy old style", 14, "bold"), bg="#00997a", fg="white")
        self.lbl_netpay.place(x=235,y=6, width=120, height=60)

        btn_print = Button(bill_Menu_Frame, text='Print', font=("goudy old style", 14, "bold"),cursor='hand2', bg="orange", fg="white")
        btn_print.place(x=2,y=75, width=120, height=50)

        btn_cler = Button(bill_Menu_Frame, text='Clear All',command=self.clear_all, font=("goudy old style", 14, "bold"),cursor='hand2', bg="gray", fg="white")
        btn_cler.place(x=128,y=75, width=100, height=50)

        btn_generate = Button(bill_Menu_Frame, text='Generate/\nSave Bill',command=self.generate_bill, font=("goudy old style", 14, "bold"),cursor='hand2', bg="#000080", fg="white")
        btn_generate.place(x=235,y=75, width=120, height=50)

        self.show()
        # self.bill_top()

        self.update_date_time()

## All Calculator function
    def get_input(self,num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')
    
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

##data fetch from items mudule
    def show(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            cur.execute("Select item_code, description, price, quantity, status from items where status = 'Active'")
            rows = cur.fetchall()
            self.items_Table.delete(*self.items_Table.get_children())
            for row in rows:
                self.items_Table.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()
        
    def search(self):
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search Input Requried!", parent = self.root)
            else:
                cur.execute("Select item_code, description, price, quantity, status from items where description LIKE '%" + self.var_search.get() +"%' and status = 'Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.items_Table.delete(*self.items_Table.get_children())
                    for row in rows:
                        self.items_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!", parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()

    def get_data(self, ev): # show data function
        data = self.items_Table.focus()
        content = (self.items_Table.item(data))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1') #qty set 1

    def get_data_cart(self, ev): # show data function
        data2 = self.cart_Table.focus()
        content = (self.cart_Table.item(data2))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3]) #get data from cart
        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])


    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', "Please select the Product", parent = self.root)

        elif self.var_qty.get() == '':
            messagebox.showerror('Error', "Quantity is Requried", parent = self.root)

        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error', "Invalid Quantity", parent = self.root)

        else:
            # price_cal = float(int(self.var_qty.get()) * float(self.var_price.get()))
            price_cal = self.var_price.get()
            
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_qty.get(), self.var_stock.get()]
            # self.cart_list.append(cart_data)
            # print(cart_data)
            
            ##update cart(if bill same item multipul times)
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    
                    present = 'yes'
                    break
                index_ += 1
            
            # print(present, index_)
            if present =='yes':
                condt = messagebox.askyesno('Confirm', "Product already present \nDo you want to Update| Remove from Cart List")
                if condt == True:
                    if self.var_qty.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2] = price_cal #price
                        self.cart_list[index_][3] = self.var_qty.get() #Qty
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amt = self.bill_amt + (float(row[2]) * int(row[3]))
        
        self.discount = (self.bill_amt*5)/ 100
        
        self.net_pay = self.bill_amt - self.discount
        self.lbl_amt.config(text=f'Bill Amount\n [{str(self.bill_amt)}]')
        self.lbl_netpay.config(text=f'Net Pay\n [{str(self.net_pay)}]')
        self.cart_Title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.cart_Table.delete(*self.cart_Table.get_children())
            for row in self.cart_list:
                self.cart_Table.insert('', END, values=row)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)

    ## Bill Generate ##
    def generate_bill(self):
        if self.var_cusname.get()=='' or self.var_cuscontact.get()=='':
            messagebox.showerror("Error", f"Customer details are Requried",  parent = self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", f"Please add products to the Cart!!",  parent = self.root)
        else:
            ## bill top
            self.bill_top()
            # bill Middle
            self.bill_middle()
            # bill bottom
            self.bill_bottom()

            fp = open(f'invoices/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated/Saved", parent=self.root)


    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tKNOX Inventory System
\t Phone No. 98000***, Nepal-0123
{str("=" * 41)}
Customer Name: {self.var_cusname.get()}
Ph no. {self.var_cuscontact.get()}
Bill No. {str(self.invoice)} \t\t\t Date: {str(time.strftime("%d/%m/%Y"))}
{str("=" * 41)}
    Product Name \t\t\tQTY    Price
{str("=") * 41}
        '''
        self.txt_bill.delete('1.0', END)
        self.txt_bill.insert('1.0', bill_top_temp)


    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("=" * 41)}
Bill Amount\t\t\t    Rs.{self.bill_amt}
Discount-\t\t\t    Rs.{self.discount}
Net Pay\t\t\t    Rs.{self.net_pay}
{str("=" * 41)}\n
        '''
        self.txt_bill.insert(END, bill_bottom_temp)

    def bill_middle(self): #update product list qty status
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid = str(row[0])
                name = str(row[1])
                qty = int(row[4])- int(row[3])
                if int(row[3]) == int(row[4]):
                    status = 'Inactive'
                if int(qty) != int(row[4]):
                    status = 'Active'                    
                price = str(float(row[2]) * int(row[3]))
                self.txt_bill.insert(END, "\n "+name+"\t\t\t"+row[3]+"    Rs."+price) 
                
                ##update Qty in product table
                cur.execute('Update items set quantity=?, status=? where item_code=?',(
                    qty,
                    status,
                    pid,
                ))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set(r'') #get data from cart
        self.lbl_instock.config(text=f"In Stock")
        self.var_stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cusname.set('')
        self.var_cuscontact.set('')
        self.txt_bill.delete('1.0', END)
        self.cart_Title.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        upd_time = time.strftime("%H:%M:%S")
        upd_date = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text = f"Welcome to KNOX Inventory Management System\t\t Date: {str(upd_date)}\t\t Time: {str(upd_time)}")
        self.lbl_clock.after(200,self.update_date_time)


if __name__=="__main__":
    root=Tk()
    obj = billClass(root)
    root.mainloop()