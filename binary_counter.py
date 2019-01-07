
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
tal = 0
talcompare = 0
try:
    while True:
        if (GPIO.input(21)):
            GPIO.output(2, GPIO.HIGH)
            #1 dvs +1
            tal1 = 1
#            GPIO.output(3, GPIO.LOW)
        else:
            GPIO.output(2, GPIO.LOW)
            tal1 = 0
        if (GPIO.input(20)):
            GPIO.output(3, GPIO.HIGH)
            # 2 dvs +2
            tal2 = 2
 #           GPIO.output(3, GPIO.LOW)
         #2
        else:
            GPIO.output(3, GPIO.LOW)
            tal2 = 0
            #GPIO.output(2, GPIO.LOW)
        if (GPIO.input(16)):
            # 4 dvs +2
            tal4 =4
        else:
            tal4 = 0

        time.sleep(0.1)
        tal = tal1 + tal2 +tal4
        if tal != talcompare:
            talcompare = tal
            print (tal)
finally:

#3 er rød 1
#2 er gul1

    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.cleanup()


