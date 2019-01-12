
import RPi.GPIO as GPIO
import time
from tkinter import *

 
window = Tk()
 
window.title("Welcome Ida's binary counter  app")
window.geometry('600x300')
frame1 = Frame(window)
frame1header = Frame(window)

lbl = Label(window, text="Kontakter tændt", font=("Arial Bold", 50))
lbl2 = Label(window, text="Resultat: ", font=("Arial Bold", 50))

lrad1 = Label(frame1header,text='16',font=("Arial Bold", 50) )
lrad2 = Label(frame1header,text='8',font=("Arial Bold", 50))
lrad3 = Label(frame1header,text='4',font=("Arial Bold", 50))
lrad4 = Label(frame1header,text='2',font=("Arial Bold", 50))
lrad5 = Label(frame1header,text='1',font=("Arial Bold", 50))


rad1 = Label(frame1,text=" x",font=("Arial Bold", 50) )
rad2 = Label(frame1,text="o",font=("Arial Bold", 50))
rad3 = Label(frame1,text='o',font=("Arial Bold", 50))
rad4 = Label(frame1,text='o',font=("Arial Bold", 50))
rad5 = Label(frame1,text='o',font=("Arial Bold", 50))
txt = Label(window,text="42", font=("Arial Bold", 50))

lbl.pack()
frame1header.pack()
frame1.pack()
rad1.pack(side=LEFT)
rad2.pack(side=LEFT)
rad3.pack(side=LEFT)
rad4.pack(side=LEFT)
rad5.pack(side=LEFT)
lrad1.pack(side=LEFT)
lrad2.pack(side=LEFT)
lrad3.pack(side=LEFT)
lrad4.pack(side=LEFT)
lrad5.pack(side=LEFT)
lbl2.pack(side=LEFT)

lbl2.pack(side=LEFT)
txt.pack(side=LEFT)

counter = 0 
def counter_label(lbl):
  def count():
    global counter
    counter += 1
    lbl.config(text=str(counter))
    if (counter > 5):
        txt.config(text="77")

    lbl.after(1000, count)
  count()
#counter_label(lbl)

def go_switching(window):
    
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
                lbl.config(text=str(counter))
    finally:

    #3 er rød 1
    #2 er gul1

        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.cleanup()

    
window.after(1000,go_switching(window) )   
window.mainloop(    )

