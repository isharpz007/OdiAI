import webbrowser
import subprocess
import os


def run(command):
    command = command.lower()

    if "open chrome" in command:
        webbrowser.open("https://google.com")
        return "Opening Chrome."

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    if "open vscode" in command or "open vs code" in command:
        subprocess.Popen("code")
        return "Opening VS Code."

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad."

    return None