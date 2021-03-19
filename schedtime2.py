import sched 
import time 
import pyttsx3

scheduler = sched.scheduler()

def timenow():
    a = time.strftime('%H:%M:%S', time.localtime())
    sp = pyttsx3.init()
    sp.say(f'Hey Lord, its {a}')
    sp.runAndWait()
    print(a)
    scheduler.enter(delay=3600, priority=0, action=timenow)

timenow()
scheduler.run(blocking= True)


