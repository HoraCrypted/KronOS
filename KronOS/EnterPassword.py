import tkinter as tk
import webbrowser

def check_password():
    if password_entry.get() == "Fuyu":
        root.destroy()
        webbrowser.open("https://archive.org/details/fuyu_20250506")

root = tk.Tk()
root.title("Password Verification")
root.geometry("300x150")

label = tk.Label(root, text="Enter password:", font=("Arial", 12))
label.pack(pady=20)

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Enter", command=check_password)
submit_button.pack(pady=20)

root.mainloop()
