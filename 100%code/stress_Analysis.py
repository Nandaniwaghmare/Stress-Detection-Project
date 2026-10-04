import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
import emotion_1_updated as validate
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
global msg
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Stress analysis using Face Recognition System")

# 430
#######lbl = tk.Label(root, text="Diabetic Retinopathy Detection System", font=('times', 35,' bold '), height=1, width=30,bg="seashell2",fg="indian red")
########lbl.place(x=350, y=5)
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('bg.jpeg')
image2 =image2.resize((1700,900), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Stress Detection System", font=("Times New Roman", 25, 'bold'),
                    background="powder blue", fg="black", width=85, height=2)
label_l1.place(x=0, y=0)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=200, y=100)
    
#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def evaluation():
        # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
        validate.upload()
def yoga():
        from subprocess import call
        call(['python','yoga.py'])
  

          

def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    update_label(msg)
    
   
    #mail(result)
    
# def mail(result):
#     import smtplib
#     from email.message import EmailMessage
#     import imghdr
    
#     Sender_Email = "ruchita.sct1@gmail.com"
#     Reciever_Email = "ruchita.sctcod@gmail.com"
    
#     Password ='7719849698'
#     newMessage = EmailMessage()    #creating an object of EmailMessage class
#     newMessage['Subject'] = "Sentiment Analysis" #Defining email subject
#     newMessage['From'] = Sender_Email  #Defining sender email
#     newMessage['To'] = Reciever_Email  #Defining reciever email  
#     newMessage.set_content(str(result)) #Defining email body
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(Sender_Email, Password)              
#         smtp.send_message(newMessage)
#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="Detection Using Face",command=evaluation,width=25, height=1,font=('times', 15, ' bold '), bg="#34495E", fg="white")
button3.place(x=20, y=180)

button4 = tk.Button(root, text="Prediction On Captured Images",command=prediction_emotion, width=25, height=1, bg="#34495E", fg="white",font=('times', 15, ' bold '))
button4.place(x=20, y=240)
button5 = tk.Button(root, text="Yoga suggestion",command=yoga, width=25, height=1, bg="#34495E", fg="white",font=('times', 15, ' bold '))
button5.place(x=20, y=300)

exit = tk.Button(root, text="Exit", command=window, width=25, height=1, font=('times', 15, ' bold '), bg="red",fg="white")
exit.place(x=20, y=360)

root.mainloop()