import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess
from pathlib import Path
import webbrowser

class ApplicationWindow:
    def __init__(self, parent, title, width=400, height=300):
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")
        self.window.attributes('-topmost', True)
        
        # Add title bar
        self.title_bar = tk.Frame(self.window, bg='#1f1f1f', height=30)
        self.title_bar.pack(fill='x')
        tk.Label(self.title_bar, text=title, fg='white', bg='#1f1f1f').pack(side='left', padx=5)
        tk.Button(self.title_bar, text='×', command=self.window.destroy).pack(side='right')

class ChromeWindow(ApplicationWindow):
    def __init__(self, parent):
        super().__init__(parent, "Chrome", 800, 500)
        self.frame = tk.Frame(self.window, bg='white')
        self.frame.pack(fill='both', expand=True)
        
        # Add toolbar
        toolbar = tk.Frame(self.frame, bg='#f1f1f1')
        toolbar.pack(fill='x', pady=2)
        
        # Navigation buttons
        tk.Button(toolbar, text="←", width=2).pack(side='left', padx=2)
        tk.Button(toolbar, text="→", width=2).pack(side='left', padx=2)
        tk.Button(toolbar, text="⟳", width=2).pack(side='left', padx=2)
        
        # URL bar
        url_frame = tk.Frame(toolbar, bg='white', relief='solid', bd=1)
        url_frame.pack(side='left', fill='x', expand=True, padx=5)
        tk.Label(url_frame, text="🔒", bg='white').pack(side='left', padx=2)
        url_bar = tk.Entry(url_frame, bd=0, highlightthickness=0)
        url_bar.pack(side='left', fill='x', expand=True, pady=5)
        url_bar.insert(0, "https://www.google.com")
        
        # Go button with better styling
        go_btn = tk.Button(toolbar, text="Go", bg='#4285f4', fg='white', padx=10)
        go_btn.config(command=lambda: webbrowser.open(url_bar.get()))
        go_btn.pack(side='left', padx=5)
        
        # Main content area
        content = tk.Frame(self.frame, bg='white')
        content.pack(fill='both', expand=True, pady=10)
        tk.Label(content, text="Google", font=('Arial', 24), bg='white').pack(pady=20)
        search_frame = tk.Frame(content, bg='white')
        search_frame.pack(pady=20)
        tk.Entry(search_frame, width=40, font=('Arial', 12)).pack()

class DesktopSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("KronOS")
        self.root.geometry("800x600")
        
        # Create desktop background
        self.desktop = tk.Frame(root, bg="#008080")
        self.desktop.pack(fill="both", expand=True)
        
        # Create taskbar
        self.taskbar = tk.Frame(self.desktop, bg="#c0c0c0", height=40)
        self.taskbar.pack(side="bottom", fill="x")
        
        # Add clock with fixed time
        self.clock_label = tk.Label(self.taskbar, text="5/4/25 7:15 PM", 
                                    bg="#c0c0c0", font=('Arial', 9))
        self.clock_label.pack(side="right", padx=10, pady=5)
        
        # Add start button
        self.start_btn = tk.Button(self.taskbar, text="Start", relief="raised")
        self.start_btn.pack(side="left", padx=5, pady=5)
        
        # Add power button
        self.power_btn = tk.Button(self.taskbar, text="Power", 
                                 command=self.run_kron,
                                 bg="red", fg="white")
        self.power_btn.pack(side="right", padx=5, pady=5)
        
        # Load icons
        self.icons = {
            "chrome": self.load_icon("chrome.png", (32, 32)),
            "computer": self.load_icon("computer.png", (32, 32)),
            "recycle": self.load_icon("recycle.png", (32, 32)),
            "notepad": self.load_icon("notepad.png", (32, 32)),
        }
        
        # Add desktop icons with images
        self.create_desktop_icon("Chrome", 0, self.icons["chrome"], self.open_chrome)
        self.create_desktop_icon("My Computer", 1, self.icons["computer"], self.open_computer)
        self.create_desktop_icon("Recycle Bin", 2, self.icons["recycle"], self.open_recycle)
        self.create_desktop_icon("Notepad", 3, self.icons["notepad"], self.open_notepad)

    def load_icon(self, icon_name, size):
        try:
            # First try to load from the same directory as the script
            icon_path = Path(__file__).parent / "icons" / icon_name
            if not icon_path.exists():
                # If not found, return None and the text-only version will be used
                return None
            img = Image.open(icon_path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except:
            return None

    def create_desktop_icon(self, name, position, icon=None, command=None):
        frame = tk.Frame(self.desktop, bg="#008080")
        if icon:
            btn = tk.Button(frame, image=icon, text=name, compound='top', command=command)
        else:
            btn = tk.Button(frame, text=name, command=command)
        btn.pack()
        frame.place(x=20, y=20 + (position * 90))

    def open_chrome(self):
        ChromeWindow(self.root)

    def open_computer(self):
        win = ApplicationWindow(self.root, "My Computer", 500, 400)
        main_frame = tk.Frame(win.window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # System files section
        files_frame = tk.Frame(main_frame, bg='white')
        files_frame.pack(fill='x', pady=10)
        tk.Label(files_frame, text="System Files", font=('Arial', 10, 'bold'), bg='white').pack(anchor='w')
        
        system_files = [
            ("system/config/system_config.py", "System Configuration"),
            ("system/services/network_service.py", "Network Service"),
            ("system/utils/security_monitor.py", "Security Monitor"),
            ("system/utils/process_manager.py", "Process Manager"),
            ("system/services/update_service.py", "Update Service")
        ]
        
        for filename, description in system_files:
            file_frame = tk.Frame(files_frame, bg='white')
            file_frame.pack(fill='x', pady=2)
            icon = self.load_icon("file.png", (16, 16))
            if icon:
                tk.Label(file_frame, image=icon, bg='white').pack(side='left', padx=5)
            tk.Label(file_frame, text=filename, font=('Arial', 9), bg='white').pack(side='left')
            tk.Label(file_frame, text=description, font=('Arial', 9), fg='gray', bg='white').pack(side='right')
        
        # Original drive display
        for drive in ['C:', 'D:']:
            drive_frame = tk.Frame(main_frame, relief='solid', bd=1)
            drive_frame.pack(fill='x', pady=5, padx=5)
            
            icon = self.load_icon("drive.png", (24, 24))
            if icon:
                tk.Label(drive_frame, image=icon).pack(side='left', padx=5)
            tk.Label(drive_frame, text=f"Local Disk ({drive})", font=('Arial', 10)).pack(side='left', pady=10)
            tk.Label(drive_frame, text="256 GB", fg='gray').pack(side='right', padx=10)

    def open_recycle(self):
        win = ApplicationWindow(self.root, "Recycle Bin", 400, 300)
        main_frame = tk.Frame(win.window, bg='white')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Add recycle bin icon
        icon = self.load_icon("recycle.png", (48, 48))
        if icon:
            tk.Label(main_frame, image=icon, bg='white').pack(pady=20)
        
        tk.Label(main_frame, text="Recycle Bin is Empty", 
                font=('Arial', 12), bg='white').pack()
        tk.Label(main_frame, text="Drop files here to delete", 
                fg='gray', bg='white').pack()
        
        # Add restore and empty buttons
        btn_frame = tk.Frame(main_frame, bg='white')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Empty Recycle Bin", state='disabled').pack(side='left', padx=5)
        tk.Button(btn_frame, text="Restore All", state='disabled').pack(side='left', padx=5)

    def open_notepad(self):
        win = ApplicationWindow(self.root, "Notepad", 600, 400)
        
        # Menu bar
        menu_bar = tk.Frame(win.window, bg='#f0f0f0')
        menu_bar.pack(fill='x')
        for menu in ['File', 'Edit', 'Format', 'View', 'Help']:
            tk.Button(menu_bar, text=menu, relief='flat', bg='#f0f0f0').pack(side='left', padx=5)
        
        # Text area with better styling
        text = tk.Text(win.window, wrap='word', font=('Consolas', 11))
        text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text)
        scrollbar.pack(side='right', fill='y')
        text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)

    def run_kron(self):
        # Get the directory where the script is located
        script_dir = Path(__file__).parent
        kron_path = script_dir / "Kron.py"
        
        try:
            subprocess.run(["python", str(kron_path)], check=True)
        except Exception as e:
            print(f"Error running Kron.py: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopSimulator(root)
    root.mainloop()
