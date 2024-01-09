import tkinter as tk
from customtkinter import CTk, CTkButton, CTkEntry, set_appearance_mode, set_default_color_theme

# Create the window
root = CTk()
root.geometry("400x400")

# Set the appearance
set_appearance_mode("light")
set_default_color_theme("blue")

# Create the save function
def save_text():
    filename = name.get()
    if filename:
        with open(f"{filename}.txt", "w") as f:
            f.write(text.get())
        save_text_button.config(text=f"Save the text as {filename}.")

<<<<<<< HEAD
root.title("TypeRight")

name = tk.StringVar()
file_name = CTkEntry(root, width=400, height=40, textvariable=name)
file_name.pack(padx=10, pady=10)
=======
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
            text.set(content)

open_text_button = CTkButton(root, text="Open", command=open_file)
open_text_button.pack(pady=5, padx=5)
>>>>>>> parent of 251c252 (Update main.py)

# create the save text button
save_text_button = CTkButton(root, text=f"Save the text as {name.get()}.", command=save_text)
save_text_button.pack(pady=5, padx=5)

# Create the textbox
text = tk.StringVar()
text_box = CTkEntry(root, width=400, height=420, textvariable=text)
text_box.pack(padx=10, pady=10)

root.mainloop()