import os
import pygame
from gtts import gTTS

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

if __name__ == "__main__":
    say_out_loud('The quick brown fox jumps over the lazy dog.')