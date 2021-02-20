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
