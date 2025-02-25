import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from speech_util import say_out_loud
from data import get_question


class ListeningExercise(tk.Frame):
    
    def __init__(self, parent, back_to_menu):
        super().__init__(parent)

        # Title Label
        label = tk.Label(self, text="Listening Exercise", font=("Arial", 20, "bold"))
        label.pack(pady=30)

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

        # setting up question for the exercise
        self.current_question = None
        self.selected_answer = None
        self.load_new_question()
    

    def play_question_audio(self):
        say_out_loud(self.current_question["text"])
        self.display_answer_choices(self.current_question["options"])


    def load_new_question(self):
        self.current_question = get_question()      # current question assigned
        self.selected_answer = None                 # clears the answer


    def display_answer_choices(self, answer_options):
        # clears existing option buttons
        for btn in self.option_buttons:
            btn.destroy()
        self.option_buttons.clear()

        # display answer choices
        for option in answer_options:
            btn = ttk.Button(self.frame_options, text=option, command=lambda opt=option: self.select_answer(opt))
            btn.pack(fill="x", padx=20, pady=2)
            self.option_buttons.append(btn)


    def select_answer(self, option):
        self.selected_answer = option


    def submit_answer(self):
        
        if not self.selected_answer:
            messagebox.showwarning("No Selection", "Please select an answer before submitting.")
            return

        is_correct = self.selected_answer == self.current_question["answer"]

        if is_correct:
            messagebox.showinfo('Correct!', 'Well done! You answered correctly.')
        else:
            messagebox.showerror('Wrong Answer', f'The correct answer was: {self.current_question["answer"]}')

        self.load_new_question()
        
        # hide the choices for the new question, will be available when the user plays the question
        self.display_answer_choices([])
