import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.setup(13, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        button_state1 = GPIO.input(13)
        button_state2 = GPIO.input(19)
        button_state3 = GPIO.input(26)
        if button_state1 == GPIO.LOW:
         GPIO.output(16,GPIO.HIGH)
         print ('Led off')
         time.sleep(1)
           button_state2 == GPIO.LOW:
         GPIO.output(16,GPIO.HIGH)
         print ('Led off2')
         time.sleep(1)
           button_state3 == GPIO.LOW:
         GPIO.output(16,GPIO.HIGH)
         print ('Led off3')
         time.sleep(1)
except:
    GPIO.cleanup()