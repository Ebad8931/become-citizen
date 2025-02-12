import tkinter as tk
from tkinter import ttk

class SpeakingPractice(tk.Frame):
    def __init__(self, parent, back_to_menu):
        super().__init__(parent)

        # Title Label
        label = tk.Label(self, text="Speaking Practice", font=("Arial", 20, "bold"))
        label.pack(pady=50)

        # Message Label
        message = tk.Label(self, text="This feature is for the user to improve Speaking skills", font=("Arial", 14))
        message.pack(pady=20)

        # Back to Menu Button
        back_button = ttk.Button(self, text="Back to Menu", command=back_to_menu)
        back_button.pack(pady=30, ipadx=20, ipady=5)
