import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Hello", "Welcome to GUI Programming!")

# Membuat jendela utama
root = tk.Tk()
root.title("Simple GUI Example")

# Menambahkan tombol ke jendela
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=20)

# Menjalankan loop utama
root.mainloop()
