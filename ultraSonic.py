#Kevin Hinojosa
#This serves as a simple LED setup for GPIO usage.
#run power from 3.3V if connected directly
#otherwise output will con
#Use a 220 ohm resister --{red red brown gold}--
# Led long end is +ANode, short is -Cathode
#USE GPIO pin names
#UltrSonic needs .015 seconds to settle.

import RPi.GPIO as GPIO     #this allows us to use General Purpose Input Output Pins
import time                     #time allows us to use sleep function
GPIO.setmode(GPIO.BCM)      #this tells The pi how to read the pins, GPIO.BCM is titles, GPIO.BOARD is 12 34 56 78 starting at top left
GPIO.setup(18, GPIO.OUT)    #this tells the pi to use this pin as output LED
GPIO.setup(23, GPIO.OUT)    #this tells the pi to use this pin as output LED
GPIO.setup(5, GPIO.OUT)     #this is used for ultrasonic aka Trigger
GPIO.setup(6, GPIO.IN)      #this will accept input from HC-SRO4 ultrasonic sensor aka ECHO


counter=0
myBool= True

while counter<=5:
    print("counter is ", counter,".")
    GPIO.output(18, True)       #this sets output to True== 1 or False ==0.
    GPIO.output(23, False)
    print("Led On")
    time.sleep(.5)               #time is in seconds or milli(.150)

    GPIO.output(18, False)
    GPIO.output(23, True)
    print ("Led off")
    time.sleep(.5)
    counter=counter+1

def distance():
    print("distance func")
    GPIO.output(5, False)
    time.sleep(.000002)

    GPIO.output(5, True)
    time.sleep(.00001)
    GPIO.output(5, False)
    
    while GPIO.input(6) == 0:
        a=0
    time1= time.time()
    while GPIO.input(6) == 1:
        a=1
    time2 = time.time()

    during = time2 - time1
    print("exit dintance func")
    return (during * 340 / 2 * 100)



def loop():
    print ("loop funct")
    looper=0
    while (looper<10):
        dis = distance()
        print("looper count:", looper)
        print (dis, 'cm')
        print (time.sleep(0.3))
        time.sleep(1)
        looper=looper+1
    print ("exit loop funct")  

loop()
GPIO.cleanup() # cleanup all GPIO or we will have warning errors that pins are in use
