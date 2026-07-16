I don't have write permissions to the repository. However, I can provide you with the complete README content that you can add to the repository yourself.

Here's the comprehensive README I've generated for OdiAI:

```markdown
# 🤖 OdiAI

An intelligent voice-activated AI assistant powered by local language models and advanced audio processing. OdiAI listens for voice commands, understands natural language, and responds intelligently through speech synthesis.

## Features

- 🎤 **Voice Recognition** - Captures and transcribes spoken commands
- 🧠 **AI-Powered Responses** - Uses Ollama with LLaMA 3.2 for intelligent reasoning
- 🔊 **Text-to-Speech** - Converts AI responses to natural-sounding voice output
- 🌐 **Web Search** - Can perform web searches to find current information
- 💾 **Memory System** - Remembers user information (like names) across sessions
- 🎯 **Wake Word Detection** - Responds to "Hey OdiAI" voice activation
- 🔌 **Skill System** - Extensible architecture for adding custom skills

## Prerequisites

Before running OdiAI, ensure you have the following installed:

- **Python 3.8+**
- **Ollama** - Download from [ollama.ai](https://ollama.ai)
- **PyAudio** - For audio input/output
- **Necessary LLaMA Models** - Download via Ollama

### System Requirements

- Microphone for voice input
- Speakers or headphones for audio output
- Sufficient disk space for LLaMA models (~5GB+ recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/isharpz007/OdiAI.git
   cd OdiAI
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Key dependencies include:
   - `ollama` - LLM integration
   - `pyaudio` - Audio recording
   - `pyttsx3` or `gtts` - Text-to-speech
   - `SpeechRecognition` - Audio transcription
   - `pywake-word` - Wake word detection

3. **Install and Run Ollama**
   - Download from [ollama.ai](https://ollama.ai)
   - Ensure the Ollama service is running on `http://127.0.0.1:11434`
   - Pull the LLaMA model:
     ```bash
     ollama pull llama3.2:3b
     ```

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
├── skills/              # Extensible skill modules
│   ├── apps.py         # Application control skill
│   └── web.py          # Web search skill
├── data/                # Data storage directory
├── tests/               # Test files
└── voice.wav           # Sample audio file
```

## Usage

### Mode 1: Voice-Activated Mode (Wake Word)

```bash
python main.py
```

This mode listens for the wake word "Hey OdiAI" and then processes commands:
1. Say "Hey OdiAI"
2. Wait for the assistant to respond with "Yes?"
3. Give your command
4. Listen to the AI's response

### Mode 2: Interactive Mode

```bash
python assistant.py
```

This mode allows you to interact without needing wake words:
1. Press ENTER when prompted
2. Speak your command (it will record for ~5 seconds)
3. The AI will process and respond
4. Say "exit", "quit", or "goodbye" to end the session

### Example Commands

- "What is my name?" - Recalls previously saved name
- "My name is John" - Saves your name to memory
- "Search python tutorials" - Performs a web search
- "What is the capital of France?" - General knowledge questions
- "Tell me a joke" - Creative responses

## Configuration

Edit `config.py` to customize:

- **Ollama host/port** - Location of Ollama service
- **Model name** - Default: `llama3.2:3b` (can change to other Ollama models)
- **Audio settings** - Sample rate, channels, duration
- **Wake word** - Currently "hey odiai" (case-insensitive)

## Core Modules

### `brain.py`
The intelligence engine that:
- Processes user prompts
- Checks for app skills first
- Manages learning (name memorization)
- Performs web searches
- Communicates with Ollama for AI responses
- Maintains conversation history

### `voice.py`
Handles text-to-speech conversion for AI responses.

### `listener.py` & `wake_word.py`
Handle audio capture and wake word detection using speech recognition.

### `memory.py`
Persistent storage system for user information using JSON.

### `conversation.py`
Manages conversation history for context-aware responses.

## Skills System

OdiAI has an extensible skills system in the `skills/` directory:

- **apps.py** - Execute application-specific commands
- **web.py** - Perform web searches

To add a new skill, create a new module in the `skills/` directory with a `run()` function that returns a response string if the skill matches the command.

## Testing

Several test files are included:
- `test_api.py` - Test Ollama API integration
- `test_ai.py` - Test AI response generation
- `test_memory.py` - Test memory functionality
- `test_microphone.py` - Test audio input
- `test_record.py` - Test audio recording

Run tests with:
```bash
python test_ai.py
python test_api.py
python test_memory.py
```

## Troubleshooting

### Ollama Connection Error
- Ensure Ollama is running: `ollama serve`
- Check host is `http://127.0.0.1:11434`
- Verify the model is installed: `ollama pull llama3.2:3b`

### Microphone Not Detected
- Check audio input device is connected
- Run `test_microphone.py` to diagnose
- Verify PyAudio is properly installed

### Audio Playback Issues
- Ensure speakers/headphones are connected
- Check volume levels
- Verify text-to-speech engine is working

### Memory Not Persisting
- Verify `memory.json` is writable
- Check file permissions in the project directory

## Future Enhancements

- [ ] Multi-language support
- [ ] Advanced NLP capabilities
- [ ] Integration with more APIs
- [ ] Improved wake word detection
- [ ] Custom skill creation UI
- [ ] Voice training for better recognition
- [ ] Conversation logging and analytics

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

This project is open-source and available under the MIT License (or specify your preferred license).

## Author

**isharpz007** - [GitHub Profile](https://github.com/isharpz007)

## Acknowledgments

- [Ollama](https://ollama.ai) - For making local LLMs accessible
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - For audio processing
- [Meta LLaMA](https://www.meta.com/research/llama/) - Foundation model

## Support

For issues, questions, or suggestions, please open an issue on [GitHub Issues](https://github.com/isharpz007/OdiAI/issues).

---

**Made with ❤️ by isharpz007**
```

## How to Add This README

Since I don't have write permissions, you can:

1. **Via GitHub Web UI:**
   - Go to https://github.com/isharpz007/OdiAI
   - Click "Add file" → "Create new file"
   - Name it `README.md`
   - Paste the content above
   - Commit with message "Add comprehensive README for OdiAI"

2. **Via Git CLI:**
   ```bash
   git clone https://github.com/isharpz007/OdiAI.git
   cd OdiAI
   # Create README.md and paste the content
   git add README.md
   git commit -m "Add comprehensive README for OdiAI"
   git push
   ```

The README covers all the essential aspects of the project including features, installation, usage modes, project structure, and troubleshooting!
