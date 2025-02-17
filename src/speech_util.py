import os
import pygame
from gtts import gTTS
import wave
import pyaudio

from app_constants import temp_dir


def say_out_loud(text: str):

    # generate speech
    tts = gTTS(text=text, lang='en')

    # save audio in temporary file
    temp_filename = os.path.join(temp_dir, 'audio.mp3')
    tts.save(temp_filename)

    # initialize pygame mixer to play back audio
    pygame.init()
    pygame.mixer.init()

    # load and play the audio
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    # wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # clean up and remove the temp file
    pygame.mixer.quit()
    os.remove(temp_filename)


def convert_speech_to_text():
    pass


def get_speech_duration(text: str) -> int:
    # estimates the speech duration (in seconds) based on the number of words in the text.
    
    words_per_second = 2.5                                  # average speaking rate
    words_in_sentence = len(text.split())

    return max(3, words_in_sentence / words_per_second)     # return at least 3 seconds
     

def record_audio(filename: str, duration: int):
    # function: records audio from the microphone and saves it to a .wav file.
    # param filename: path to save the recorded audio.
    # param duration: recording duration in seconds.

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    # Open stream for recording
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print(f"🎤 Recording for {duration} seconds...")

    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded data to file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print("✅ Recording complete!") 


def transcribe_audio():
    pass


if __name__ == "__main__":
    # say_out_loud('The quick brown fox jumps over the lazy dog.')

    record_audio('../temp/temp_recording.wav', 5)
