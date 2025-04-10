
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("speech_sample.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Transcription: ", text)
except Exception as e:
    print("Error:", e)
