from cProfile import label
from cgitb import text
from sqlite3 import Row
import tkinter as tk
from tkinter import *
parent = Tk()
parent.geometry("400x250")
parent.title("welcome to python")
name = Label(parent, text="name").grid(row=0, column=0)
e1 = Entry(parent).grid(row=0, column=1)
password = Label(parent, text="password").grid(row=1, column=0)
e2 = Entry(parent).grid(row=1, column=1)
submit = Button(parent, text="submit").grid(row=4, column=0)
parent.mainloop()