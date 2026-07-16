import sounddevice as sd
import soundfile as sf


def record_audio(filename="voice.wav", duration=5, samplerate=16000):
    print("🎤 Speak now...")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )

    sd.wait()  # Wait until recording is finished

    sf.write(filename, recording, samplerate)
    print(f"Recording saved as {filename}")


# Call the function
record_audio()