from gopigo import *
from time import *




## Global var for multithreading
etat = "stop"

def clignote():
    global etat
    while( etat == "stop"):
        print("clignote")
        led_on(LED_L)
        led_off(LED_R)
        sleep(0.5)
        led_on(LED_R)
        led_off(LED_L)
        sleep(0.5)

        
def avancer (n):
    fwd()
    led_on(LED_L)
    led_on(LED_R)
    sleep(n)
    led_off(LED_L)
    led_off(LED_R)
    stop()

def reculer (n):
    set_left_speed(72)
    bwd()
    led_on(LED_L)
    led_on(LED_R)
    sleep(n)
    stop()

    
#################### MAIN #################
import threading as Thread
import _thread
_thread.start_new_thread(clignote,())

servo (90)
set_left_speed(60)
set_right_speed(69)
'''
fwd()
sleep(1)
led_on(LED_L)
led_on(LED_R)
stop()
'''

avancer(2)
reculer (2)
