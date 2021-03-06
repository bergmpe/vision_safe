#it created by Carlos Williamberg on 06/14/2017.

import RPi.GPIO as gpio
import time
import threading
import tts

HIGH = 1
LOW  = 0
BUZZER_PIN = 3
SWITCH_BUTTON = 13#button to switch mode

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(BUZZER_PIN, gpio.OUT)
gpio.setup(SWITCH_BUTTON, gpio.IN, pull_up_down=gpio.PUD_UP)

#beep_enable = True
BEEP_INTERVAL = 1#beep interval in seconds
mode = 0

def beep():
    try:
        gpio.output(BUZZER_PIN, LOW)
        time.sleep(BEEP_INTERVAL)
        gpio.output(BUZZER_PIN, HIGH)
        time.sleep(BEEP_INTERVAL)
    except KeyboardInterrupt:
        #gpio.cleanup()
        print('deu exption')
        exit
        
def vibracall():
    print('vibracall')


    
modes = {0: beep, 1: vibracall, 2: tts.speak}
notification = modes[mode]
#t = threading.Thread(target=beep)
#t.start()

def change_mode(channel):
    global mode
    mode += 1
    if mode == (len(modes)):
        mode = 0
    notification = modes[mode]
    #notification()
    print('changed mode', mode)
    
#notification = beep(1)
# add rising edge detection on the SWITCH_BUTTON, ignoring further edges for 200ms for switch bounce handling
gpio.add_event_detect(SWITCH_BUTTON, gpio.FALLING, callback=change_mode, bouncetime=200)


