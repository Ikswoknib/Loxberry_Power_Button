#!/usr/bin/env python

# shutdown script for Raspberry Pi
# watch LOW level on pin 5 to enter sleep mode
# status led on pin 7: ON = ready, BLINK = confirm button

import RPi.GPIO as GPIO
import os
import time

# use the pin number as on the raspi board

GPIO.setmode(GPIO.BOARD)

# set pin 7 as output and HIGH, pin 5 is input

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(5, GPIO.IN)

# start the loop for every .5 seconds, waiting for LOW on pin 5
# then 2 short flashes with led to confirm and shutdown to sleep mode

while True:
        if not (GPIO.input(5)):
                        for i in range(1, 25):  #Frage 25 mal alle 0.1s den GPI$
                                if GPIO.input(5):
                                        for j in range(1,3):
                                                GPIO.output(7, False)
                                                time.sleep(.5)
                                                GPIO.output(7, True)
                                                time.sleep(.5)
                                        #print 'poweroff'
                                        os.system("sudo /sbin/poweroff")
                                        i = 0
                                        break
                                time.sleep(.1)
                        #while not (GPIO.input(5)):
                        #       time.sleep(.2)
                        if (i!=0):
                                for j in range(1,5):
                                        GPIO.output(7, False)
                                        time.sleep(.15)
                                        GPIO.output(7, True)
                                        time.sleep(.15)
                                #print 'restart'
                                os.system("sudo /sbin/reboot")

        time.sleep(.2)





