from password_manager import PasswordManager
import tkinter as tk
from tkinter import messagebox
import os

#checks whether the file is empty
#if it is empty, a new key is generated
def is_file_empty(file_path):
    # Get the size of the file
    file_size = os.path.getsize(file_path)
    
    # Check if the file is empty (size is 0)
    return file_size == 0

key_path = 'key.key'
password_path = 'passwords.txt'

passwords = {}

pm = PasswordManager()

#the file should already be saved
#if the file's empty, make key
if is_file_empty(key_path):
    pm.create_key(key_path)
#otherwise, load already stored key
else:
    pm.load_key(key_path)

pm.create_password_file(password_path,passwords)

#function to add a password w/ site
def add_password():
    pm.add_password(site_name.get(),password.get())
    site_name_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)

#shows the password of one site
def show_password():
    pm.load_password_file(password_path)
    pw = pm.get_password(website.get())
    tk.messagebox.showinfo('Password',f'{pw}')
    site_entry.delete(0,tk.END)

window = tk.Tk()

#add password title thing
text = tk.Label(window,text='Add Password').grid(row=0,column=1)

#entry of site
site_name_label = tk.Label(window, text='Website Name:').grid(row=1,column=0)
site_name = tk.StringVar()
site_name_entry = tk.Entry(window, textvariable=site_name)
site_name_entry.grid(row=1,column=1)

#entry of password
password_label = tk.Label(window, text='Password:').grid(row=2,column=0)
password = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password)
password_entry.grid(row=2,column=1)

#button to add the password
add_password_button = tk.Button(window, text='Add',command=add_password).grid(row=3,column=1)

#show password title thingy
text = tk.Label(window, text='Show Password').grid(row=4,column=1)

#entering the site's name
site_label = tk.Label(window, text='Website Name:').grid(row=5,column=0)
website = tk.StringVar()
site_entry = tk.Entry(window, textvariable=website)
site_entry.grid(row=5,column=1)

#button to display the password
display_password = tk.Button(window, text='Show',command=show_password).grid(row=6,column=1)

window.mainloop()