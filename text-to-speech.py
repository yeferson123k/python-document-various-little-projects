import pyttsx3

string = "this is string!"

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# check voices

for voice in voices:
    print("Voice:")
    print("ID: %s" %voice.id)