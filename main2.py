from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
import time
from employee import empClass
from supplier import suppClass
from customer import cusClass
from items import itemClass
from sales import salesClass
from billing import billClass

class KNOX:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x700+0+0")
        self.root.title("KNOX Inventory Management System | v.02")
        self.root.iconbitmap("resoures\mainlogo.ico")
        self.root.config(bg="gray")

        # -- User Status & CLOCK--
        self.lbl_clock=Label(self.root, text = "Welcome to KNOX Inventory Management System\t\t Date: DD:MM:YYY\t\t Time: HH:MM:SS", font= ("times new roman", 15), bg="#00997a", fg="white")
        self.lbl_clock.place(x=0, y=0, relwidth=1, height=30)

        # -- footer contact status
        # self.lbl_clock=Label(self.root, text = "KNOX Enterprise Management System | Developed by KNOX Co.\n For any Technical issues, Contact: +977 xxxxxxx", font= ("times new roman", 15,), bg="#737373", fg="white")
        # self.lbl_clock.place(x=0, y=645, relwidth=1, height=50)
        
        self.update_date_time()
        
        #Menu list
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)  # Corrected here
        
        #Create a Menu item
        file_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "File", menu=file_menu)
        file_menu.add_command(label="Create New User",compound='left', underline=0)
        file_menu.add_command(label="Changer User",compound='left', underline=0)
        file_menu.add_command(label="Change Password")
        file_menu.add_command(label="Assign Roles")
        file_menu.add_command(label="Log Out")
        file_menu.add_command(label="Exit")


        Regis_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "New Registration", menu=Regis_menu)
        Regis_menu.add_command(label="Suppliers", command=self.supplier)
        Regis_menu.add_command(label="Customers", command=self.customer)
        Regis_menu.add_command(label="Reports")


        finance_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "Accounts", menu=finance_menu)
        finance_menu.add_command(label="Receivable")
        finance_menu.add_command(label="Payable")
        finance_menu.add_command(label="Balance Sheet")
        finance_menu.add_command(label="Payment Request")


        purchase_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "Purchasing", menu=purchase_menu)
        purchase_menu.add_command(label="Purchse Order")
        purchase_menu.add_command(label="Received Order")
        purchase_menu.add_command(label="Reports")

        sales_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "Sales", menu=sales_menu)
        sales_menu.add_command(label="Billing", command=self.billing)
        sales_menu.add_command(label="View Customer Billing", command=self.sales)
        sales_menu.add_command(label="Daily Sales Report") #including pending delivery
        sales_menu.add_command(label="Delivery List")
        sales_menu.add_command(label="Return Material Authorization")
        sales_menu.add_command(label="Submission List")

        inventory_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "Inventory", menu=inventory_menu)
        inventory_menu.add_command(label="Inventory Stock")
        inventory_menu.add_command(label="Inventory Stock Aging")
        inventory_menu.add_command(label="Item PSI Report")
        inventory_menu.add_command(label="Item Creation", command=self.items)

        master_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "Master Lists", menu=master_menu)
        master_menu.add_command(label="Promotions")
        master_menu.add_command(label="Customer Price List")
        master_menu.add_command(label="Supplier Price List")
        master_menu.add_command(label="All Reports")


        payroll_menu = Menu(my_menu, tearoff="off")
        my_menu.add_cascade(label = "HR and Payroll", menu=payroll_menu)
        payroll_menu.add_command(label="Employee", command=self.employee)
        payroll_menu.add_command(label="Performance")
        payroll_menu.add_command(label="Report Cards")


        # Content
        # self.lbl_employee=Label(self.root, text = "Total Employee\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_employee.place(x=150, y=150, height=150, width=300)
        
        # self.lbl_supplier=Label(self.root, text = "Total Supplier\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_supplier.place(x=500, y=150, height=150, width=300)

        # self.lbl_category=Label(self.root, text = "Total Category\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_category.place(x=850, y=150, height=150, width=300)

        # self.lbl_Product=Label(self.root, text = "Total Product\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_Product.place(x=150, y=350, height=150, width=300)
        
        # self.lbl_sales=Label(self.root, text = "Total Sales\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_sales.place(x=500, y=350, height=150, width=300)

        # self.lbl_inventory=Label(self.root, text = "Total Sales\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        # self.lbl_inventory.place(x=850, y=350, height=150, width=300)



#reflect others moudle in main dashboard

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = empClass(self.new_win)
    
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = suppClass(self.new_win)

    def customer(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = cusClass(self.new_win)
    
    def items(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = itemClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = billClass(self.new_win)

    def update_date_time(self):
        upd_time = time.strftime("%H:%M:%S")
        upd_date = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text = f"Welcome to KNOX Inventory Management System\t\t Date: {str(upd_date)}\t\t Time: {str(upd_time)}")
        self.lbl_clock.after(200,self.update_date_time)


if __name__=="__main__":
    root=Tk()
    obj = KNOX(root)
    root.mainloop()