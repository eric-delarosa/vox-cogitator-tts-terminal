import pyttsx3
engine = pyttsx3.init()
text = input("Enter text to speak: ")

engine.say(text)
engine.runAndWait()

engine.save_to_file(text, 'output.mp3')
engine.runAndWait()

print("Text has been spoken and saved to output.mp3")