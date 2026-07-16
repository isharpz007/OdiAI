from listener import record_audio
from transcribe import transcribe_audio
from brain import ask_ai
from voice import speak

print("🤖 OdiAI is ready!")

while True:
    input("\nPress ENTER to talk...")

    print("🎤 Listening...")
    record_audio()

    print("📝 Transcribing...")
    question = transcribe_audio()

    print("You:", question)

    if question.lower() in ["exit", "quit", "goodbye"]:
        speak("Goodbye!")
        break

    print("🧠 Thinking...")
    answer = ask_ai(question)

    print("OdiAI:", answer)

    speak(answer)