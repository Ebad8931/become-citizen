import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from app_constants import logo_path

class MainMenu(tk.Frame):
    
    def __init__(
        self, 
        parent, 
        navigate_to_coming_soon, 
        navigate_to_listening_exercise,
        navigate_to_speaking_practice
    ):
        super().__init__(parent)
        
        # Load the logo
        self.logo_img = Image.open(logo_path)
        self.logo_img = self.logo_img.resize((100, 100), Image.LANCZOS)  # Resize the logo
        self.logo = ImageTk.PhotoImage(self.logo_img)

        # Logo Display
        logo_label = tk.Label(self, image=self.logo)
        logo_label.pack(pady=20)

        # Define button width
        button_width = 20

        # Knowledge Test Button
        button = ttk.Button(self, text="Knowledge Test", command=navigate_to_coming_soon, width=button_width)
        button.pack(pady=10, ipadx=20, ipady=5)

        # Reading Practice Button
        button = ttk.Button(self, text="Reading Practice", command=navigate_to_coming_soon, width=button_width)
        button.pack(pady=10, ipadx=20, ipady=5)

        # Listening Exercise Button
        button = ttk.Button(self, text="Listening Exercise", command=navigate_to_listening_exercise, width=button_width)
        button.pack(pady=10, ipadx=20, ipady=5)

        # Speaking Practice Button
        button = ttk.Button(self, text="Speaking Practice", command=navigate_to_speaking_practice, width=button_width)
        button.pack(pady=10, ipadx=20, ipady=5)

        # Exit Button
        exit_button = ttk.Button(self, text="Exit", command=parent.quit, width=button_width)
        exit_button.pack(pady=10, ipadx=20, ipady=5)
