# pip install pyaudio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("शुभ प्रभात!")

    elif hour>=12 and hour<=19:
        speak("नमस्ते!")  
    else:
         speak("शुभ रात्रि!")
    
    speak("कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("सुनना...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("मान्यता देना...")    
        query = r.recognize_google(audio, language='hi-in')
        print(f"उपयोगकर्ता ने कहा: {query}\n")

    except Exception as e:
        # print(e)    
        print("उसे एक बार फिर से बोलो कृपया...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bbke1979vines@gmail.com', '9351685024')
    server.sendmail('bbke1979vines@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'विकिपीडिया' in query:
            speak('विकिपीडिया खोज रहा है......')
            query = query.replace("विकिपीडिया", "")
            results = wikipedia.summary(query, sentences=4)
            speak("विकिपीडिया के अनुसार")
            print(results)
            speak(results)

        elif 'यूट्यूब' in query:
          webbrowser.open("youtube.com")
          speak("यूट्यूब खुल रहा है")

        elif 'गूगल' in query:
            webbrowser.open("google.com")
            speak("गूगल खुल रहा है")

        elif 'स्टैक ओवरफ़्लो' in query:
            webbrowser.open("stackoverflow.com")   
            speak("स्टैक ओवरफ़्लो खुल रहा है ")
        
        elif 'हनुमान' in query:
            webbrowser.open("https://search.brave.com/search?q=hanuman&source=desktop")   
            speak("महान हनुमान")

        elif 'epic' in query:
            webbrowser.open("epic game")
            speak("वेब पेज खुल रहा है")

        elif 'apna college' in query:
            webbrowser.open("https://www.apnacollege.in/?msg=not-logged-in")
            speak("वेब पेज खुल रहा है")

        elif 'python corse' in query:
            webbrowser.open("replit.com")
            speak("codewith herry वेब पेज खुल रहा है")

        elif 'file ' in query:
            folder = 'C:\\'
            os.startfile(folder)
            

        elif 'भजन' in query:
            music_dir = 'C:/Users/jitenDRA kumar saini/Music/JAISHIYARAM'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("भजन शुरू किया जाए")
        
        elif 'समय' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"सर !समय अभि {strTime}")
        
       
        elif 'python' in query:
            codePath = "B:\\Python projects"
            os.startfile(codePath)
            
         #cammunication part

        elif 'ओमान' in query:
            print("नमस्ते, मैं कैसे सेवा कर सकता हूं")
            speak("नमस्ते, मैं कैसे सेवा कर सकता हूं")

        elif 'नमस्ते' in query:
            print("अरे आप कैसे हैं")
            speak("अरे आप कैसे हैं")
        
        elif 'ठीक' in query:
            print("मैं भी अच्छा ही हूं!")
            speak("मैं भी अच्छा ही हूं!")
        
        elif 'तुम्हारा भाई' in query:
            speak("मेरे सभी दोस्त हैं, इसलिए मेरे बहुत सारे भाई और बहन हैं")
            print("मेरे सभी दोस्त हैं, इसलिए मेरे बहुत सारे भाई और बहन हैं") 

        elif 'नाम' in query:
            speak("  मेरा नाम ओमान है ")
            print("  मेरा नाम ओमान है") 

        
        elif 'email to jitendra' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jitendrayourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend jitendra bhai. I am not able to send this email")    
        else:
            print("")
          
        