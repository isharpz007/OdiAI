import whisper

model = whisper.load_model("base")

def transcribe_audio():
    result = model.transcribe("voice.wav")
    return result["text"].strip()