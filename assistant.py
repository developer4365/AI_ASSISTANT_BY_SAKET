import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import os
import platform
import pyautogui
import time

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def open_app(app_name):
    system = platform.system()
    try:
        if system == "Windows":
            # Windows app open commands
            if app_name == "notepad":
                subprocess.Popen(["notepad.exe"])
            elif app_name == "calculator":
                subprocess.Popen(["calc.exe"])
            else:
                speak(f"Sorry, I don't know how to open {app_name} on Windows yet.")
        elif system == "Darwin":
            # macOS app open commands
            subprocess.Popen(["open", "-a", app_name])
        elif system == "Linux":
            subprocess.Popen([app_name])
        else:
            speak("Unsupported operating system.")
    except Exception as e:
        speak(f"Failed to open {app_name}. Error: {str(e)}")

def control_android(command):
    # Use adb commands to control android device
    # This is a placeholder for actual implementation
    try:
        if "open" in command:
            # Example: open app by package name or activity
            # User needs to specify app name or package
            speak("Opening app on Android is not implemented yet.")
        elif "send message" in command:
            speak("Sending message on Android is not implemented yet.")
        else:
            speak("Android control command not recognized.")
    except Exception as e:
        speak(f"Failed to control Android device. Error: {str(e)}")

def parse_command(command):
    if "open" in command:
        if "android" in command:
            control_android(command)
        else:
            # Extract app name after "open"
            app_name = command.replace("open", "").strip()
            open_app(app_name)
    elif "search" in command:
        # Extract search query
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye!")
        exit(0)
    else:
        speak("Sorry, I did not understand the command.")

def main():
    speak("Hello, I am your personal AI assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            parse_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()
