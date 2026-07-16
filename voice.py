import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

def speak(text):
    print("OdiAI:", text)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello! I am OdiAI. I am now connected to Ollama.")