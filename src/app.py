import tkinter as tk

root = tk.Tk()
root.title("Hello World")

label = tk.Label(root, text="Hello, World!")
label.pack(padx=20, pady=20)

root.mainloop()