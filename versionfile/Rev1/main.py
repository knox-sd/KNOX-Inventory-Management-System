from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from employee import empClass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x700+0+0")
        self.root.title("KNOX Enterprise Management System | v.1")
        self.root.iconbitmap("")
        self.root.config(bg="white")
        # --title--
        self.icon_title = PhotoImage(file= "resoures/applogo.png")
        title=Label(self.root, text = "KNOX Enterprise Management System",image=self.icon_title,compound=LEFT, font= ("arial", 35, "bold"), bg="#000080", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        #title=Label(self.root, text = "Inverntory Management System", font= ("arial", 40, "bold")).place(x=0,y=0,relheight=1,height=70)

        # btn_logout==
        btn_logout =Button(self.root, text= "Logout", font=("Helvetica", 15, "bold"), bg="#98F5FF", cursor="hand2").place(x=1140, y=10, width=110, height=45)
        # -- User Status & CLOCK--
        self.lbl_clock=Label(self.root, text = "Welcome to KNOX Enterprise Management System\t\t Date: DD:MM:YYYY\t\t Time: HH:MM:SS", font= ("times new roman", 15,), bg="#737373", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # -- footer contact status
        self.lbl_clock=Label(self.root, text = "KNOX Enterprise Management System | Developed by KNOX Co.\n For any Technical issues, Contact: +977 xxxxxxx", font= ("times new roman", 15,), bg="#737373", fg="white")
        self.lbl_clock.place(x=0, y=645, relwidth=1, height=50)


        ## Left Menu
        self.Menulogo=Image.open("resoures/Menulogo.png")
        self.Menulogo=self.Menulogo.resize((250,200), Image.ADAPTIVE)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)
        
        leftMenu = Frame(self.root, bd = 2, relief=RIDGE, bg="white")
        leftMenu.place(x=0, y=100, width=200, height=540)

        lbl_menuLogo = Label(leftMenu,image=self.Menulogo)
        lbl_menuLogo.pack(side = TOP, fill =X)

        # btn_menu==        
        lbl_menu =Label(leftMenu, text= "Menu", font=("arial", 20), bg="Gray").pack(side=TOP, fill= X)
        self.icon_side = PhotoImage(file= "resoures/side2.png")
        
        btn_employee = Button(leftMenu, text= "Employee",command=self.employee,image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        
        btn_supplier = Button(leftMenu, text= "Supplier",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        btn_category = Button(leftMenu, text= "Category",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        btn_product = Button(leftMenu, text= "Product",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        btn_sales = Button(leftMenu, text= "Sales",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        btn_stock= Button(leftMenu, text= "Inventory",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)
        btn_exit = Button(leftMenu, text= "Exit",image=self.icon_side,compound=LEFT, padx=5,anchor="w", font=("arial", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill= X)

        # Content
        self.lbl_employee=Label(self.root, text = "Total Employee\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_employee.place(x=250, y=150, height=150, width=300)
        
        self.lbl_supplier=Label(self.root, text = "Total Supplier\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_supplier.place(x=600, y=150, height=150, width=300)

        self.lbl_category=Label(self.root, text = "Total Category\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_category.place(x=950, y=150, height=150, width=300)

        self.lbl_Product=Label(self.root, text = "Total Product\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_Product.place(x=250, y=350, height=150, width=300)
        
        self.lbl_sales=Label(self.root, text = "Total Sales\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_sales.place(x=600, y=350, height=150, width=300)

        self.lbl_inventory=Label(self.root, text = "Total Sales\n[ 0 ]",bd = 5, relief=RIDGE, font= ("times new roman", 18, "bold"), bg="#00997a", fg="white")
        self.lbl_inventory.place(x=950, y=350, height=150, width=300)

#reflect employee moudle in main
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = empClass(self.new_win)
        
        
if __name__=="__main__":
    root=Tk()
    obj = IMS(root)
    root.mainloop()