# Vox Cogitator TTS Terminal

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

A terminal-based voice assistant inspired by the Warhammer 40k universe, featuring speech-to-text (STT), text-to-speech (TTS), and real-time ASCII-art mouth animation for a digital "face." Designed as a fun, retro-style tool for voice interaction, with a nod to the Omnissiah's mechanical servants.

## Table of Contents
- [Features](#features)
- [Features to Add](#features-to-add)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Speech-to-Text (STT)**: Listens via microphone and converts spoken words to text using Google's recognition API.
- **Text-to-Speech (TTS)**: Converts text input into spoken audio using pyttsx3, with optional MP3 export.
- **Viseme Animation**: Maps phonemes (speech sounds) to ASCII-art mouth positions for visual feedback, simulating a talking face in the terminal.
- **Terminal-Based Interface**: Pure command-line operation with ANSI escape codes for cursor control and color.
- **Warhammer 40k Theme**: Named after the Vox Cogitator, evoking mechanical, arcane tech aesthetics.

## Features to Add
Based on the current codebase, here are suggested features to expand functionality. I've prioritized them by ease of implementation (using existing libraries) and potential impact. These could turn the project into a fully interactive voice chatbot.

### High Priority (Core Enhancements)
1. **Integrated Conversation Loop**: Combine STT, TTS, and face rendering into a single script (e.g., extend `main.py` or create a new `conversation.py`). Allow continuous back-and-forth dialogue, where the app listens, processes, responds, and animates in real-time.
   - *Why?* Currently, STT, TTS, and visemes are separate scripts. Integration would make it a cohesive app.
   - *Implementation*: Use threading for concurrent listening/speaking/animation. Add a simple NLP layer (e.g., keyword matching) for responses.

2. **Real-Time Viseme Sync with TTS**: During TTS playback, dynamically update the mouth animation based on the spoken phonemes, rather than simulating with character mapping.
   - *Why?* `main.py` is a static demo; real sync would make the "face" react to actual speech.
   - *Implementation*: Hook into pyttsx3's event system to detect phonemes and load/render ASCII art from `mouth-positions/` in sync.

3. **Improved Phoneme Detection**: Enhance `faceRenderer.py` to use a proper phoneme library (e.g., integrate with `phonemizer` or `espeak`) for more accurate mapping, supporting full words/phrases instead of single characters.
   - *Why?* Current mapping in `main.py` is basic (char-based); real phonemes would improve animation fidelity.
   - *Implementation*: Add a dependency for phoneme extraction and update the mapping dict.

### Medium Priority (User Experience)
4. **Audio Input/Output Handling**: Add options for microphone selection, noise reduction, and audio device configuration (e.g., via `pyaudio` settings).
   - *Why?* `stt.py` assumes default mic; users with multiple devices or noisy environments need flexibility.
   - *Implementation*: Use `speech_recognition`'s device selection and add command-line args.

5. **Customizable Voices and Languages**: Allow users to select TTS voices, speeds, and languages (pyttsx3 supports this). Add multi-language STT support beyond Google (e.g., fallback to offline engines like PocketSphinx).
   - *Why?* Enhances accessibility and fun; ties into the "cogitator" theme with varied "dialects."
   - *Implementation*: Expose pyttsx3 voice options via config or CLI.

6. **Error Handling and Logging**: Add robust error handling for network issues (Google STT), audio failures, and interruptions. Include logging for debugging.
   - *Why?* Current scripts have basic try/except; production-ready apps need better resilience.
   - *Implementation*: Use Python's `logging` module and add retries for API calls.

### Low Priority (Advanced/Experimental)
7. **Full Face Rendering**: Expand beyond mouth to include eyes, eyebrows, or a full ASCII face that reacts to speech (e.g., blinking, expressions).
   - *Why?* Builds on `faceRenderer.py`; makes it more immersive.
   - *Implementation*: Create more text files or use a library like `curses` for dynamic terminal graphics.

8. **Offline Mode**: Integrate offline STT/TTS (e.g., using PocketSphinx for recognition and eSpeak for synthesis) to avoid internet dependency.
   - *Why?* Useful for privacy or low-connectivity scenarios.
   - *Implementation*: Add conditional logic to switch engines based on availability.

9. **Conversation Memory**: Add a simple chat history or state machine to remember context across turns (e.g., using a dict or file).
   - *Why?* Turns it into a basic chatbot; could integrate with AI APIs like OpenAI for smarter responses.
   - *Implementation*: Store responses in a list and reference them.

10. **Packaging and Distribution**: Create a PyInstaller executable or Docker container for easy sharing. Add a setup.py or pyproject.toml for pip installation.
    - *Why?* Makes it distributable beyond the repo.
    - *Implementation*: Use PyInstaller to bundle the virtual env and scripts.

These features build incrementally on your existing code. Start with integration (1-3) to get a working prototype, then add polish (4-6).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/eric-delarosa/vox-cogitator-tts-terminal.git
   cd vox-cogitator-tts-terminal
   ```

2. **Set Up Virtual Environment** (recommended):
   ```bash
   python3 -m venv vox-cogitator
   source vox-cogitator/bin/activate  # On Windows: vox-cogitator\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt  # If you create one; see Dependencies below
   ```
   - Ensure you have a microphone for STT and speakers/headphones for TTS.
   - For Linux, install PortAudio if needed: `sudo apt-get install portaudio19-dev`.

## Usage
- **Run STT Demo**: `python stt.py` (listens and prints recognized text).
- **Run TTS Demo**: `python tts.py` (enter text to speak and save as MP3).
- **Run Viseme Demo**: `python main.py` (displays animated mouth for sample text).
- **Future Integrated App**: Once built, run `python conversation.py` for full interaction.

Example output from `main.py`:
```
Speaking: 'F'
       [  XXXXXXXXXXX  ]
```

## Dependencies
- Python 3.8+
- `speech_recognition` (for STT)
- `pyttsx3` (for TTS)
- `pyaudio` (for audio handling)

Create a `requirements.txt`:
```
speech_recognition==3.16.0
pyttsx3==2.99
pyaudio==0.2.14
```

## Project Structure
```
vox-cogitator-tts-terminal/
├── main.py              # Viseme animation demo
├── stt.py               # Speech-to-text script
├── tts.py               # Text-to-speech script
├── faceRenderer.py      # Viseme mapping and rendering class
├── mouth-positions/     # ASCII art files for mouth shapes
│   ├── closed.txt
│   ├── open.txt
│   └── ...
├── vox-cogitator/       # Virtual environment (ignore in repo)
├── README.md            # This file
└── requirements.txt     # Dependencies
```

## Contributing
Contributions are welcome! Fork the repo, create a feature branch, and submit a PR. Ideas:
- Improve viseme accuracy.
- Add unit tests.
- Enhance the Warhammer theme (e.g., sound effects).

## License
MIT License. See [LICENSE](LICENSE) for details.
