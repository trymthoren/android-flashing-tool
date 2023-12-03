import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    # Function to open a file selection dialog
    file_path = filedialog.askopenfilename(title="Select a file to flash", filetypes=[("All files", "*.*")])
    if file_path:
        label.config(text=f"Selected file: {file_path}")
        flash_button.config(state=tk.NORMAL)
        return file_path
    else:
        return None

def flash_file(file_path):
    # ADB commands to restart into bootloader and flash the file
    os.system("adb reboot bootloader")
    os.system("sleep 10")  # Allowing time for the device to boot into bootloader
    os.system(f"adb flash {file_path}")
    label.config(text="Flashing done!")
    flash_button.config(state=tk.DISABLED)

# Setting up the GUI
root = tk.Tk()
root.title("Universal Android Flasher")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)
label = tk.Label(frame, text="Please select a file to flash")
label.pack(pady=20)
select_button = tk.Button(frame, text="Select File", command=lambda: select_file())
select_button.pack(pady=10)
flash_button = tk.Button(frame, text="Flash File", state=tk.DISABLED, command=lambda: flash_file(selected_file))
flash_button.pack(pady=10)
root.mainloop()
