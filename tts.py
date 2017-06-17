#it created by Carlos Williamberg on 06/14/2017

from espeak import espeak
import time

def speak():
    print('é faixa')
    espeak.set_voice('pt')
    espeak.speed = 1
    espeak.synth("é faixa de pedestre")
    time.sleep(1)
