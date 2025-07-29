import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print(f"🤖: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good Morning Jagarnath!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Jagarnath!")
    else:
        speak("Good Evening Jagarnath!")
    speak("Main aapka assistant hoon. Boliye kya karu main?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
        try:
            print("🧠 Recognizing...")
            query = r.recognize_google(audio, language='hi-IN')
            print(f"🗣️ You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, main samajh nahi paya. Phir se boliye.")
            return ""
        except sr.RequestError:
            speak("Speech service down hai.")
            return ""

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"Abhi samay hai {now}")

def open_youtube():
    speak("YouTube khol raha hoon.")
    webbrowser.open("https://www.youtube.com")

def open_google():
    speak("Google khol raha hoon.")
    webbrowser.open("https://www.google.com")

def open_whatsapp():
    try:
        whatsapp_path = os.path.expandvars(r"C:\Users\%USERNAME%\AppData\Local\WhatsApp\WhatsApp.exe")
        subprocess.Popen([whatsapp_path])
        speak("WhatsApp khul gaya.")
    except Exception as e:
        print(f"Error: {e}")
        speak("WhatsApp open karne mein dikkat aa gayi.")

def identify_name():
    speak("Aapka naam Jagarnath hai.")

def play_on_youtube(song_name):
    speak(f"{song_name} YouTube par chala raha hoon.")
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")

def search_google(query):
    speak(f"Google par ye dhundh raha hoon: {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    greet_user()
    while True:
        query = listen()

        if query == "":
            continue

        elif "google" in query or "गूगल" in query:
            speak("Google par search kar raha hoon.")
            search_query = query.replace("google", "").replace("गूगल", "").strip()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                os.system(f"start {url}")
            else:
                open_google()


        elif "play" in query or "गाना" in query or "सॉन्ग" in query:
            song = query.replace("play", "").replace("गाना", "").replace("सॉन्ग", "").strip()
            if song:
                play_on_youtube(song)
            else:
                speak("Konsa song chalana hai?")

        elif "google" in query or "गूगल" in query:
            search_google(query)

        elif "time" in query or "समय" in query or "टाइम" in query:
            tell_time()

        elif "your name" in query or "मेरा नाम" in query or "what is my name" in query:
            identify_name()

        elif "whatsapp" in query or "व्हाट्सएप" in query:
            open_whatsapp()

        elif "exit" in query or "बंद करो" in query or "bye" in query:
            speak("Bye Jagarnath, milte hain jald.")
            break

        else:
            speak("Main is command ko nahi samajh paya.")

if __name__ == "__main__":
    main()
