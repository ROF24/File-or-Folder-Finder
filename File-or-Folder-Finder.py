#importing the enviroments
import tkinter as tk
from tkinter import messagebox, filedialog
import os

#finding the folder or file in drive
def find_first_in_path(name, search_type):
    if search_type == "folder":
        my_path = os.path.expanduser("~")  # Home directory
    else:
        my_path = "C:\\"  # Root of C drive
    for root, dirs, files in os.walk(my_path):
        if search_type == "folder":
            for d in dirs:
                if d.lower() == name.lower():
                    return os.path.join(root, d)
        elif search_type == "file":
            for f in files:
                if f.lower() == name.lower():
                    return os.path.join(root, f)
    return None

#submit window
def on_submit():
    user_input = entry.get()
    search_type = var.get()
    path = find_first_in_path(user_input, search_type)
    if path:
        # Copy path to clipboard
        title.clipboard_clear()
        title.clipboard_append(path)
        title.update()  # Needed for clipboard to persist after window closes
        if search_type == "file":
            folder_path = os.path.dirname(path)  # Get containing folder
            os.startfile(folder_path)
        else:
            os.startfile(path)
        messagebox.showinfo(f"{search_type.title()} Found", f"Path: {path}")
    else:
        messagebox.showinfo("Not Found", f"{search_type.title()} '{user_input}' not found.")

# Create main window
title = tk.Tk()
title.title("Input Window")
title.geometry("350x130")

# Label
label = tk.Label(title, text="Enter name to search in your device:")
label.pack(pady=5)

# Text entry box
entry = tk.Entry(title, width=30)
entry.pack(pady=5)
entry.focus()

#choice dots
var = tk.StringVar(value="folder")

frame = tk.Frame(title)
frame.pack(pady=5)

folder_radio = tk.Radiobutton(frame, text="Folder", variable=var, value="folder")
folder_radio.pack(side=tk.LEFT, padx=10)

file_radio = tk.Radiobutton(frame, text="File", variable=var, value="file")
file_radio.pack(side=tk.LEFT, padx=10)

# Submit button
button = tk.Button(title, text="Submit", command=on_submit)
button.pack(pady=10)

#loop so you can submit as many as you want
title.mainloop()
