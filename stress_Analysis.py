import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import webbrowser
import emotion_1_updated as validate
    
# Initialize Tkinter window
root = tk.Tk()
root.configure(background="#2C3E50")  # Dark blue-gray background
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Stress Analysis using Face Recognition System")

# Background Image (If needed)
image2 = Image.open('s1.webp')
image2 = image2.resize((1700, 900), Image.LANCZOS)  
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

# %%
# Stylish Header

label_l1 = tk.Label(root, text="Mindease", font=("Helvetica", 28, 'bold'), 
                    background="#1ABC9C", fg="white", width=85, height=2, relief="raised", bd=3)
label_l1.place(x=0, y=0)

# Function to open links
def open_link(url):
    webbrowser.open_new(url)

# Function to update the UI with results
def update_label(result_text, yoga_url):
    """Displays stress evaluation and a clickable yoga link."""
    
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) and widget not in fixed_labels:
            widget.destroy()

    # Stress result label
    result_label = tk.Label(root, text=result_text, width=80, height=5, font=("Arial", 16, "bold"), 
                            bg='#ECF0F1', fg='black', relief="solid", bd=2)
    result_label.place(x=300, y=120)

    # Clickable yoga link
    link_label = tk.Label(root, text="Click here for suggested Yoga", fg="blue", cursor="hand2",
                          font=("Arial", 14, "underline"), bg='#ECF0F1')
    link_label.place(x=650, y=250)
    link_label.bind("<Button-1>", lambda e: open_link(yoga_url))

# Function to predict stress levels
def prediction_emotion():
    start = time.time()
    
    try:
        result_text, yoga_url = validate.files_count()  
    except ValueError:
        print("Error: files_count() did not return two values")
        return

    end = time.time()
    execution_time = "Execution Time: {0:.4f} seconds".format(end - start)
    final_result = result_text + '\n\n' + execution_time

    update_label(final_result, yoga_url)

# Start face detection
def evaluation():
    validate.upload()

# Open yoga suggestions
def yoga():
    from subprocess import call
    call(['python', 'yoga.py'])

# Exit function
def window():
    root.destroy()

# Button hover effect
def on_enter(e):
    e.widget.config(bg="#E67E22", fg="white")

def on_leave(e):
    e.widget.config(bg=e.widget.default_bg, fg="white")

# Fixed UI elements
fixed_labels = [label_l1]

# Button styling with different colors
button_styles = [
    {"bg": "#3498DB"},  # Blue
    {"bg": "#2ECC71"},  # Green
    {"bg": "#9B59B6"},  # Purple
    {"bg": "#E74C3C"}   # Red (Exit)
]

button_texts = [
    ("\U0001F4F7 Detection Using Face", evaluation),
    ("\U0001F4CA Prediction On Captured Images", prediction_emotion),
    ("\U0001F9D8 Yoga Suggestion", yoga),
    ("❌ Exit", window)
]

# Creating buttons with different colors
for i, (text, command) in enumerate(button_texts):
    style = {
        "font": ('Arial', 16, 'bold'),
        "width": 30,
        "height": 1,
        "bd": 3,
        "relief": "raised",
        "fg": "white",
        "activebackground": "#1ABC9C"
    }
    style.update(button_styles[i])
    
    btn = tk.Button(root, text=text, command=command, **style)
    btn.default_bg = style["bg"]  # Store default bg color
    btn.place(x=20, y=180 + (i * 70))
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
