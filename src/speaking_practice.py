import os
import tkinter as tk
from tkinter import ttk
import threading
import time

from speech_util import get_speech_duration, transcribe_audio, evaluate_pronunciation


class SpeakingPractice(tk.Frame):
    def __init__(self, parent, back_to_menu):
        super().__init__(parent)

        self.sentence_to_speak = "The United States is a country of freedom and opportunity."

        # Title Label
        label = tk.Label(self, text="Speaking Practice", font=("Arial", 20, "bold"))
        label.pack(pady=50)

        # Instruction Label
        self.instruction_label = tk.Label(self, text="Click 'I'm Ready' and repeat the sentence:", font=("Arial", 12))
        self.instruction_label.pack(pady=20)

        # Sentence Display
        self.sentence_label = tk.Label(self, text=self.sentence_to_speak, font=("Arial", 14, "bold"), fg="blue")
        self.sentence_label.pack(pady=10)

        # Countdown Label
        self.countdown_label = tk.Label(self, text="", font=("Arial", 14, "bold"), fg="red")
        self.countdown_label.pack()

        # Ready Button
        self.ready_button = ttk.Button(self, text="I'm Ready", command=self.start_countdown)
        self.ready_button.pack(pady=10)

        # Recognized Speech Display
        self.recognized_var = tk.StringVar()
        self.recognized_label = tk.Label(self, textvariable=self.recognized_var, font=("Arial", 12), wraplength=400, fg="blue")
        self.recognized_label.pack(pady=10)

        # Feedback Display
        self.feedback_var = tk.StringVar()
        self.feedback_label = tk.Label(self, textvariable=self.feedback_var, font=("Arial", 12), wraplength=400, fg="green")
        self.feedback_label.pack(pady=10)

        # Back to Menu Button
        back_button = ttk.Button(self, text="Back to Menu", command=back_to_menu)
        back_button.pack(pady=30, ipadx=20, ipady=5)

    
    def start_countdown(self):
        
        # Starts the 3-2-1 countdown to before recording the user's voice
        self.ready_button.config(state=tk.DISABLED)
        self.countdown_label.config(text="Get ready...")
        self.update()
        time.sleep(1)

        for i in range(3, 0, -1):
            self.countdown_label.config(text=str(i))
            self.update()
            time.sleep(1)

        self.countdown_label.config(text="🎤 Speak now!")
        self.update()

        # Calculate duration based on sentence length
        duration = get_speech_duration(self.sentence_to_speak)

        # Start recording in a separate thread
        threading.Thread(target=self.record_and_process, args=(duration,), daemon=True).start()

        
    def record_and_process(self, speech_duration):

        # Convert speech to text
        transcript = transcribe_audio(speech_duration)
        print(transcript)
        self.recognized_var.set(transcript)

        self.countdown_label.config(text="✅ Recording complete!")

        # Provide feedback
        feedback = evaluate_pronunciation(self.sentence_to_speak, transcript) # self.get_feedback(transcript)
        print(feedback)
        self.feedback_var.set(feedback)


    def get_feedback(self, user_text):
        """Compares the user's spoken text with the expected text and provides feedback."""
        if not user_text:
            return "No speech detected. Try again!"
        
        expected_words = set(self.sentence_to_speak.lower().split())
        user_words = set(user_text.lower().split())

        correct_words = expected_words & user_words
        incorrect_words = expected_words - user_words

        if len(correct_words) / len(expected_words) > 0.8:
            return "Great job! Your pronunciation is close to perfect."
        elif len(correct_words) / len(expected_words) > 0.5:
            return "Good effort! Some words could be clearer."
        else:
            return "Try again! Focus on clearer pronunciation."