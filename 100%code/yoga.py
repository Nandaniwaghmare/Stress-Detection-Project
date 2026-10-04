import tkinter as tk
from tkinter import messagebox


def show_pose_details(pose):
    poses = {
        "Bhujangasana (Cobra Pose)": "Helps stimulate ovarian function and improves blood circulation to the pelvic region.",
        "Dhanurasana (Bow Pose)": "Strengthens the abdominal muscles and improves hormonal balance.",
        "Malasana (Garland Pose)": "Promotes relaxation of the pelvic muscles and helps regulate menstrual cycles.",
        "Setu Bandhasana (Bridge Pose)": "Stimulates thyroid function and helps balance hormones.",
        "Surya Namaskar (Sun Salutation)": "Improves overall metabolism and reduces stress, a key factor in PCOD management."
    }
    
    description = poses.get(pose, "Pose not found.")
    messagebox.showinfo(pose, description)

def create_yoga_app():
    root = tk.Tk()
    root.title("Yoga Poses For Relieving Stress")
    root.geometry("1300x700")
    
    tk.Label(root, text="Yoga Poses for PCOD Management", font=("Arial", 16), pady=10,fg="dark blue").pack()
    tk.Label(root, text="Select a yoga pose to learn more about its benefits:", font=("Arial", 12), pady=5,fg="dark blue").pack()
    
    poses = [
        "Bhujangasana (Cobra Pose)",
        "Dhanurasana (Bow Pose)",
        "Malasana (Garland Pose)",
        "Setu Bandhasana (Bridge Pose)",
        "Surya Namaskar (Sun Salutation)"
    ]
    
    colors = ["#FFDDC1", "#FFC1C1", "#D1FFC1", "#C1E1FF", "#E1C1FF"]
    
    for i, pose in enumerate(poses):
        tk.Button(
            root,
            text=pose,
            font=("Arial", 12),
            bg=colors[i],  # Assign background color from the list
            command=lambda p=pose: show_pose_details(p),
            pady=5
        ).pack(fill=tk.X, padx=20, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_yoga_app()


