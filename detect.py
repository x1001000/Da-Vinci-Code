import RPi.GPIO as GPIO
import time
import pygame

TRIG = 40
ECHO = 26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)
#time.sleep(2)
pygame.mixer.init()

def distance():
    #time.sleep(0.06)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

def play(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(0.06)

try:
    while True:
        d = distance()
        if 10 < d <= 30:
            print 'G'
            play('G.wav')
        elif 30 < d <= 50:
            print 'B'
            play('B.wav')
        elif 50 < d <= 70:
            print 'D'
            play('D.wav')
        else:
            time.sleep(0.06)
except:
    print 'E X C E P T'
    GPIO.cleanup()