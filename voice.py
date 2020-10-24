import speech_recognition as sr
#import pyaudio


def record_volume():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as sourse:
        audio = r.listen(sourse)
    query = r.recognize_google(audio, language='ru-RU')
    print(query.lower().replace('-', ' '))


record_volume()
