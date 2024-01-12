# import tkinter as tk

# def update_listbox(*args):
#     search_term = entry_var.get()

#     # Clear the listbox
#     listbox.delete(0, tk.END)

#     # Add search results to listbox
#     for item in list_items:
#         if search_term.lower() in item.lower():
#             listbox.insert(tk.END, item)

# root = tk.Tk()

# # List of items (this could be replaced with your own list)
# list_items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape']

# # Create a StringVar for the entry
# entry_var = tk.StringVar()
# entry_var.trace('w', update_listbox)

# # Create the entry
# entry = tk.Entry(root, textvariable=entry_var)
# entry.pack()

# # Create the listbox
# listbox = tk.Listbox(root)
# listbox.pack()

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# def select_item(event):
#     for item in tree.selection():
#         item_text = tree.item(item, "values")
#         print(item_text)  # You can replace this with your own code

# root = tk.Tk()

# # Create a Treeview
# tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")

# # Set the column headings
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")

# # Add some data
# tree.insert("", "end", values=("Alice", 25))
# tree.insert("", "end", values=("Bob", 30))
# tree.insert("", "end", values=("Charlie", 35))

# tree.bind("<<TreeviewSelect>>", select_item)

# tree.pack()

# root.mainloop()


import tkinter as tk
from tkinter import ttk

def update_combobox():
    # Clear the combobox
    combobox.set('')

    # Add new data to the combobox
    combobox['values'] = ['New item 1', 'New item 2', 'New item 3']

root = tk.Tk()

# Create a StringVar for the combobox
combobox_var = tk.StringVar()

# Create the combobox
combobox = ttk.Combobox(root, textvariable=combobox_var)

# Set the initial values in the combobox
combobox['values'] = ['Item 1', 'Item 2', 'Item 3']

combobox.pack()

# Add a button that updates the combobox when clicked
button = tk.Button(root, text="Update Combobox", command=update_combobox)
button.pack()

root.mainloop()


    def bill_middle(self): #update product list qty status
        con = sqlite3.connect(database = r'knoxims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid = [0]
                name = row[1]
                qty = row[3]
                if int(qty) == int(row[4]):
                    status = 'Inactive'
                
                if int(qty) != int(row[4]):
                    status = 'Active'                
                price = str(float(row[2]) * int(row[3]))
                self.txt_bill.insert(END, "\n "+name+"\t\t\t"+qty+"\tRs."+price) #change 1 line Item number, Qty, Price && second line Product Description
                ## update qty in product table
                cur.execute("Update items set quantity=?, status=? where item_code=?", (
                    qty,
                    status,
                    pid
                ))
                con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Erorr due to : {str(ex)}",  parent = self.root)
        con.close()
        self.show()