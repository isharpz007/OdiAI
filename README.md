# 🤖 OdiAI

**A voice-activated AI assistant that runs entirely on your machine.**

OdiAI listens for a wake word, transcribes what you say, reasons about it with a local LLM via [Ollama](https://ollama.ai), and speaks the answer back to you — no cloud API keys, no data leaving your computer.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-blue">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="Ollama" src="https://img.shields.io/badge/powered%20by-Ollama-black">
</p>

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Core Modules](#core-modules)
- [Skills System](#skills-system)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

| | |
|---|---|
| 🎯 **Wake Word Detection** | Responds to "Hey OdiAI" — no button presses needed |
| 🎤 **Voice Recognition** | Captures and transcribes spoken commands in real time |
| 🧠 **Local AI Reasoning** | Powered by Ollama running LLaMA 3.2 — fully offline inference |
| 🔊 **Text-to-Speech** | Converts responses into natural-sounding voice output |
| 💾 **Persistent Memory** | Remembers user details (like your name) across sessions |
| 🌐 **Web Search** | Looks up current information when local knowledge isn't enough |
| 🔌 **Extensible Skills** | Drop-in skill modules for custom commands and integrations |

## How It Works

```
🎙️  Wake word          "Hey OdiAI"
        ↓
📝  Transcription       listener.py + transcribe.py
        ↓
🧠  Reasoning           brain.py → skills check → memory check → Ollama (llama3.2:3b)
        ↓
🔊  Speech output       voice.py
```

## Prerequisites

- **Python 3.8+**
- **[Ollama](https://ollama.ai)** installed and running locally
- **A working microphone and speakers/headphones**
- **~5 GB free disk space** for the LLaMA model

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/isharpz007/OdiAI.git
cd OdiAI
```

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

Key packages installed:

| Package | Purpose |
|---|---|
| `ollama` | LLM integration |
| `pyaudio` | Audio recording |
| `pyttsx3` / `gtts` | Text-to-speech |
| `SpeechRecognition` | Audio transcription |
| `pywake-word` | Wake word detection |

**3. Install and start Ollama**

```bash
ollama serve
ollama pull llama3.2:3b
```

By default, OdiAI expects Ollama at `http://127.0.0.1:11434`.

**4. Verify the setup**

```bash
python test_microphone.py
python test_api.py
```

## Usage

### Voice-Activated Mode (recommended)

```bash
python main.py
```

1. Say **"Hey OdiAI"**
2. Wait for the assistant to respond with **"Yes?"**
3. Speak your command
4. Listen to the spoken response

### Interactive Mode (no wake word)

```bash
python assistant.py
```

1. Press **Enter** when prompted
2. Speak your command (records for ~5 seconds)
3. The AI processes and replies
4. Say **"exit"**, **"quit"**, or **"goodbye"** to end the session

### Example Commands

| Say this | OdiAI does this |
|---|---|
| "My name is John" | Saves your name to memory |
| "What is my name?" | Recalls it from memory |
| "Search python tutorials" | Runs a web search |
| "What is the capital of France?" | Answers a general knowledge question |
| "Tell me a joke" | Generates a creative response |

## Configuration

All settings live in `config.py`:

| Setting | Description | Default |
|---|---|---|
| Ollama host/port | Location of the Ollama service | `http://127.0.0.1:11434` |
| Model name | Ollama model used for reasoning | `llama3.2:3b` |
| Wake word | Phrase that triggers listening | `"hey odiai"` (case-insensitive) |
| Audio settings | Sample rate, channels, recording duration | see file |

## Project Structure

```
OdiAI/
├── main.py              # Wake-word activated entry point
├── assistant.py         # Manual interaction mode
├── brain.py             # Core AI logic and reasoning engine
├── voice.py             # Text-to-speech functionality
├── listener.py          # Audio recording
├── transcribe.py        # Audio transcription
├── wake_word.py         # Wake word detection
├── memory.py            # Persistent memory management
├── memory.json          # User data storage
├── conversation.py      # Conversation history management
├── commands.py          # Command handling
├── chat.py              # Chat utilities
├── config.py            # Configuration settings
├── skills/
│   ├── apps.py           # Application control skill
│   └── web.py            # Web search skill
├── data/                 # Data storage directory
├── tests/                # Test files
└── voice.wav             # Sample audio file
```

## Core Modules

- **`brain.py`** — The reasoning engine. Checks skills first, then memory, then falls back to Ollama for a general response; also maintains conversation history.
- **`voice.py`** — Converts AI text responses into speech.
- **`listener.py` / `wake_word.py`** — Handle audio capture and wake-word detection.
- **`memory.py`** — Persists user information to `memory.json`.
- **`conversation.py`** — Tracks conversation history for context-aware replies.

## Skills System

Skills live in `skills/` and let you extend OdiAI with custom commands.

To add a new skill:

1. Create a new module in `skills/`
2. Implement a `run()` function that returns a response string when the skill matches the command
3. OdiAI's `brain.py` will pick it up automatically on the next command check

Included by default:

- **`apps.py`** — Executes application-specific commands
- **`web.py`** — Performs web searches

## Testing

```bash
python test_ai.py          # AI response generation
python test_api.py         # Ollama API integration
python test_memory.py      # Memory persistence
python test_microphone.py  # Audio input
python test_record.py      # Audio recording
```

## Troubleshooting

<details>
<summary><strong>Ollama connection error</strong></summary>

- Make sure Ollama is running: `ollama serve`
- Confirm the host is `http://127.0.0.1:11434`
- Confirm the model is pulled: `ollama pull llama3.2:3b`
</details>

<details>
<summary><strong>Microphone not detected</strong></summary>

- Check that an audio input device is connected
- Run `python test_microphone.py` to diagnose
- Confirm PyAudio is installed correctly
</details>

<details>
<summary><strong>No audio output</strong></summary>

- Check that speakers/headphones are connected and volume is up
- Confirm the text-to-speech engine (`pyttsx3`/`gtts`) is installed and working
</details>

<details>
<summary><strong>Memory not persisting</strong></summary>

- Confirm `memory.json` exists and is writable
- Check file permissions in the project directory
</details>

## Roadmap

- [ ] Multi-language support
- [ ] Advanced NLP capabilities
- [ ] Integration with more APIs
- [ ] Improved wake-word detection accuracy
- [ ] UI for creating custom skills
- [ ] Voice training for better recognition
- [ ] Conversation logging and analytics

## Contributing

Contributions are welcome!

1. Fork the repo and create a feature branch
2. Make your changes
3. Add or update tests where relevant
4. Open a pull request describing what you changed and why

Bug reports and feature requests are just as welcome — please open an [issue](https://github.com/isharpz007/OdiAI/issues).

## License

Released under the [MIT License](LICENSE).

## Acknowledgments

- [Ollama](https://ollama.ai) — local LLM runtime
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) — audio I/O
- [Meta LLaMA](https://www.meta.com/research/llama/) — foundation model

---

**Author:** [isharpz007](https://github.com/isharpz007)
**Support:** [GitHub Issues](https://github.com/isharpz007/OdiAI/issues)
