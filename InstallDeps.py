import subprocess
import sys
import pkg_resources
import os

def install_requirements():
    required_packages = {
        'pillow': 'PIL',  # Package name : Import name
        'tkinter': 'tk',
        'datetime': 'datetime',
        'random': 'random',
        'string': 'string',
        'time': 'time'
    }
    
    print("Checking and installing required packages...")
    
    for package, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✓ Successfully installed {package}")
            except subprocess.CalledProcessError:
                print(f"✗ Failed to install {package}")
                return False
    
    print("\nAll dependencies are installed!")
    print("\nYou can now run KronOS.py")
    return True

if __name__ == "__main__":
    if install_requirements():
        input("\nPress Enter to exit...")
