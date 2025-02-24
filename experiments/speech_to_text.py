import speech_recognition as sr


recognizer = sr.Recognizer()

speech_duration = 5     # seconds until the mic will listen
speech_timeout = 3             # seconds to wait for the speech to start

try:
    with sr.Microphone() as source:
        audio = recognizer.adjust_for_ambient_noise(source)
        print("say something ...")
        audio = recognizer.listen(source, timeout=speech_timeout, phrase_time_limit=speech_duration) 

    speech_text = recognizer.recognize_google(audio).lower()
except sr.UnknownValueError:
    speech_text = "Could not understand. Try again."
except sr.RequestError:
    speech_text = "Speech recognition service unavailable."
except sr.WaitTimeoutError:
    speech_text = "No speech detected. Try again."

print(speech_text)