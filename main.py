# Import all things
import tkinter as tk
import customtkinter
from customtkinter import *
from tkinter import *

# Create the window
root = customtkinter.CTk()
root.geometry("400x400")
root.title("TypeRight")

# Set the appearance
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Create the save function
def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text.get())

# create the save text button
save_text_button = CTkButton(root, text= "Save", command = save_text,)
save_text_button.pack(pady=5, padx=5)

# Create the textbox
text = tk.StringVar()
text_box = CTkEntry(root, width=400, height=420, textvariable = text)
text_box.pack (padx=10, pady=10)

# Create the mainloop to keep the app running
root.mainloop()