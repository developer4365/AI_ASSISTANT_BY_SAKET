# Personal AI Assistant

This is a Python-based personal AI assistant with voice interaction that can control your computer and Android phone (via ADB).

## Features
- Voice recognition and speech synthesis
- Control computer applications and system functions
- Control Android phone via ADB commands
- Web search functionality
- Command parsing for various tasks

## Requirements
- Python 3.7+
- Microphone for voice input
- Speakers for voice output
- Android device with USB debugging enabled (for Android control)
- ADB installed (Android SDK Platform Tools)

## Installation
1. Clone or download the project.
2. Navigate to the project directory.
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
5. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Ensure your microphone is working.
2. For Android control, connect your Android device via USB and enable USB debugging.
3. Run the assistant: `python assistant.py`
4. Speak commands like:
   - "Open notepad"
   - "Search for Python tutorials"
   - "Exit" to quit

## Supported Commands
- Open applications (e.g., "open notepad", "open calculator")
- Web search (e.g., "search for weather")
- Android control (placeholder for now)
- Exit the assistant

## Notes
- Android control is basic and requires ADB setup.
- Voice recognition uses Google Speech Recognition, so internet connection is required.
- Customize commands in the `parse_command` function as needed.
