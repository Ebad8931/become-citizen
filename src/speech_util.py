import os
import pygame
from gtts import gTTS
import wave
import pyaudio
import speech_recognition as sr

from app_constants import temp_dir


def synthesize_speech(text: str, output_file: str):
    tts = gTTS(text=text, lang='en')        # generate speech
    tts.save(output_file)                   # save in file


def play_audio(audio_file_path: str):
    # initialize pygame mixer to play back audio
    pygame.init()
    pygame.mixer.init()

    # load and play the audio
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

    # wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # clean up and remove the temp file
    pygame.mixer.quit()
    os.remove(audio_file_path)


def say_out_loud(text: str):

    # save audio in temporary file
    temp_filename = os.path.join(temp_dir, 'audio.mp3')

    synthesize_speech(text, temp_filename)

    play_audio(temp_filename)



def get_speech_duration(text: str) -> int:
    # estimates the speech duration (in seconds) based on the number of words in the text.
    
    words_per_second = 2                                                # average speaking rate
    words_in_sentence = len(text.split())

    speech_duration = words_in_sentence / words_per_second * 1.10           
    speech_duration = round(speech_duration * 1.10)                     # 10% buffer duration

    return max(3, speech_duration)                                      # return at least 3 seconds
     

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


def transcribe_audio(audio_file: str) -> str:
    # speech to text function
    # transcribes audio from a file and returns the text in str format
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"📝 Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("⚠ Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("⚠ Speech Recognition service unavailable.")
        return ""


if __name__ == "__main__":
    say_out_loud('The quick brown fox jumps over the lazy dog.')

    # duration = get_speech_duration('The quick brown fox jumps over the lazy dog.')
    # print('Duration', duration)

    # record_audio('../temp/temp_recording.wav', duration)

    # transcribe_audio('../temp/temp_recording.wav')


