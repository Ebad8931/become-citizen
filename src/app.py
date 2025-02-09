import tkinter as tk
from main_menu import MainMenu
from coming_soon import ComingSoon


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Become Citizen")
        self.geometry("500x500")
        self.iconbitmap("../assets/become-citizen-favicon.ico")

        # Initialize container frame
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_main_menu()

    def show_main_menu(self):
        """Displays the Main Menu screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        MainMenu(self.container, self.show_coming_soon).pack(fill="both", expand=True)

    def show_coming_soon(self):
        """Displays the Coming Soon screen."""
        for widget in self.container.winfo_children():
            widget.destroy()
        ComingSoon(self.container, self.show_main_menu).pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()