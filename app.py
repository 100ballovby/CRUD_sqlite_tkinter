from tkinter import *
from tkinter import messagebox
from db import Database

# creating DataBase
db = Database('store.db')

# creating app main window
app = Tk()
# and its configuration
app.geometry('750x350')
app.title('Store Manager')

########## писать начинаем здесь ##########


def populate_list():
    parts_list.delete(0, END)
    for row in db.read():
        parts_list.insert(END, row)
        # очистить поле вывода заказов
        # прочитать содержимое БД
        # заполнить область вывода заказов данными из БД


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showwarning('Required Fields', 'Please fill all fields!')
        return


# Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 16), pady=20)
part_entry = Entry(app, textvariable=part_text)
part_label.grid(row=0, column=0)
part_entry.grid(row=0, column=1)
# Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer name', font=('bold', 16), pady=20)
customer_entry = Entry(app, textvariable=customer_text)
customer_label.grid(row=0, column=2)
customer_entry.grid(row=0, column=3)
# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer name', font=('bold', 16), pady=20)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_label.grid(row=1, column=0)
retailer_entry.grid(row=1, column=1)
# Price
price_text = DoubleVar()
price_label = Label(app, text='Price', font=('bold', 16), pady=20)
price_entry = Entry(app, textvariable=price_text)
price_label.grid(row=1, column=2)
price_entry.grid(row=1, column=3)
# Parts list (ListBox)
parts_list = Listbox(app, height=10, width=50, border=1)
parts_list.grid(row=3, column=0, columnspan=4, rowspan=6, pady=20, padx=20)
# Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=4)
# setting up Scrollbar
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Buttons
add_btn = Button(app, text='Add item', width=12, command=add_item)
remove_btn = Button(app, text='Remove item', width=12)
update_btn = Button(app, text='Update item', width=12)
clear_btn = Button(app, text='Clear fields', width=12)

add_btn.grid(row=2, column=0, pady=20)
remove_btn.grid(row=2, column=1, pady=20)
update_btn.grid(row=2, column=2, pady=20)
clear_btn.grid(row=2, column=3, pady=20)