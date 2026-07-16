import re
from ollama import Client
from skills.apps import run as app_skill
from memory import remember, recall
from skills.web import search_web
from conversation import add_user, add_ai, get_history

client = Client(host="http://127.0.0.1:11434")


def ask_ai(prompt):
    prompt = prompt.strip()

    # ----- App Skills -----
    result = app_skill(prompt)
    if result:
        return result

    # ----- Learn user's name -----
    match = re.search(r"my name is (.+)", prompt, re.IGNORECASE)

    if match:
        name = match.group(1).strip()
        remember("name", name)
        return f"Nice to meet you, {name}. I'll remember your name."

    # ----- Recall user's name -----
    question = prompt.lower()

    if (
        "what is my name" in question
        or "what's my name" in question
        or "what my name" in question
        or "do you know my name" in question
    ):
        name = recall("name")

        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet."

    # ----- Web Search -----
    if prompt.lower().startswith("search "):
        query = prompt[7:]
        result = search_web(query)

        if result:
            return result

    # ----- Ask Ollama -----
    add_user(prompt)

    response = client.chat(
        model="llama3.2:3b",
        messages=get_history(),
    )

    answer = response["message"]["content"]

    add_ai(answer)

    return answer