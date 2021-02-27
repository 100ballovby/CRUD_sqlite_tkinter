from tkinter import *
from tkinter import messagebox
from db import Database

# creating DataBase
db = Database('store.db')

# creating app main window
app = Tk()
# and its configuration
app.geometry('750x450')
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
    db.create(part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    # ^ получили данные
    parts_list.delete(0, END)  # очищаем список продуктов
    parts_list.insert(END, (part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0] # я хочу выбрать первую запись в списке
        selected_item = parts_list.get(index)
        # ^ сохраняю список с данными о продукте
        # затем очищаю все поля для ввода и заполняю их информацией о выбранном продукте
        part_entry.delete(0, END) # очистить поле
        part_entry.insert(END, selected_item[1]) # вставить название продукта
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    populate_list()


def remove_item():
    db.delete(selected_item[0])
    clear_text()
    populate_list()

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
# забиндим выбор
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add item', width=12, command=add_item)
remove_btn = Button(app, text='Remove item', width=12, command=remove_item)
update_btn = Button(app, text='Update item', width=12, command=update_item)
clear_btn = Button(app, text='Clear fields', width=12, command=clear_text)

add_btn.grid(row=2, column=0, pady=20)
remove_btn.grid(row=2, column=1, pady=20)
update_btn.grid(row=2, column=2, pady=20)
clear_btn.grid(row=2, column=3, pady=20)