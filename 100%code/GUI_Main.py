

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Stress Detection System")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()



# 


bg_img1 = Image.open(r"img.jpg")

bg_img1.resize((w,h),Image.ANTIALIAS)
print(w,h)
bg_img1 = ImageTk.PhotoImage(bg_img1)

bg_img2=ImageTk.PhotoImage(Image.open("3.jpg"))

bg_img3=ImageTk.PhotoImage(Image.open("4.jpg"))

bg_lbl = tk.Label()
bg_lbl.place(x=0,y=0)
#, relwidth=1, relheight=1)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		bg_lbl.config(image=bg_img1)
	elif x == 2:
		bg_lbl.config(image=bg_img2)
	elif x == 3:
		bg_lbl.config(image=bg_img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



w = tk.Label(root, text="Stress Detection System",width=70,background="skyblue",height=2,font=("Times new roman",25,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","Login.py"])
    
def Register():
    from subprocess import call
    call(["python","Registration.py"])
    
def window():
    root.destroy()


wlcm=tk.Label(root,text="......Welcome to Stress Detection System ......",width=94,height=3,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=620)




d2=tk.Button(text="Login",command=Login,width=10,height=1,bd=5,background="pink",foreground="black",font=("times new roman",15,"bold"))
d2.place(x=100,y=150)


d3=tk.Button(text="Register",command=Register,width=10,height=1,bd=5,background="pink",foreground="black",font=("times new roman",15,"bold"))
d3.place(x=100,y=210)


d3=tk.Button(text="Exit",command=window,width=10,height=1,bd=5,background="pink",foreground="black",font=("times new roman",15,"bold"))
d3.place(x=100,y=270)

root.mainloop()
