import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import pyaudio
import wave
import speech_recognition as sr

from app_constants import temp_dir


class SpeakingPractice(tk.Frame):
    def __init__(self, parent, back_to_menu):
        super().__init__(parent)

        # Title Label
        label = tk.Label(self, text="Speaking Practice", font=("Arial", 20, "bold"))
        label.pack(pady=50)

        # Message Label
        message = tk.Label(self, text="This feature is for the user to improve Speaking skills", font=("Arial", 14))
        message.pack(pady=20)

        self.record_button = ttk.Button(self, text="🎤 Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = ttk.Button(self, text="⏹ Stop Recording", command=self.stop_recording)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.transcribe_button = ttk.Button(self, text="📝 Convert to Text", command=self.convert_to_text)
        self.transcribe_button.pack(pady=10)
        
        self.text_output = tk.Text(self, height=5, width=40)
        self.text_output.pack(pady=10)

        # Back to Menu Button
        back_button = ttk.Button(self, text="Back to Menu", command=back_to_menu)
        back_button.pack(pady=30, ipadx=20, ipady=5)


    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.record_audio).start()
    
    def stop_recording(self):
        self.recording = False
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def record_audio(self):
        self.recording = True
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        
        while self.recording:
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        temp_audio_file = os.path.join(temp_dir, 'recorded_audio.wav')
        
        with wave.open(temp_audio_file, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
    

    def convert_to_text(self):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(os.path.join(temp_dir, 'recorded_audio.wav')) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", f"Could not process audio: {e}")