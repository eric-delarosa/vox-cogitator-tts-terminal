import speech_recognition as sr
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said: " + text)
            
            if "exit" in text:
                print("Exiting...")
                break
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results;; {0}".format(e))
    except KeyboardInterrupt:
        print("Interrupted by user")
        break