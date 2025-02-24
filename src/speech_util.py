import os
import pygame
from gtts import gTTS
import speech_recognition as sr

from app_constants import temp_dir


def synthesize_speech(text: str, output_file: str):
    tts = gTTS(text=text, lang='en')        # generate speech
    tts.save(output_file)                   # save in *.mp3 file


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


def say_out_loud(text: str):

    # save audio in temporary file
    audio_temp_file_path = os.path.join(temp_dir, 'audio.mp3')

    synthesize_speech(text, audio_temp_file_path)
    play_audio(audio_temp_file_path)

    os.remove(audio_temp_file_path)


def get_speech_duration(text: str) -> int:
    # estimates the speech duration (in seconds) based on the number of words in the text.
    
    words_per_second = 1.5                                                # average speaking rate
    words_in_sentence = len(text.split())

    speech_duration = words_in_sentence / words_per_second * 1.10           
    speech_duration = round(speech_duration * 1.10)                     # 10% buffer duration

    return max(3, speech_duration)                                      # return at least 3 seconds
     

def transcribe_audio(speech_duration: int) -> str:
    # speech to text function
    # transcribes audio by listening from the microphone and return the text in str format
    
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            audio = recognizer.adjust_for_ambient_noise(source)
            print("listening ...")
            audio = recognizer.listen(source, timeout=7, phrase_time_limit=speech_duration)

        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "⚠ Could not understand the audio."
    except sr.RequestError:
        return "⚠ Speech Recognition service unavailable."
    except sr.WaitTimeoutError:
        return "No speech detected. Try again."


if __name__ == "__main__":
    say_out_loud('The quick brown fox jumps over the lazy dog.')

    duration = get_speech_duration('The quick brown fox jumps over the lazy dog.')
    print('Duration', duration)

    print('Say what you just heard ...')
    text = transcribe_audio(duration)
    print('Recorded speech:', text)
