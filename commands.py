import webbrowser
import subprocess
import os


def run_command(command):
    command = command.lower()

    if "open chrome" in command:
        webbrowser.open("https://google.com")
        return "Opening Chrome."

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    elif "open vscode" in command:
        subprocess.Popen("code")
        return "Opening VS Code."

    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad."

    return None