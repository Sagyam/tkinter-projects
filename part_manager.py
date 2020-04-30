from tkinter import Tk, StringVar, Label, Entry, W, Listbox, Scrollbar, Button, END, messagebox
from db import Database
db = Database('store.db')
global selected_item


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retail_text.get() == '' or price_text.get() == '':
        messagebox.showerror("Missing field", 'One or more field is missing')
        return
    db.insert(part_text.get(), customer_text.get(), retail_text.get(), price_text.get())
    populate_list()


def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)

    # Write to selected values to respective textbox
    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retail_entry.delete(0, END)
    retail_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])


def update_item():
    print("update")


def clear_text():
    print("clear")


def remove_item():
    print(select_item([0]))
    # db.remove(selected_item([0]))
    populate_list()


# Create window object
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 18), pady=20, padx=10)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold', 18), padx=10, pady=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retail
retail_text = StringVar()
retail_label = Label(app, text='Retail', font=('bold', 18), padx=10, pady=20)
retail_label.grid(row=1, column=0, sticky=W)
retail_entry = Entry(app, textvariable=retail_text)
retail_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 18), padx=10, pady=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Parts List
parts_list = Listbox(app, height=10, width=100, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Bind Select
parts_list.bind('<<ListboxSelect>>', select_item)

# Create scrollbar
scroll_bar = Scrollbar(app)
scroll_bar.grid(row=3, column=3)

# Connect scroll to listbox
parts_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=parts_list.yview)

# Buttons
add_btn = Button(app, text="Add part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove part", width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=20)

update_btn = Button(app, text="Update part", width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=20)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3, pady=20)

app.title("Part Manager")
app.geometry("720x480")
populate_list()

# Start program
app.mainloop()
