import tkinter as tk

from main_menu import MainMenu
from coming_soon import ComingSoon
from listening_exercise import ListeningExercise
from speaking_practice import SpeakingPractice
from app_constants import app_title, favicon_path


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(app_title)
        self.geometry("450x550")
        self.iconbitmap(favicon_path)

        # Initialize container frame
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_main_menu()

    def show_main_menu(self):
        """Displays the Main Menu screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        MainMenu(
            self.container, 
            self.show_coming_soon, 
            self.show_listening_exercise,
            self.show_speaking_practice
        ).pack(fill="both", expand=True)

    def show_coming_soon(self):
        """Displays the Coming Soon screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        ComingSoon(self.container, self.show_main_menu).pack(fill="both", expand=True)
    
    def show_listening_exercise(self):
        """Displays the Listening Exercise screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        ListeningExercise(self.container, self.show_main_menu).pack(fill="both", expand=True)
    
    def show_speaking_practice(self):
        """Displays the Speaking Practice screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        SpeakingPractice(self.container, self.show_main_menu).pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()