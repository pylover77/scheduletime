import time
import pyttsx3
while True:
    a = time.strftime('%H:%M:%S', time.localtime())
    sp = pyttsx3.init()
    sp.say(f'Olá mestre Natan, agora são exatamente {a}')
    sp.runAndWait()
    print(a)
    time.sleep(3600)