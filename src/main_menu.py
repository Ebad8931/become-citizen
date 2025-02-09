import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from app_constants import logo_path

class MainMenu(tk.Frame):
    def __init__(self, parent, navigate_to_coming_soon):
        super().__init__(parent)
        
        # Load the logo
        self.logo_img = Image.open(logo_path)
        self.logo_img = self.logo_img.resize((100, 100), Image.LANCZOS)  # Resize the logo
        self.logo = ImageTk.PhotoImage(self.logo_img)

        # Logo Display
        logo_label = tk.Label(self, image=self.logo)
        logo_label.pack(pady=20)

        # Menu Buttons
        options = [
            "Knowledge Test",
            "Reading Practice",
            "Listening Exercises",
            "Speaking Practice"
        ]

        for option in options:
            button = ttk.Button(self, text=option, command=navigate_to_coming_soon)
            button.pack(pady=10, ipadx=20, ipady=5)

        # Exit Button
        exit_button = ttk.Button(self, text="Exit", command=parent.quit)
        exit_button.pack(pady=10, ipadx=20, ipady=5)
