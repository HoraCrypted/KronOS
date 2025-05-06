import tkinter as tk
import random
import string
from datetime import datetime
import time

def get_display_text():
    now = datetime.now()
    # Check if current time is 07:15
    if now.hour == 7 and now.minute == 15:
        return "Fuyu"
    else:
        # Return a random 6-letter string
        return ''.join(random.choices(string.ascii_uppercase, k=6))

def update_label():
    new_text = get_display_text()
    label.config(text=new_text)
    # Update again after 60 seconds
    root.after(60000, update_label)

# Create the window
root = tk.Tk()
root.title("Kron")
root.geometry("300x150")

# Display label
label = tk.Label(root, text="", font=("Helvetica", 48))
label.pack(expand=True)

# Initialize display
update_label()

# Run the application
root.mainloop()