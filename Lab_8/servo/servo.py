import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
servo_pin = 11
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,50)
pwm.start(7)

for i in range(0,180):
    dc = (i/18) + 2
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.05)

for i in range(180,0,-1):
    dc = (i/18 )+ 2
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.05)

pwm.stop()
GPIO.cleanup()