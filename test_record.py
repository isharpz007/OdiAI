import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
samplerate = 16000  # Hz
filename = "voice.wav"

print("🎤 Recording... Speak now!")

recording = sd.rec(
    int(duration * samplerate),
    samplerate=samplerate,
    channels=1,
    dtype="float32"
)

sd.wait()  # Wait until recording is finished

sf.write(filename, recording, samplerate)

print(f"✅ Recording saved as {filename}")