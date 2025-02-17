import time
import threading
import tkinter as tk
from tkinter import messagebox

def countdown_timer(seconds, label):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02}:{secs:02}"
        label.config(text=timer_display)
        time.sleep(1)
        seconds -= 1

    messagebox.showinfo("Time's Up!", "Countdown finished!")

def start_timer():
    try:
        duration = int(entry.get())
        thread = threading.Thread(target=countdown_timer, args=(duration, timer_label))
        thread.start()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# Input field
entry_label = tk.Label(root, text="Enter time (seconds):")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

# Start button
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

# Timer display
timer_label = tk.Label(root, text="00:00", font=("Arial", 20))
timer_label.pack(pady=10)

# Run the application
root.mainloop()
