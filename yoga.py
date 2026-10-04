import tkinter as tk
from tkinter import messagebox

def show_pose_details(pose):
    poses = {
        "Bhujangasana (Cobra Pose)": "Relieves stress, fatigue, and opens up the chest to improve breathing and relaxation.",
        "Dhanurasana (Bow Pose)": "Stretches the back and abdomen, helping to relieve stress and anxiety.",
        "Malasana (Garland Pose)": "Calms the mind, relieves tension in the lower back and hips, and promotes relaxation.",
        "Setu Bandhasana (Bridge Pose)": "Calms the brain and helps alleviate stress and mild depression.",
        "Surya Namaskar (Sun Salutation)": "Boosts energy levels, improves focus, and significantly reduces stress and anxiety."
    }
    
    description = poses.get(pose, "Pose not found.")
    messagebox.showinfo(pose, description)

def create_yoga_app():
    root = tk.Tk()
    root.title("Yoga Poses For Stress Relief")
    root.geometry("1300x700")
    
    tk.Label(root, text="Yoga Poses for Stress Management & Relaxation", font=("Arial", 16, "bold"), pady=10, fg="dark blue").pack()
    tk.Label(root, text="Select a yoga pose to learn more about its benefits:", font=("Arial", 12), pady=5, fg="dark blue").pack()
    
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
            bg=colors[i],
            command=lambda p=pose: show_pose_details(p),
            pady=5
        ).pack(fill=tk.X, padx=20, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_yoga_app()


