import os
import pygame
from gtts import gTTS


# generate speech
tts = gTTS(text='Hello world!', lang='en')

# save audio in temporary file
temp_filename = 'audio.mp3'
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