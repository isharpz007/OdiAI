# from brain import think
# from voice import speak

# print("=" * 40)
# print("      OdiAI",)
# print("=" * 40)

# while True:
#     command = input("you: ")
#     response = think(command)
#     print("OdiAI:", response)
#     speak(response)
#     if command.lower() == "bye":
#         break


from wake_word import listen
from brain import ask_ai
from voice import speak

print("🤖 OdiAI is running...")

while True:
    text = listen()

    if "hey odiai" in text:
        speak("Yes?")

        command = listen()

        if command:
            answer = ask_ai(command)
            print(answer)
            speak(answer)