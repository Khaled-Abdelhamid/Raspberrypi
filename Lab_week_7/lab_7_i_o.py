from time import sleep
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
button_1 = 16
button_2 = 12
led_1 = 22
led_2 = 18
GPIO.setup(button_1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_1,GPIO.OUT,)
GPIO.setup(led_2,GPIO.OUT)
BS1 = False
BS2 = False


while(1):
    if GPIO.input(button_1)==0:
        print("BS1 1 was pressed")
        if BS1==False:
            GPIO.output(led_1,True)
            BS1 = True
            sleep(0.5)
        else:    
            GPIO.output(led_1,False)
            BS1 = False
            sleep(0.5)

    if GPIO.input(button_2)==0:
        print("BS1 2 was pressed")
        if BS2==False:
            GPIO.output(led_2,True)
            BS2 = True
            sleep(0.5)
        else:    
            GPIO.output(led_2,False)
            BS2 = False
            sleep(0.5)