import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random

# Initialize the main window
window = tk.Tk()
window.title("REGISTRATION FORM")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.configure(background="#E3F2FD")  # Light blue background

# Variables
Fullname, address, username, Email, password, password1 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
Phoneno, age, var = tk.IntVar(), tk.IntVar(), tk.IntVar()

# Database setup
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS registration(
        Fullname TEXT, address TEXT, username TEXT, 
        Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, password TEXT
    )
""")
db.commit()

# Function to check password strength
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    return (len(passwd) >= 6 and 
            len(passwd) <= 20 and 
            any(char.isdigit() for char in passwd) and 
            any(char.isupper() for char in passwd) and 
            any(char.islower() for char in passwd) and 
            any(char in SpecialSym for char in passwd))

# Function to insert data into the database
def insert():
    fname, addr, un, email, mobile, gender, time, pwd, cnpwd = Fullname.get(), address.get(), username.get(), Email.get(), Phoneno.get(), var.get(), age.get(), password.get(), password1.get()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    # Validation checks
    if fname.isdigit() or fname == "":
        ms.showinfo("Message", "Please enter a valid name")
    elif addr == "":
        ms.showinfo("Message", "Please enter an address")
    elif not re.search(regex, email):
        ms.showinfo("Message", "Please enter a valid email")
    elif len(str(mobile)) != 10:
        ms.showinfo("Message", "Please enter a 10-digit mobile number")
    elif time <= 0 or time > 100:
        ms.showinfo("Message", "Please enter a valid age")
    elif password_check(pwd) is not True:
        ms.showinfo("Message", "Password must contain at least 1 uppercase, 1 lowercase, 1 symbol, and 1 number")
    elif pwd != cnpwd:
        ms.showinfo("Message", "Passwords do not match")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO registration VALUES(?,?,?,?,?,?,?,?)', (fname, addr, un, email, mobile, gender, time, pwd))
            conn.commit()
            ms.showinfo('Success!', 'Account Created Successfully!')
            from subprocess import call
            call(["python","Login.py"])
            window.destroy()

# UI Components

# Background Image
image2 = Image.open('bg7.png')
image2 = image2.resize((1700, 900), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0)

# Frame for Registration Form
frame = tk.LabelFrame(window, width=550, height=565, bd=5, font=('times', 14, 'bold'), bg="white", relief="ridge")
frame.place(x=450, y=135)

# Title Label
title_label = tk.Label(window, text="Registration Form", font=('times', 35, 'bold'), height=2, width=55, bg="#34495E", fg="white")
title_label.place(x=0, y=0)

# Labels & Entry Fields
fields = [
    ("Full Name:", Fullname, 30),
    ("Address:", address, 80),
    ("E-mail:", Email, 130),
    ("Phone No:", Phoneno, 180),
    ("Age:", age, 280),
    ("Username:", username, 330),
    ("Password:", password, 380, "*"),
    ("Confirm Password:", password1, 430, "*")
]

for text, var, y_pos, *args in fields:
    label = tk.Label(frame, text=text, width=15, font=("Times New Roman", 15, "bold"), bg="lightgray", bd=5)
    label.place(x=30, y=y_pos)
    entry = tk.Entry(frame, textvar=var, width=20, font=('', 15), bd=5, show=args[0] if args else "")
    entry.place(x=230, y=y_pos)

# Gender Selection
gender_label = tk.Label(frame, text="Gender:", width=12, font=("Times New Roman", 15, "bold"), bg="lightgray")
gender_label.place(x=30, y=230)
tk.Radiobutton(frame, text="Male", variable=var, value=1, bg="white", font=("bold", 15)).place(x=230, y=230)
tk.Radiobutton(frame, text="Female", variable=var, value=2, bg="white", font=("bold", 15)).place(x=340, y=230)

# Register Button with Hover Effect
def on_enter(e): register_btn.config(bg="#1A5276")
def on_leave(e): register_btn.config(bg="#34495E")

register_btn = tk.Button(frame, text="Register", font=("Arial", 18, "bold"), width=10, bg="#34495E", fg="white", command=insert, relief="raised")
register_btn.place(x=200, y=500)
register_btn.bind("<Enter>", on_enter)
register_btn.bind("<Leave>", on_leave)

window.mainloop()
