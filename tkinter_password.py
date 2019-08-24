from tkinter import *
import tkinter as tk

import string
import random
import pyperclip


def rand_pw():
    global length_input


    special_chars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    digits = string.digits
    upper_keys = string.ascii_uppercase
    lower_keys = string.ascii_lowercase
    keys = digits + lower_keys + upper_keys + special_chars
    password_dict = []


    length = length_input.get()
    while len(password_dict) < int(length):
        password_dict.append(random.choice(keys))


    password = "".join(password_dict)
    pw_input.delete(0, END)
    pw_input.insert(10, password)

    return password


def copy():
    copy_pw = pw_input.get()
    pyperclip.copy(copy_pw)


#tkinter gui

root = Tk()
root.wm_iconbitmap('icon.ico')
root.geometry("470x130")
root.resizable(0,0)
root.title("Password Generator")

pw_label = Label(root, text="Password").grid(row=0, column=0, pady=4, padx = 4)
length_label = Label(root, text="Length").grid(row=2, column=0, pady=4, padx = 4)
pw_input = Entry(root, width=50)
length_input = Scale(root, from_=8, to=50, orient=HORIZONTAL, length= 305, activebackground='blue', tickinterval=42, width=9)
length_input.set(15)
pw_input.grid(row = 0, column = 1, pady=4, padx = 4)
length_input.grid(row = 2, column = 1)
Button(root, text='Quit', command=root.quit, width=10, bg='#AC0202').grid(row=3, column=2, sticky=W, pady=4)
Button(root, text='Generate', command=rand_pw, width=10).grid(row=2, column=2, sticky=W, pady=4)
Button(root, text='Copy', command=copy, width=10).grid(row=0, column=2, sticky=W, pady=4)

root.mainloop()

