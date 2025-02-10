import tkinter as tk
from tkinter import ttk

class ListeningExercises(tk.Frame):
    def __init__(self, parent, back_to_menu):
        super().__init__(parent)

        # Title Label
        label = tk.Label(self, text="Listening Exercises", font=("Arial", 20, "bold"))
        label.pack(pady=50)

        # Message Label
        message = tk.Label(self, text="Listen to the question and select an answer", font=("Arial", 14))
        message.pack(pady=10)

        # Play Audio Button
        self.btn_play_audio = ttk.Button(self, text="▶ Play Question", command=self.play_question_audio)
        self.btn_play_audio.pack(pady=10, ipadx=20, ipady=5)

        # Options Frame
        self.frame_options = tk.Frame(self)
        self.frame_options.pack(pady=10)

        self.option_buttons = []  # Store buttons for updating options dynamically

        # Submit Button
        self.btn_submit = ttk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.btn_submit.pack(pady=10, ipadx=20, ipady=5)

        # Back to Menu Button
        back_button = ttk.Button(self, text="Back to Menu", command=back_to_menu)
        back_button.pack(pady=30, ipadx=20, ipady=5)

        self.load_new_question()
    
    def play_question_audio(self):
        pass

    def load_new_question(self):
        pass
    
    def submit_answer(self):
        pass
