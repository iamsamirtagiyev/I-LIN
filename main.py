import random
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

r = sr.Recognizer()

def speak(text):
    xtts = gTTS(text=text, lang='tr')
    file = 'file' + str(random.randint(0, 99999)) + '.mp3'
    xtts.save(file)
    playsound(file)
    os.remove(file)


def record():
    with sr.Microphone() as source:
        listen = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(listen, language='tr-TR')
        except sr.UnknownValueError:
            speak('ne dediğinizi anlayamadim')
        except sr.RequestError:
            speak('asisten calismiyor')
        
        return voice
    
start = False
voice  = record()



if voice != '':
    voice = voice.lower()


if 'aylin' in voice or 'hey aylin' in voice:
    speak('merhaba ben aylin. sana nasıl yardımcı ola bilirim')
    start = True


while(start):
    voice  = record()

    if 'kapat' in voice:
        speak('şimdilik hoşçakal. bana ihtiyacın olursa aylin demen yeterli')
        break

    if 'merhaba' in voice:
        speak('sana da merhaba')

    if 'selam' in voice:
        speak('sana da selam')

    if 'nasılsın' in voice:
        speak('iyiyim sen nasılsın')

    if 'bana bir ibne fotografi göster' in voice:
        speak('kahbe fotoğrafı açılıyor...')

    if 'video aç' in voice or 'müzik aç' in voice:
        speak('ne açmamı istersiniz')
        query = record().lower()
        url = 'https://www.youtube.com/results?search_query={}'.format(query)
        speak("youtubeda " + query + " açılıyor")
        browser = webdriver.Chrome()
        browser.get(url)

    if 'googlede ara' in voice or 'arama yap' in voice:
        speak('neyi aramamı istersiniz')
        query = record().lower()
        url = 'https://www.google.com/search?q={}'.format(query)
        speak("{} için arama yapılıyor".format(query))
        browser = webdriver.Chrome()
        browser.get(url)

    if 'film ara' in voice or 'film aç' in voice:
        speak('ne tür film açmami istersiniz')
        query = record().lower()
        url = 'https://www.filmmodu.tv/hd-film-kategori/{}'.format(query)
        speak("{} türü için bulduğum filmler bunlar".format(query))
        browser = webdriver.Chrome()
        browser.get(url)

    if 'hava durumu' in voice:
        speak('hangi şehirin hava durumunu bilmek istersiniz')
        query = record().lower()
        url = 'https://www.ntvhava.com/{}-hava-durumu'.format(query)
        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')

        morning = soup.find_all('div', {'class': 'daily-report-tab-content-pane-item-box-bottom-degree-big'})
        night = soup.find_all('div', {'class': 'daily-report-tab-content-pane-item-box-bottom-degree-small'})
        status = soup.find_all('div', {'class': 'daily-report-tab-content-pane-item-text'})

        morning_list = []
        night_list = []
        status_list = []

        for x in morning:
            x = x.text
            morning_list.append(x)
        
        for y in night:
            y = y.text
            night_list.append(y)
        
        for z in status:
            z = z.text
            status_list.append(z)

        sum = '{} için yarinki hava durumu. {}, gündüz sıcaklığı {}, gece sıcaklığı {}'.format(query, status_list[0], morning_list[0], night_list[0])
        speak(sum)
        



