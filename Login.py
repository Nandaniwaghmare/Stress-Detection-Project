import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk

# Initialize Main Window
root = tk.Tk()
root.title("Login Page")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
root.configure(bg="white")

username = tk.StringVar()
password = tk.StringVar()

# Load Background Image
bg_image = Image.open('reg1.jpg').resize((w, h), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image, master=root)
bg_label = tk.Label(root, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0)

# Frame for Login Box
frame = tk.Frame(root, bg="#ffffff", bd=10, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(frame, text="Login Here", font=("Arial", 25, "bold"), bg="#ffffff", fg="#900C3F")
title_label.grid(row=0, columnspan=2, pady=20)

# Username Entry
user_label = tk.Label(frame, text="Username:", font=("Arial", 16), bg="#ffffff")
user_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
user_entry = tk.Entry(frame, textvariable=username, font=("Arial", 14), bd=5, relief="groove")
user_entry.grid(row=1, column=1, padx=10, pady=10)

# Password Entry
pass_label = tk.Label(frame, text="Password:", font=("Arial", 16), bg="#ffffff")
pass_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
pass_entry = tk.Entry(frame, textvariable=password, show="*", font=("Arial", 14), bd=5, relief="groove")
pass_entry.grid(row=2, column=1, padx=10, pady=10)

# Function to Handle Login
# Function to Handle Login
def login():
    with sqlite3.connect('evaluation.db') as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration (Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, Gender TEXT, age TEXT, password TEXT)")
        db.commit()
        cursor.execute("SELECT * FROM registration WHERE username = ? AND password = ?", (username.get(), password.get()))
        result = cursor.fetchall()
        if result:
            ms.showinfo("Success", "Login Successful!")
            root.destroy()
            from subprocess import call
            call(["python", "stress_Analysis.py"])  # Yahan apni agli file ka sahi naam likhein
        else:
            ms.showerror("Error", "Invalid Username or Password")
# Function to Open Registration Page
def registration():
    from subprocess import call
    call(["python", "Register.py"])
    root.destroy()

# Login Button
login_btn = tk.Button(frame, text="Login", command=login, font=("Arial", 14, "bold"), bg="#28a745", fg="white", padx=10, pady=5, width=12)
login_btn.grid(row=3, column=1, pady=20)

# Register Button
register_btn = tk.Button(frame, text="Create Account", command=registration, font=("Arial", 14, "bold"), bg="#dc3545", fg="white", padx=10, pady=5, width=12)
register_btn.grid(row=3, column=0, pady=20)

root.mainloop()
