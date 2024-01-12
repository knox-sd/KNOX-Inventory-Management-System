from tkinter import *
from PIL import Image, ImageTk ##change jpng or other photos convert into png
from tkinter import ttk, messagebox
import sqlite3
import os
# import pandas as pd
# import openpyxl

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1070x550+100+100")
        self.root.title("Sales")
        self.root.iconbitmap("resoures\checklist.ico")
        self.root.config(bg="white")
        self.root.focus_force()

        self.invoice_list = []
        self.var_invoice = StringVar()


        ##Title
        title = Label(self.root, text="Customer Sales Invoices", font=("Century Gothic", 15, "bold"), bg="#000080", fg="white").place(x=40, y=10, width=1000)

        lbl_invoice = Label(self.root, text="Invoice No.", font=("times new roman", 15), bg="white").place(x=30, y=60)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow").place(x=150, y=60, width=200, height=30)  

        btn_search= Button(self.root, text="Search",command=self.search, font=("times new roman",15, "bold"), bg="green", fg="white", cursor="hand2").place(x=370, y=60, width=120, height=30)
        btn_clear= Button(self.root, text="Clear",command=self.clear, font=("times new roman",15, "bold"), bg="lightgray", fg="black", cursor="hand2").place(x=510, y=60, width=120, height=30)

        ##Invoices List
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=30, y=100, width=250, height=400)


        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)

        self.Sales_List = Listbox(sales_Frame, font=("Century Gothic", 15),bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1)

        ##calling get_data function on Invoice List
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        ##Bill Area
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=300, y=100, width=500, height=400)

        lbl_title2 = Label(bill_Frame, text="Sales Invoices Area", font=("Century Gothic", 20, "bold"), bg="#00997a").pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame,bg="lightyellow", yscrollcommand=scrolly.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        ##Image
        self.bill_img = Image.open("resoures/bill.png")
        self.bill_img = self.bill_img.resize((250,180))
        self.bill_img=ImageTk.PhotoImage(self.bill_img)
        
        lbl_image = Label(self.root,image=self.bill_img,bd=0)
        lbl_image.place(x=820, y=110)

        self.show()


##Adding invoices invoice list - Function
    def show(self):
        del self.invoice_list[:] ## delete store list before(empty list>> Ready to store new data)
        self.Sales_List.delete(0, END)
        # print(os.listdir('invoices'))        
        for i in os.listdir('invoices'):
            # print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.Sales_List.insert(END, i)
                self.invoice_list.append(i.split('.')[0]) ## add select invoice in invoice_list veriable(which made initial)
        
    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        # print(file_name)
        self.bill_area.delete('1.0', END) #delete previous select invoice
        fp = open(f'invoices/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice No. should be requried", parent = self.root)
        else:
            # print(self.invoice_list, self.var_invoice.get())
            if self.var_invoice.get() in self.invoice_list:
                # print("yes!! find the invocie")
                fp = open(f'invoices/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()  
            else:
                messagebox.showerror("Error", "Invaild Invoice No.", parent = self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()