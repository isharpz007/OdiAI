conversation = [
    {
        "role": "system",
        "content": (
            "You are OdiAI, a friendly personal AI assistant built by Odi. "
            "Be helpful and concise."
        ),
    }
]

def add_user(message):
    conversation.append({
        "role": "user",
        "content": message,
    })

def add_ai(message):
    conversation.append({
        "role": "assistant",
        "content": message,
    })

def get_history():
    return conversation